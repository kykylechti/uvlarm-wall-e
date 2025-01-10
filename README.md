# LARM
Projet robot en UV LARM

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

## Install
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
Il se déplace intelligemment dans l'espace afin d'explorer l'ensemble de la zone.

### Vision

uvlarm-wall-e/grp_pibot26/scripts/vision

La caméra permet au robot de détecter la présence d'objets verts.
Si la forme détectée est suffisament imposante, il considère que l'objet est trouvé et envoie un message String dans un topic dédié.

### Fonctionalités supplémentaires 
Le robot possède plusieurs fonctions d'arrêt avec les différents éléments qu'il possède : le bumper avant ainsi que les roules qui se relâchent.
Les boutons du robot permettent de relancer le mouvement automatique.
