import random


class coordinate_to_car():

    def __init__(self):
        self.i = 0
        self.coordinate = []
        self.center_point = []
        self.move = ''

    def run(self,data):
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

    def str_split(self,data=""):
        data = data.split(":")
        data = [data[0]] + data[1].split(",")
        self.coordinate = data

    def get_center(self):
        center_x = abs(((self.coordinate[1] - self.coordinate[3]) / 2) + self.coordinate[1])
        center_y = abs(((self.coordinate[2] - self.coordinate[4]) / 2) + self.coordinate[4])
        self.center_point = [center_x,center_y]

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