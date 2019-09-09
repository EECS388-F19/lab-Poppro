import random


def main():
    print("Hunter")
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    print(x)
    print(y)
    print("Sum = " + str((x+y)))
    print("Average = " + str(((x+y)/2.0)))


if __name__ == "__main__":
    main()
