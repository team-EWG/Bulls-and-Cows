def getDigits(num):
    return [int(i) for i in str(num)]

def numOfBullsCows(num, guess):
    bull_cow = [0, 0]
    num_list = getDigits(num)
    guess_list = getDigits(guess)

    for i, j in zip(num_list, guess_list):
        if j in num_list:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1

    return bull_cow