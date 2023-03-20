import random
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class coordinate_to_car():

    def __init__(self):
        self.i = 0
        self.coordinate = []
        self.center_point = []
        self.move = ''

    def run(self, data):
        self.str_split(data)
        self.get_center()
        return self.move_state()

    def random_xxyy(self):
        x1 = random.randint(0, 640 - 10)
        y1 = random.randint(10, 640)
        x2 = random.randint(x1 + 10, 640)
        y2 = random.randint(0, y1 - 10)
        xxyy = [x1, y1, x2, y2]
        return xxyy

    def str_split(self, data=""):
        data = data.split(":")
        data = [data[0]] + data[1].split(",")
        self.coordinate = data

    def get_center(self):
        center_x = abs(((self.coordinate[1] - self.coordinate[3]) / 2) + self.coordinate[1])
        center_y = abs(((self.coordinate[2] - self.coordinate[4]) / 2) + self.coordinate[4])
        self.center_point = [center_x, center_y]

    def move_state(self):
        if self.center_point[0] < 310:
            move_R_L = 'L'
        elif self.center_point[0] > 525:
            move_R_L = 'R'
        else:
            move_R_L = 'N'
        if self.center_point[1] > 235:
            move_or_stop = 'move'
        else:
            move_or_stop = 'stop'
        self.move = f'{move_or_stop}_{move_R_L}'
        return self.move

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('operation')
        self.subscription = self.create_subscription(String, 'topic_jetson_info', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(String, 'topic_car_move', 10)
        timer_period = 0.2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.car_move = coordinate_to_car()

    def timer_callback(self):
        car_move_ = self.car_move.run()
        car_move_mag = String()
        car_move_mag.data = f'{car_move_}'
        self.publisher_.publish(car_move_mag)
        self.get_logger().info(f'Send_car_move_data:{car_move_}')
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