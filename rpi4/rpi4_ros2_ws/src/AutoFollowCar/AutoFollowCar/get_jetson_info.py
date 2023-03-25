import rclpy
import socket
from rclpy.node import Node

from std_msgs.msg import String


class rpi4_eth():

    def __init__(self):
        self.rpi4_ip = '192.168.55.100'
        self.ip_port = 8888
        self.rpi4_eth = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.rpi4_eth.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.rpi4_eth.bind((self.rpi4_ip, self.ip_port))
        self.rpi4_eth.listen(5)

    def run(self):
        while True:
            conn, addr = self.rpi4_eth.accept()
            indata = conn.recv(1024)
            if len(indata) == 0:
                conn.close()
            else:
                indata = (indata.decode())
                break

        return indata

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('jetson_info_publisher')
        self.publisher_ = self.create_publisher(String, 'topic_jetson_info', 10)
        timer_period = 0.2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.data = rpi4_eth()

    def timer_callback(self):
        jetson_msg = String()
        jetson_msg.data = 'NO.00:0,800,800,0,0'
        jetson_msg.data = f'{self.data.run()}'
        self.publisher_.publish(jetson_msg)
        self.get_logger().info(f'Send_to_operation:{jetson_msg.data}')
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()