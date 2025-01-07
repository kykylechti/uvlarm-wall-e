#!/usr/bin/python3
import rclpy
import math
import random
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from rclpy.node import Node

obstacleDetec = "noScan"    # Détection des obstacles
memory = "no"               # Détection précédente différente de la détection actuelle
i = 0                       # Rotations aléatoires à effectuer
stop = 0                    # Arrêt d'urgence
defaultSpeed = 0.5          # Vitesse par défaut 
defaultRotSpeed = 1.0       # Vitesse de rotation par défaut

# Arrêt d'urgence par bumper
class ROSListener: 
    def __init__(self, rosNode): 
        self._logger = rosNode.get_logger()
        self._subscription=rosNode.create_subscription(BumperEvent, '/events/bumper', self.listener_callback, 10)
    
    def listener_callback(self, msg):
        global stop
        if msg.state==1:
            stop=1

class StraightCtrl:
    def initializeRosNode(self, rosNode ):
        # Get logger from the node:
        self._logger= rosNode.get_logger()

        # Initialize publisher:
        self._pubVelocity= rosNode.create_publisher(
            Twist, '/multi/cmd_nav', 10
        )

        # Initialize scan callback:
        self._subToScan= rosNode.create_subscription(
            LaserScan, 'scan',
            self.scan_callback, 10
        )

        # Initialize control callback:
        self._timForCtrl= rosNode.create_timer(
            0.05, self.control_callback
        )

    def scan_callback(self, scanMsg ):
        self._logger.info( '> get scan' )
        global obstacleDetec, i

        obstaclesLeft= []
        obstaclesRight= []
        angle= scanMsg.angle_min
        for aDistance in scanMsg.ranges :
            if(angle<1.0 and angle>0.0) and (0.05 < aDistance and aDistance < 0.25) : #-57° à 0° environ
                aPoint= [
                    math.cos(angle) * aDistance,
                    math.sin(angle) * aDistance
                ]
                obstaclesLeft.append(aPoint)
            if(angle<0.0 and angle>-1.0) and (0.05 < aDistance and aDistance < 0.25) : #0° à 57° environ
                aPoint= [
                    math.cos(angle) * aDistance,
                    math.sin(angle) * aDistance
                ]
                obstaclesRight.append(aPoint)
            angle+= scanMsg.angle_increment
        
        if len(obstaclesLeft) == 0 and len(obstaclesRight) == 0:    # pas d'obstacles détectés dans la zone
            obstacleDetec = "no"
        elif len(obstaclesLeft) != 0 and len(obstaclesRight) == 0:  # obstacle détecté à gauche
            obstacleDetec = "left"
        elif len(obstaclesLeft) == 0 and len(obstaclesRight) != 0:  # obstacle détecté à droite
            obstacleDetec = "right"
        elif len(obstaclesLeft) != 0 and len(obstaclesRight) != 0:  # obstacle détecté des deux cotés
            obstacleDetec = "both"

            

    def control_callback(self):
        self._logger.info( '< define control' )
        global obstacleDetec, i

        memory='no'
        # Dès qu'on change d'état, la mémoire change (si l'obstacle a été détecté à droite en premier il continue de tourner à gauche et inversement)
        if (memory=='no' and (obstacleDetec=='left' or obstacleDetec=='right'))and ((memory=='left' or memory=='right') and obstacleDetec=='no'): 
            memory=obstacleDetec
        # Si jamais il est détecté des deux cotés en même temps
        elif (obstacleDetec=='both' and memory=='no'): 
            memory='both'

        velocity = Twist()                                  # initialisation du Twist
        if i!=0:
            velocity.linear.x = 0.0
            velocity.angular.z = -defaultRotSpeed
            i-=1
        elif memory == 'no':                                # Aller tout droit
            velocity.linear.x = defaultSpeed
            velocity.angular.z = 0.0
        elif memory == 'left':                              # Tourner à droite
            velocity.linear.x = 0.0
            velocity.angular.z = -defaultRotSpeed
        elif memory == 'right':                             # Tourner à gauche
            velocity.linear.x = 0.0
            velocity.angular.z = defaultRotSpeed
        elif memory =='both':                               # Tourner à gauche pendant une durée aléatoire
            i=random.randint(5, 30)
            velocity.linear.x = 0.0
            velocity.angular.z = -defaultRotSpeed
            memory='no'

        self._pubVelocity.publish(velocity)
    

def main():
    # Initialisation du noeud
    rclpy.init()
    node= Node( 'basic_move' )

    # Appel du contrôle
    control= StraightCtrl()
    control.initializeRosNode( node )

    # Infinite Loop:
    rclpy.spin( node )

    # Fin du programme
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
	main()

