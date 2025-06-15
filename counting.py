from const import RES


class Counting:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0
        self.index = 0
        self.score = 0

    def count_rufie(self):
        return(4*(self.p1+self.p2+self.p3)-200)/10

    def worst_level(self):
        norm_age = (min(15, self.age)-7)//2
        level = 21-norm_age*1.5
        return level

    def total_score(self):
        self.index = self.count_rufie()
        level = self.worst_level()
        decrs = [0, 4, 5, 5.5, 0]
        self.score = 0
        for decr in decrs:
            level -= decr
            if self.index >= level:
                return self.score
            self.score += 1
        self.score -= 1
        return self.score

    def __str__(self):
        name = f'{self.name},\n'
        index = f'your rufie index: {self.index}\n'
        tip = f'your heart work level:{RES[self.score]}'

        return name+index+tip
