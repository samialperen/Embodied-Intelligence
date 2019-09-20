# Assignment 1 of Embodied Intelligence Course

### Prerequisities
* Ubuntu 18.04 (Bionic)
* ROS-Melodic
* Gazebo

Braitenberg vehicles were implemented using ROS and Gazebo in C++. As a sensor, 360 point laserscan messages were divided into four regions: north, west , south and east. One can think these regions as a four different sensor. As a stimulus, simple objects in the Gazebo environment was used. 

**NOTE:** This assignment can be useful for people who are trying to subscribe ROS laserscan messages and process them since in the time being, there is not any source in the web in C++ although there are many in Python.

**Keywords:** subscribe laserscan cpp, C++, process laserscan, laser processing, ROS, gazebo

As a simulation environment and robot, Turtlebot3 Burger was used in Turtlebot3 empty world environment. 

### Install Turtlebot3 and Turtlebot3-Gazebo
```
$ sudo apt-get install ros-melodic-turtlebot3
$ sudo apt-get install ros-melodic-turtlebot3-gazebo
```

### Run
```
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
$ rosrun assignment1 scan_listener
```

For more information, check the source code.
You can see demo videos of the results [here](/assignment1/videos)

