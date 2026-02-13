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

### 2) Workspace erstellen und Paket bauen

Erstelle einen ROS 2 Workspace und baue das Paket:

```bash
# Workspace-Verzeichnis erstellen
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

# Dieses Repository klonen
git clone https://github.com/christianpfitzner/my_hello_ros.git

# Zurück zum Workspace-Root
cd ~/ros2_ws

# Paket bauen
colcon build

# Workspace-Setup laden
source install/setup.bash
```

### 3) Publisher starten

Öffne ein **erstes Terminal** und starte den Publisher:

```bash
source /opt/ros/$ROS_DISTRO/setup.bash
cd ~/ros2_ws
source install/setup.bash
ros2 run my_hello_ros my_hello_ros_publisher
```

Du solltest sehen: `Publishing: "Hello ROS2"` (alle 0.5 Sekunden)

### 4) Subscriber starten

Öffne ein **zweites Terminal** und starte den Subscriber:

```bash
source /opt/ros/$ROS_DISTRO/setup.bash
cd ~/ros2_ws
source install/setup.bash
ros2 run my_hello_ros my_hello_ros_subscriber
```

Du solltest sehen: `I heard: "Hello ROS2"`

---

## Weitere nützliche Befehle

### Topics anzeigen
```bash
ros2 topic list
```

### Topic-Daten live ansehen
```bash
ros2 topic echo /hello_ros_topic
```

### Node-Informationen anzeigen
```bash
ros2 node list
ros2 node info /my_hello_ros_publisher
```
