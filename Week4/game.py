import random

while True:
    n = int(input("Level: "))
    if not n <= 0:
        break
ans = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    #nonpositive include 0
    if guess < 1:
        continue
    if guess == ans:
        print("Just right!")
        break
    elif guess < ans:
        print("Too Small!")
    else:
        print("Too large!")


