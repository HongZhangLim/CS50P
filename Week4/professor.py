import random


def main():
    level = get_level()
    point = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        trial = 0
        while trial in range(3):
            ans = int(input(f"{x} + {y} = "))
            if ans == x + y:
                point += 1
                trial = 0
                break
            else:
                print("EEE")
                trial += 1
                if trial == 3 and ans != x + y:
                    print(f"{x} + {y} = {x+y}")
                continue
    print(f"Score: {point}")

# return level int
def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level in (1,2,3):
            return level
        else:
            continue

# return 10 sets of x y
def generate_integer(level):
    if level == 1:
        int_min = 0
    else:
        int_min = 10 ** (level - 1)
    int_max = (10 ** level) - 1
    return random.randint(int_min, int_max)

if __name__ == "__main__":
    main()
