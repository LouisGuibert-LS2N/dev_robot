#!/bin/bash

gnome-terminal --title="Lidar" -- bash -c 'cd ~/lidar_ws; source /opt/ros/foxy/local_setup.bash; source ./install/setup.bash; sudo chmod 777 /dev/ttyUSB0; ros2 launch sllidar_ros2  sllidar_s1_launch.py; $SHELL'

gnome-terminal --title="Motor_control" -- bash -c 'cd ~/dev_robot_ws; source /opt/ros/foxy/local_setup.bash; source ./install/setup.bash; ros2 run robot_control motor_control'

gnome-terminal --title="Path_control" -- bash -c 'cd ~/dev_robot_ws; source /opt/ros/foxy/local_setup.bash; source ./install/setup.bash; ros2 run robot_control path_control'

kill -9 $PPID
