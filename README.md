# LARM
Projet robot en UV LARM

🇬🇧 [English version below](#-english)

## Dépendances
Installation nécessaire de pyrealsense2
```sh
$ pip install pyrealsense2
```
Installation nécessaire de cv2
```sh
$ pip install opencv-python
```
Installation des ROS interfaces pour permettre de communiquer avec les boutons, bumpers...
```sh
cd $ROS_WORKSPACE
git clone https://github.com/imt-mobisyst/pkg-interfaces.git
colcon build --base-path pkg-interfaces
source ./install/setup.bash
```
## Install
```sh
git clone https://github.com/kykylechti/uvlarm-wall-e
colcon build --base-path pkg-interfaces
source ./install/setup.bash
```
## Get Started
Robot mobile
```sh
ros2 launch grp_pibot26 tbot_v1_launch.yaml
```
Simulation
```sh
ros2 launch grp_pibot26 simulation_v1_launch.yaml
```
### Déplacement
uvlarm-wall-e/grp_pibot26/scripts/direct_robot

Le robot est capable de se déplacer dans tout l'espace, sans se bloquer et sans n'avoir besoin de s'arrêter.
Ses mouvements sont fluides et il anticipe la venue d'obstacles.
Il se déplace aléatoirement dans l'espace afin d'explorer l'ensemble de la zone.
### Vision
uvlarm-wall-e/grp_pibot26/scripts/vision

Cette node repert la présence d'objets verts dans le champ de la caméra. Chaque objet détecté est comparé à un template du fantome. Si la corrélation est suffisante, un son est produit par le robot, un message est envoyé dans un topic dédié et la distance au robot est calculé.
Les objets détectés sont placés sur la carte en rouge pour les objets verts quelconques et en vert pour les fantomes. Deux points ne peuvent pas être placés à proximité et chaque fantome est identifié avec une ID unique.
### Fonctionalités supplémentaires
Le robot possède plusieurs fonctions d'arrêt avec les différents éléments qu'il possède : le bumper avant ainsi que les roules qui se relâchent.
Les boutons du robot permettent de relancer le mouvement automatique.
### Types de message personnalisés
Création de message personnalisés pour certains topics. Ces messages permettent par exemple de créer des flux d'image avec des coordonnées associées sur cette image.
### En cours de développement
Mouvement intelligent basé sur un algorithme de recherche du plus court chemin. Une fois ce chemin trouvé, l'objectif est d'identifier les points où des changements de direction ont lieu, puis d'orienter le robot et de l'envoyer jusqu'au prochain point.
Pour cela, nous cherchons les zones non identifiées sur la carte (-1) et sélectionnons les zones potentiellement accessibles pour le robot.

---

## 🇬🇧 English

## Dependencies
Requires pyrealsense2
```sh
$ pip install pyrealsense2
```
Requires cv2
```sh
$ pip install opencv-python
```
Install the ROS interfaces needed to communicate with the buttons, bumpers, etc.
```sh
cd $ROS_WORKSPACE
git clone https://github.com/imt-mobisyst/pkg-interfaces.git
colcon build --base-path pkg-interfaces
source ./install/setup.bash
```
## Install
```sh
git clone https://github.com/kykylechti/uvlarm-wall-e
colcon build --base-path pkg-interfaces
source ./install/setup.bash
```
## Get Started
Mobile robot
```sh
ros2 launch grp_pibot26 tbot_v1_launch.yaml
```
Simulation
```sh
ros2 launch grp_pibot26 simulation_v1_launch.yaml
```
### Movement
uvlarm-wall-e/grp_pibot26/scripts/direct_robot

The robot is able to move throughout the whole space without getting stuck and without needing to stop.
Its movements are smooth, and it anticipates upcoming obstacles.
It moves randomly through the space in order to explore the entire area.
### Vision
uvlarm-wall-e/grp_pibot26/scripts/vision

This node detects the presence of green objects in the camera's field of view. Each detected object is compared against a ghost template. If the correlation is high enough, the robot plays a sound, a message is published to a dedicated topic, and the distance to the robot is computed.
Detected objects are placed on the map in red for generic green objects and in green for ghosts. Two points cannot be placed too close to one another, and each ghost is identified with a unique ID.
### Additional features
The robot has several stop mechanisms tied to its different components: the front bumper as well as the wheels releasing.
The robot's buttons allow automatic movement to be restarted.
### Custom message types
Custom messages were created for certain topics. These messages make it possible, for example, to build image streams with coordinates associated to that image.
### Work in progress
Smart movement based on a shortest-path search algorithm. Once this path is found, the goal is to identify the points where direction changes occur, then orient the robot and send it to the next point.
To do this, we look for unidentified zones on the map (-1) and select the zones potentially accessible to the robot.
