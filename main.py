import numpy as np


def main():
    problem002()


def problem002():
    pass


def problem001():
    total = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    print(total)


if __name__ == '__main__':
    main()
