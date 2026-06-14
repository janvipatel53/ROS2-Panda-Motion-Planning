Project: Robotic Arm Kinematics using ROS2 and Panda Robot
Objective

The aim of this project was to understand the basic working of a Panda robotic arm in ROS2 by reading joint values and finding the end-effector position.

Steps Performed
Step 1: Workspace Setup

Created and built the ROS2 workspace.

Commands used:

mkdir -p ~/robot_ws/src

cd ~/robot_ws

colcon build

source install/setup.bash
Step 2: Created a Basic ROS2 Node

Created a simple node to check whether the package was working properly.

Run command:

ros2 run <package_name> hello_node

Output:

DecodeLabs Project Started!
Step 3: Reading Joint States

Created joint_reader.py to subscribe to the /joint_states topic and print joint names and positions.

Command:

ros2 run <package_name> joint_reader
Step 4: Monitoring Panda Arm Joints

Created joint_monitor.py to display the seven Panda arm joints separately.

Command:

ros2 run <package_name> joint_monitor

Output:

panda_joint1
panda_joint2
...
panda_joint7
Step 5: Forward Kinematics

Created fk_monitor.py using TF2.

The node reads the transform between:

panda_link0
      ↓
panda_hand

and displays the end-effector position.

Command:

ros2 run <package_name> fk_monitor

Sample Output:

X: 0.432 m
Y: 0.152 m
Z: 0.517 m
ROS2 Concepts Used
ROS2 Nodes
Topics
Subscribers
JointState Message
TF2
Transform Listener
Forward Kinematics
Files Created
hello_node.py

joint_reader.py

joint_monitor.py

fk_monitor.py
Commands Frequently Used
colcon build

source install/setup.bash

ros2 run <package_name> hello_node

ros2 run <package_name> joint_reader

ros2 run <package_name> joint_monitor

ros2 run <package_name> fk_monitor
Outcome
Successfully created ROS2 nodes.
Successfully read Panda robot joint states.
Successfully monitored individual joints.
Successfully obtained end-effector position using TF2.
Learned the basic concept of Forward Kinematics and ROS2 communication.