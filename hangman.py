import random
from word import words
import string

def get_valid_word(selected_word):
    word = random.choice(selected_word)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()
def display_hangman():
    stages_dict = {
            0: """
                    ___________
                   | /        | 
                   |/        ( )
                   |          |
                   |         / \\
                   |
               """,
            1: """
                    ___________
                   | /        | 
                   |/        ( )
                   |          |
                   |         / 
                   |
                """,
            2: """
                    ___________
                   | /        | 
                   |/        ( )
                   |          |
                   |          
                   |
                """,
            3: """
                    ___________
                   | /        | 
                   |/        ( )
                   |          
                   |          
                   |
                """,
            4: """
                    ___________
                   | /        | 
                   |/        
                   |          
                   |          
                   |
                """,
            5: """
                    ___________
                   | /        
                   |/        
                   |          
                   |          
                   |
                """,
            6: """
                   |
                   |
                   |
                   |
                   |
                """,
            7: "",
        }
    return stages_dict

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7


    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(display_hangman()[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou already guessed the letter')

        else:
            print('\nInvalid character. Please enter a letter')

    if lives == 0:
        print(display_hangman()[lives])
        print('Sorry, you died. The word was', word)
    else:
        print('Congratulations! You guessed the word', word, '!!')

print('Welcome to Hangman!')
hangman()