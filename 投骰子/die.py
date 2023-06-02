from random import randint

class Die:

    #表示一个骰子类

    def __init__(self, num_sides=6):
    #骰子默认6面
        self.num_sides = num_sides

    def roll(self):
    #表示投骰子的过程返回一个1-骰子面数中的数字
        return randint(1, self.num_sides)