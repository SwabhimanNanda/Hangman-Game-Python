# Import necessary modules
import random
from hangman_words import word_list
from hangman_art import logo, stages

# Display the game logo
print(logo)

# Choose a random word from the word list
chosen_word = random.choice(word_list)
print(chosen_word)

# Get the length of the chosen word
word_length = len(chosen_word)

# Set the initial number of lives
lives = 6

# Initialize a list to store the current state of the word being guessed
display = ["_" for _ in range(word_length)]

# Variable to track the end of the game
end_of_game = False

# Main game loop
while not end_of_game:    
    # Get a letter guess from the player
    guess = input("Guess the letter: ").lower()

    # Check if the letter has already been guessed
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check if the guessed letter is in the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    # If the guessed letter is not in the chosen word, reduce lives
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        # If no lives are remaining, end the game
        if lives == 0:
            end_of_game = True
            print("You lose!")
    print(f"{' '.join(display)}")

    # Check if the word has been completely guessed
    if "_" not in display:
        end_of_game = True
        print("You Win!")

    # Display the current hangman stage
    print(stages[lives])
