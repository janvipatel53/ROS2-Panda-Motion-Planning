import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState


class JointReader(Node):

    def __init__(self):
        super().__init__('joint_reader')

        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_callback,
            10
        )

        self.get_logger().info("Waiting for joint states...")

    def joint_callback(self, msg):
        print("\n========================")
        print("Joint Names:")
        print(msg.name)

        print("\nJoint Positions:")
        print(msg.position)


def main(args=None):
    rclpy.init(args=args)

    node = JointReader()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()