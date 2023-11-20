import random


def three_d_6():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)
    return d1 + d2 + d3

def generate_array():
    stats = []
    for i in range(6):
        stats.append(three_d_6())
    return stats

def generate_arrays(n):
    for i in range(n):
        stats = generate_array()
        print("{}".format(stats))

generate_arrays(100)