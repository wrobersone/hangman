# from words import words
# import string

# def get_valid_word(words):
#     word = random.choice(words)
#     while '-' in word or ' ' in word:
#         word = random.choice(words)

#     return word.upper()

# def hangman():
#     word = get_valid_word(words)
#     word_letters = set(word) # letters in the word
#     alphabet = set(string.ascii_uppercase)
#     used_letters = set() # letters the user has guessed

#     lives = 7

#     # get user input
#     while len(word_letters) > 0 and lives > 0:
#         # letters used
#         print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

#         # current word is (ie W - R D)
#         word_list = [letter if letter in used_letters else '-' for letter in word]
#         print('Current word: ', ' '.join(word_list))

#         user_letter = input('Guess a letter: ').upper()
#         if user_letter in alphabet - used_letters:
#             used_letters.add(user_letter)
#             if user_letter in word_letters:
#                 word_letters.remove(user_letter)
#                 print('')

#             else: 
#                 lives = lives - 1
#                 print('This letter is not in the word.')
#         elif user_letter in used_letters:
#             print('You have already used this letter. Guess again.')

#         else:
#             print('Invalid character.')

#     # gets here when len(word_letters) == 0 or when lives == 0
#     if lives == 0:
#         print('Game over, you lose. The word was', word)
#     else:
#         print('Congrats! You guessed the word', word, '!!')

# hangman()
import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guess this letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ".")

def display_hangman(tries):
    stages = [  """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / \\
                    -
                """,
                """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / 
                    -
                """, 
                """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     
                    -
                """, 
                """
                    --------
                    |      |
                    |      O
                    |     \\|
                    |      |
                    |     
                    -
                """,
                """
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |     
                    -
                """,
                """
                    --------
                    |      |
                    |      O
                    |     
                    |      
                    |     
                    -
                """,
                """
                    --------
                    |      |
                    |      
                    |     
                    |      
                    |     
                    -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Would you like to play again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()