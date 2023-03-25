import RPi.GPIO as GPIO
import time
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class car:
    def __init__(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)  # GPIO初始設定
        self.MOTOR_R_PWM_PIN = 12  # 右馬達轉速PIN
        self.MOTOR_L_PWM_PIN = 13  # 左馬達轉速PIN
        self.MOTOR_R_EN_PIN = 22  # 右馬達啟動PIN(LOW為啟動,HIGH為關閉)
        self.MOTOR_L_EN_PIN = 23  # 左馬達啟動PIN(LOW為啟動,HIGH為關閉)
        self.MOTOR_R_DIR_PIN = 5  # 右馬達轉向PIN
        self.MOTOR_L_DIR_PIN = 6  # 左馬達轉向PIN
        GPIO.setup(self.MOTOR_R_PWM_PIN, GPIO.OUT)
        GPIO.setup(self.MOTOR_L_PWM_PIN, GPIO.OUT)
        self.MOTOR_R = GPIO.PWM(self.MOTOR_R_PWM_PIN, 1000)  # 宣告GPIO右馬達PWM控制
        self.MOTOR_L = GPIO.PWM(self.MOTOR_L_PWM_PIN, 1000)  # 宣告GPIO左馬達PWM控制
        GPIO.setup(self.MOTOR_R_EN_PIN, GPIO.OUT)  # 宣告GPIO右馬達EN控制
        GPIO.setup(self.MOTOR_L_EN_PIN, GPIO.OUT)  # 宣告GPIO左馬達EN控制
        GPIO.setup(self.MOTOR_R_DIR_PIN, GPIO.OUT)  # 宣告GPIO右馬達DIR控制
        GPIO.setup(self.MOTOR_L_DIR_PIN, GPIO.OUT)  # 宣告GPIO左馬達DIR控制

    def stop(self):  # 馬達停止
        GPIO.output(self.MOTOR_R_EN_PIN, GPIO.HIGH)
        GPIO.output(self.MOTOR_L_EN_PIN, GPIO.HIGH)
        self.MOTOR_L.stop()
        self.MOTOR_R.stop()

    def start(self):  # 馬達啟動
        GPIO.output(self.MOTOR_R_EN_PIN, GPIO.LOW)
        GPIO.output(self.MOTOR_L_EN_PIN, GPIO.LOW)
        self.MOTOR_L.start(0)
        self.MOTOR_R.start(0)

    def move(self, speed=25, st=0):

        if st == 0:
            GPIO.output(self.MOTOR_R_DIR_PIN, GPIO.LOW)
            GPIO.output(self.MOTOR_L_DIR_PIN, GPIO.HIGH)
        elif st == 1:
            GPIO.output(self.MOTOR_R_DIR_PIN, GPIO.HIGH)
            GPIO.output(self.MOTOR_L_DIR_PIN, GPIO.LOW)

        self.start()
        self.MOTOR_L.ChangeDutyCycle(speed)
        self.MOTOR_R.ChangeDutyCycle(speed)

    def move_RL(self, speed=25, st=0):

        GPIO.output(self.MOTOR_R_DIR_PIN, GPIO.LOW)
        GPIO.output(self.MOTOR_L_DIR_PIN, GPIO.LOW)

        match st:
            case 0:
                L_SPEED = int(speed)
                R_SPEED = int(speed / 1.5)
            case 1:
                L_SPEED = int(speed / 1.5)
                R_SPEED = int(speed)

        self.start()
        self.MOTOR_L.ChangeDutyCycle(L_SPEED)
        self.MOTOR_R.ChangeDutyCycle(R_SPEED)

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('drive_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic_car_move',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.main_car = car()

    def listener_callback(self, msg):
        self.get_logger().info(f'car_move_stage:{msg.data}')
        move_st = str(msg.data)
        move_st = move_st.split("_")
        if move_st[1] == 'L':
            self.main_car.start()
            self.main_car.move_RL(st=1)
        elif move_st[1] == 'R':
            self.main_car.start()
            self.main_car.move_RL(st=0)
        elif move_st[1] == 'N':
            if move_st[2] == 'move':
                self.main_car.start()
                self.main_car.move(st=0)
            elif move_st[2] == 'stop':
                self.main_car.stop()

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()