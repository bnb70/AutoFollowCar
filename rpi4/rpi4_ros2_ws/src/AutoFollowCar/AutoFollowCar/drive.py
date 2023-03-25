import RPi.GPIO as GPIO
import time

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

    def move(self, speed=10, st=0):
        self.stop()

        if st == 0:
            GPIO.output(self.MOTOR_R_DIR_PIN, GPIO.LOW)
            GPIO.output(self.MOTOR_L_DIR_PIN, GPIO.LOW)
        elif st == 1:
            GPIO.output(self.MOTOR_R_DIR_PIN, GPIO.HIGH)
            GPIO.output(self.MOTOR_L_DIR_PIN, GPIO.HIGH)

        self.start()
        self.MOTOR_L.ChangeDutyCycle(speed)
        self.MOTOR_R.ChangeDutyCycle(speed)

    def move_RL(self, speed=10, st=0):
        self.stop()
        GPIO.output(self.MOTOR_R_DIR_PIN, GPIO.LOW)
        GPIO.output(self.MOTOR_L_DIR_PIN, GPIO.LOW)

        match st:
            case 0:
                L_SPEED = int(speed)
                R_SPEED = int(speed / 2)
            case 1:
                L_SPEED = int(speed / 2)
                R_SPEED = int(speed)

        self.start()
        self.MOTOR_L.ChangeDutyCycle(L_SPEED)
        self.MOTOR_R.ChangeDutyCycle(R_SPEED)

if __name__ == '__main__':
    car_a = car()
    car_a.move()