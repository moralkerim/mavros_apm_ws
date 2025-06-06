import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class OdometryRelay(Node):
    def __init__(self):
        super().__init__('odometry_relay')

        # Publisher
        self.publisher_ = self.create_publisher(Odometry, '/mavros/odometry/out', 10)

        # Subscriber
        self.subscription = self.create_subscription(
            Odometry,
            '/odometry',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        # Frame ID'leri değiştir
        msg.header.frame_id = "map"
        msg.child_frame_id = "base_link"

        # Yayınla
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = OdometryRelay()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

