import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyHelloRosSubscriber(Node):

    def __init__(self):
        super().__init__('my_hello_ros_subscriber')
        self.subscription = self.create_subscription(
            String,
            'hello_ros_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    my_hello_ros_subscriber = MyHelloRosSubscriber()
    rclpy.spin(my_hello_ros_subscriber)
    my_hello_ros_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()