import random

def flip_coin():
    result = random.random()
    if result < 0.66:
        return 'Heads'
    else:
        return 'Tails'

print(flip_coin())