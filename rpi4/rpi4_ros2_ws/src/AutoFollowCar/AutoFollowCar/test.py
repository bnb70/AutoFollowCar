import random
import time


class coordinate_to_car():

    def __init__(self):
        self.coordinate = []
        self.i = 0

    def random_xxyy(self):
        x1 = random.randint(0, 640 - 10)
        y1 = random.randint(10, 640)
        x2 = random.randint(x1 + 10, 640)
        y2 = random.randint(0, y1 - 10)
        xxyy = [x1, y1, x2, y2]
        return xxyy
    def str_split(self,data=""):
        self.i = len(self.coordinate)
        data = data.split(":")
        data = [data[0]] + data[1].split(",")
        self.coordinate += [data]
        if self.i >= 10:
            self.coordinate.pop(0)
        return self.coordinate

    def center(self):
        self.coordinate[]










a = coordinate_to_car()

for i in range(100):
    xxyy = a.random_xxyy()
    data = f'NO.{random.randint(1,10)}:{xxyy[0]},{xxyy[1]},{xxyy[2]},{xxyy[3]}'
    b = a.str_split(data)
    print(b)
    time.sleep(1)