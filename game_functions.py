import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if user_input == 'h':
        return next_val > current_val
    elif user_input == 'l':
        return next_val < current_val
    else:
        return True


# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    found = False

    for i in range(len(word)):
        if word[i] == letter:
            board[i] = letter
            found = True
    
    if found:
        print("Nice Work! {letter} is a part of the word")
    else:
        print("Woops {letter is not part of the word")
        return False
