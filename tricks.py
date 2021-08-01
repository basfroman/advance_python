
from random import random


if __name__ == '__main__':
    #  fast sorted list
    lst = [i for i in range(100) if random() > 0.7]
    print(lst)

    # or generator
    gen = (i for i in range(100) if random() > 0.7)
    print(gen.send(None))
