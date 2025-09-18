# ROS Assignment 1: Turtlesim Publisher Implementation

## Overview
This assignment demonstrates a basic **ROS 2 Publisher** implementation using the built-in `turtlesim` package.  
Unlike the standard approach using the `turtle_teleop_key` node to control the turtle, the objective of this assignment is to **directly implement a Publisher node** that sends velocity commands to the `turtlesim_node`, thereby controlling the turtle programmatically.

---

## 1. Launching Turtlesim

Open two terminal windows and launch the following nodes:

```bash
ros2 run turtlesim turtlesim_node
ros2 run turtlesim turtle_teleop_key
```

The first command starts the `turtlesim_node` simulation, while the second allows for manual teleoperation of the turtle.  

---

## 2. Inspecting Topics

To observe the active ROS 2 topics, run:

```bash
ros2 topic list
```

Typical output:

```
/parameter_events
/rosout
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose
```

Among these, `/turtle1/cmd_vel` is the topic responsible for controlling the turtle’s motion.  

To inspect the message type of this topic, execute:

```bash
ros2 topic info /turtle1/cmd_vel
```

Expected output:

```
Type: geometry_msgs/msg/Twist
Publisher count: 1
Subscription count: 1
```

From this, it is evident that the `/turtle1/cmd_vel` topic uses the `geometry_msgs/msg/Twist` message type.

---

## 3. Message Structure and Dependencies

The `Twist` message consists of two primary components: **linear** and **angular** velocity, represented as vectors.  
When creating the ROS 2 package for this assignment, include `geometry_msgs` as a dependency.  
In the Publisher node, import the required message types:

```python
from geometry_msgs.msg import Twist, Vector3
```

> 📃 For further details on the `Twist` message structure, refer to the official ROS documentation:  
>[https://docs.ros.org/en/noetic/api/geometry_msgs/html/msg/Twist.html](https://docs.ros.org/en/noetic/api/geometry_msgs/html/msg/Twist.html)

---

## 4. Publisher Node Implementation

The Publisher node is implemented to send commands to `/turtle1/cmd_vel`, enabling autonomous control of the turtle.  
Refer to the files in this repository for the full implementation of `turtle_publisher.py`.

---

## 5. Demonstration

Upon executing the Publisher node, the turtle moves continuously to the right as illustrated below:  

![Turtle moving right](https://github.com/user-attachments/assets/a722eefd-a687-4929-9319-0f2c4c6c4fbb)

---

## Summary

This exercise demonstrates the fundamental workflow of ROS 2 Publisher-Subscriber communication, including:  

1. Launching and inspecting ROS nodes and topics.  
2. Identifying message types and configuring package dependencies.  
3. Implementing a custom Publisher node to programmatically control a simulated robot.

Through this assignment, students gain practical experience in **topic-based communication** in ROS 2 and the integration of standard message types for robot control.
