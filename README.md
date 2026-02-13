# My Hello Ros

Kleines **ROS 2 (rclpy)**-Beispielpaket als Einstieg für den Blockkurs **„Einführung in die mobile Robotik“** an der Technischen Hochschule Nürnberg Georg Simon Ohm.  
Das Repo zeigt die wichtigsten ROS2-Grundideen anhand eines minimalen **Publisher/Subscriber**-Beispiels:

- Node **Publisher** sendet periodisch eine Textnachricht auf ein Topic
- Node **Subscriber** empfängt die Nachricht und loggt sie

> Ziel: In wenigen Minuten ein ROS2-Workspace aufsetzen, ein Paket bauen und die Kommunikation über Topics nachvollziehen.

---

## Inhalte

Dieses Paket enthält zwei ROS2-Nodes:

- `my_hello_ros_publisher`  
  Publiziert `std_msgs/msg/String` auf `hello_ros_topic` (default: alle 0.5 s, Inhalt: `"Hello ROS2"`)

- `my_hello_ros_subscriber`  
  Abonniert `hello_ros_topic` und gibt empfangene Nachrichten aus

---

## Voraussetzungen

- Ubuntu (empfohlen für den Kurs) + installierte ROS 2 Distribution (z. B. Humble)
- `colcon` Build-Tools
- Terminal-Grundlagen (source, workspace, etc.)


---

## Quickstart

### 1) ROS 2 Umgebung laden

In **jedem** neuen Terminal (oder in deiner `.bashrc`):

```bash
source /opt/ros/$ROS_DISTRO/setup.bash
```



---

## Publisher starten
```
ros2 run my_hello_ros my_hello_ros_publisher
```

---

## Subscriber starten
```
ros2 run my_hello_ros my_hello_ros_subscriber
```
