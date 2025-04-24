import random

def guess_num_user(x):
    low = 1
    high = x
    guess = ''
    while guess != 'r':
        if low != high:
            random_num = random.randint(low, high)
        else:
            random_num = high
        guess = input(f""" Is {random_num} high(h), low(l) or right(r)? """).lower()
        if guess == 'h':
            high = random_num -1
        elif guess == 'l':
            low = random_num + 1
        else:
            print("Congrats! computer guessed correctly")


guess_num_user(10)