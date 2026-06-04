import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState


class JointMonitor(Node):

    def __init__(self):
        super().__init__('joint_monitor')

        self.create_subscription(
            JointState,
            '/joint_states',
            self.callback,
            10
        )

    def callback(self, msg):

        joint_data = dict(zip(msg.name, msg.position))

        print("\n===== Panda Arm =====")

        for i in range(1, 8):
            joint_name = f'panda_joint{i}'

            if joint_name in joint_data:
                print(
                    f'{joint_name}: '
                    f'{joint_data[joint_name]:.3f} rad'
                )


def main(args=None):

    rclpy.init(args=args)

    node = JointMonitor()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()