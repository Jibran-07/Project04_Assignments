import random

def game():
    computer_choice = random.choice(['r','p','s'])
    user_choice = input(" Enter 'r' for rock, 's' for scissors and 'p' for paper: ")
    if computer_choice == user_choice:
        return "It's a draw"
    if is_win(user_choice,computer_choice):
        return "You Win!"
    return "You Lose!"

def is_win(user,computer):
    if user == 'r' and computer == 's' or user == 's' and computer == 'p' or user == 'p' and computer == 'r':
        return True

print(game())