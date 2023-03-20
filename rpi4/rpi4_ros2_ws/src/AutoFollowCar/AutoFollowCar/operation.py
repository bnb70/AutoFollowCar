import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('operation')
        self.publisher_ = self.create_publisher(String, 'topic_car_move', 10)
        self.subscription = self.create_subscription(String,'topic_jetson_info',self.listener_callback,10)
        timer_period = 0.2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Send_car_move_data:{self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Send_car_move_data:{self.i}')
        self.i += 1

    def listener_callback(self, jetson_msg):
        self.get_logger().info(f'To_Operation_data:{jetson_msg.data}')


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()