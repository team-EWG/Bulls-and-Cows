import random

def createTargetNum():
    number = []
    while len(number) < 4:
        randomInt = random.randint(1, 9) if len(number) == 0 else random.randint(0, 9)
        if randomInt not in number:
            number.append(randomInt)
    target = 0
    for i in range(4):
        target += (number[3-i] * 10 ** i)
    return target