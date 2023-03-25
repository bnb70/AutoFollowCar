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
        data = str(data)
        data = data.split(":")
        data = [data[0]] + data[1].split(",")
        self.coordinate = data

    def get_center(self):
        x1 = int(self.coordinate[1])
        y1 = int(self.coordinate[2])
        x2 = int(self.coordinate[3])
        y2 = int(self.coordinate[4])
        center_x = (abs(x1-x2)/2) + x1
        center_y = (abs(y1-y2)/2) + y2
        self.center_point = [center_x, center_y]

    def move_state(self):

        if self.center_point[0] < 310:
            move_R_L = 'L'
        elif self.center_point[0] > 525:
            move_R_L = 'R'
        else:
            move_R_L = 'N'
        if self.center_point[1] < 235 and self.center_point[1] != 0:
            move_or_stop = 'move'
        else:
            move_or_stop = 'stop'
        self.move = f'0_{move_or_stop}_{move_R_L}_0'

        return self.move

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('operation')
        self.subscription = self.create_subscription(String, 'topic_jetson_info', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(String, 'topic_car_move', 10)
        timer_period = 0.6  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.car_move_ = '0_stop_N_0'
        self.car_move = coordinate_to_car()

    def timer_callback(self):
        car_move_mag = String()
        car_move_mag.data = f'{self.car_move_}'
        self.publisher_.publish(car_move_mag)
        self.get_logger().info(f'Send_car_move_data:{self.car_move_}')
        self.car_move_ = '0_stop_N_0'
        self.i += 1

    def listener_callback(self, jetson_msg):
        self.get_logger().info(f'To_Operation_data:{jetson_msg.data}')
        self.car_move_ = self.car_move.run(jetson_msg)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()