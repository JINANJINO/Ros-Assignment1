import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Twist, Vector3

class HelloturtlePub(Node):

    def __init__(self):
        super().__init__('helloturtle_pub') # node name: helloturtle_pub
        qos_profile = QoSProfile(depth = 10)
        self.helloturtle_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', qos_profile) # message name: /turtle1/cmd_vel
        self.timer = self.create_timer(1, self.publish_turtle_pub) 
        self.count = 0

    def publish_turtle_pub(self):
        msg = Twist()
        msg.linear = Vector3(x = 2.0, y = 0.0, z = 0.0)
        msg.angular = Vector3(x = 0.0, y = 0.0, z = 0.0)
        self.helloturtle_pub.publish(msg)
        self.get_logger().info('Linear : {0}, Angular : {1}'.format(msg.linear, msg.angular))
        self.count += 1

def main(args=None):
    rclpy.init(args=args) # Node initialize
    node = HelloturtlePub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__=='__main__':
    main()