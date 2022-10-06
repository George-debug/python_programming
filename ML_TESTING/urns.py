import random

# exec(open("statistics.py").read()) to run this file

def decision(probability):
    return random.random() < probability

class Urn:
    def __init__(self, white, red):
        self.white = white
        self.red = red

    def get_ball(self):
        return decision(self.white / (self.white + self.red))

u1 = Urn(11, 4)
u2 = Urn(8, 5)
was_first = 0
total = 0

for _ in range (100000):
    is_first = decision(0.5)
    is_white = 0

    if(is_first):
        is_white = u1.get_ball()
    else:
        is_white = u2.get_ball()

    if(is_white):
        total += 1

        if(is_first):
            was_first += 1


print(was_first / total)
