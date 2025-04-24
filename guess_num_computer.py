import random

def guess_num_comp(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"""Enter a number between 1 and {x}: """))
        if guess > random_num:
            print("Oops! too high.")
        elif guess < random_num:
            print("Oops! too low.")
        else:
            print("Congrats! you guessed correctly")


guess_num_comp(10)