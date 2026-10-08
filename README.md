# My Hello ROS

A small **ROS 2 Python (`rclpy`) example** for students who are new to ROS. This package is designed as a first hands-on exercise for the *Introduction to Mobile Robotics* course at Nuremberg Institute of Technology (Technische Hochschule Nürnberg Georg Simon Ohm).

You will build and run two ROS 2 nodes that communicate using a topic:

- The **publisher** sends the text `Hello ROS2` every 0.5 seconds.
- The **subscriber** listens for that text and prints each message it receives.

By the end, you will have built a ROS 2 workspace, run both nodes, and inspected their topic communication from the command line.

## What you need

- Ubuntu with a ROS 2 distribution installed (for example, ROS 2 Humble)
- The `colcon` build tool
- A terminal, and Git to clone this repository

The commands below use Bash and assume ROS 2 Humble is installed. If you use another distribution, replace `humble` in the commands with its name.

## Quick start

### 1. Set up a workspace

Open a terminal and create a workspace. A ROS 2 workspace is a directory where you keep and build packages; its `src` directory contains the package source code.

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/christianpfitzner/my_hello_ros.git
```

### 2. Build the package

Move to the workspace root, load your ROS 2 installation, and build:

```bash
cd ~/ros2_ws
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash
```

`source` makes ROS 2 commands and packages available in the current terminal. Run both setup commands in every new terminal.

### 3. Start the publisher

In the first terminal, run:

```bash
cd ~/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run my_hello_ros my_hello_ros_publisher
```

The publisher should repeatedly print:

```text
Publishing: "Hello ROS2"
```

Keep this terminal running.

### 4. Start the subscriber

Open a second terminal and run:

```bash
cd ~/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run my_hello_ros my_hello_ros_subscriber
```

The subscriber should print messages like:

```text
I heard: "Hello ROS2"
```

Both nodes must be running at the same time for the subscriber to receive the publisher's messages. Press **Ctrl+C** in a node's terminal to stop it.

## What is happening?

A **node** is a running ROS 2 program. The publisher node sends `std_msgs/msg/String` messages on the `hello_ros_topic` topic, and the subscriber node listens to that same topic. A **topic** is a named channel that lets ROS 2 nodes exchange messages without needing to call each other directly.

## Explore with ROS 2 commands

With both nodes running, try these commands in another terminal. Remember to source the ROS 2 and workspace setup files first.

List active topics:

```bash
ros2 topic list
```

Print messages from the topic:

```bash
ros2 topic echo /hello_ros_topic
```

List running nodes and inspect the publisher:

```bash
ros2 node list
ros2 node info /my_hello_ros_publisher
```

## Troubleshooting

- **`/opt/ros/humble/setup.bash` not found:** Check which ROS 2 distribution is installed and replace `humble` with its name.
- **`Package 'my_hello_ros' not found`:** From `~/ros2_ws`, rebuild with `colcon build`, then run `source install/setup.bash` in the terminal where you launch the node.
- **No messages appear in the subscriber:** Make sure the publisher is still running and both terminals have sourced the same ROS 2 installation and workspace.
