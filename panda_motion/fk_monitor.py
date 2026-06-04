import rclpy
from rclpy.node import Node

from tf2_ros import Buffer
from tf2_ros import TransformListener


class FKMonitor(Node):

    def __init__(self):

        super().__init__('fk_monitor')

        self.tf_buffer = Buffer()

        self.tf_listener = TransformListener(
            self.tf_buffer,
            self
        )

        self.timer = self.create_timer(
            2.0,
            self.print_pose
        )

    def print_pose(self):

        try:

            transform = self.tf_buffer.lookup_transform(
                'panda_link0',
                'panda_hand',
                rclpy.time.Time()
            )

            t = transform.transform.translation

            print("\n===== End Effector Pose =====")

            print(
                f"X: {t.x:.3f} m"
            )

            print(
                f"Y: {t.y:.3f} m"
            )

            print(
                f"Z: {t.z:.3f} m"
            )

        except Exception:
            pass


def main(args=None):

    rclpy.init(args=args)

    node = FKMonitor()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()