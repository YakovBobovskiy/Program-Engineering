import random

def dice():
    roll = random.randint(1, 6)
    print(f"Выпало число: {roll}")
    if roll in [5, 6]:
        print("Вы победили!")
    elif roll in [3, 4]:
        dice()
    else:
        print("Вы проиграли!")

if __name__ == "__main__":
    dice()