import random

def randomflip(flip = 0):
    if flip is int(0):
        print("Tails!")
    else:
        print("Heads!")

def main():
    flip = random.randint(0,1)
    randomflip(flip)

if __name__ == "__main__":
    main()

