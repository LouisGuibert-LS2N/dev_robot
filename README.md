# ROBOT_CONTROL_LAUNCH
 Development for plateform robot - UC Merded

## **INSTALLATION**
### motor control & path control
1- Create a workspace

    mkdir -p ~/dev_robot_ws/src
    cd ~/dev_robot_ws/src

2- Download the package

    git clone https://github.com/LouisSEC/dev_robot/tree/main/src

3- Build the package

    colcon build

### lidar control
1- Create a workspace

    mkdir -p ~/lidar_ws/src
    cd ~/lidar_ws/src

2- Download the package

    git clone https://github.com/Slamtec/sllidar_ros2.git

3- Build the package

    colcon build


## **RUNNING PACKAGE**

**Be sure to have connected the Lidar to your device or virtual machine.**
**For vitual machine you have to selection the USB device in the parameter**

### WITH A SINGLE sh file :

In your workspace :

1- create a launch folder

    mkdir launch
    cd launch

2- create a launch file

    touch robot_control_launch.sh

3- Copy this code & modify path folders

    #!/bin/bash

    gnome-terminal --title="Lidar" -- bash -c 'cd ~/lidar_ws; source /opt/ros/foxy/local_setup.bash; source ./install/setup.bash; sudo chmod 777 /dev/ttyUSB0; ros2 launch sllidar_ros2  sllidar_s1_launch.py; $SHELL'

    gnome-terminal --title="Motor_control" -- bash -c 'cd ~/dev_robot_ws; source /opt/ros/foxy/local_setup.bash; source ./install/setup.bash; ros2 run robot_control motor_control'

    gnome-terminal --title="Path_control" -- bash -c 'cd ~/dev_robot_ws; source /opt/ros/foxy/local_setup.bash; source ./install/setup.bash; ros2 run robot_control path_control'

    kill -9 $PPID
    
   

### One by one
1- Open 3 terminal and source your environment
    In your workspace:

    source ./install/setup.bash
**2- For the lidar control terminal, don't forget to authorize the modification of USB port :**

    sudo chmod 777 /dev/ttyUSB0

3- run and launch ros2 nodes

    ros2 launch sllidar_ros2  sllidar_s1_launch.py

    ros2 run robot_control motor_control

    ros2 run robot_control path_control


## **modify the code**
3 files have been created to control the robot :
PATH: ~/dev_robot_ws/install/robot_control/lib/pyhton3.8/site-packages/robot_control

### Control_V3
This file correspond to the connection between your code and the robot.
All function are defined to have access to the robot / send data to the robot

### motor_control
This file is a ros2 node subscriber to the topic **motor_command**.
It is this file who send continuously the data (speed and orientation of each motor) to the robot

### path_control
This file is a ros2 node publisher to the topic **motor_command** and subscriber to the topic **scan**
This file decide which command sending to the robot, depending on sensors (here lidar)
You can define **cruise speed**, and path control
