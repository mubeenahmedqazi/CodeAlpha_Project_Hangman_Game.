import random
import hangman_stages


word_list = [
    "APPLE", "MANGO", "BANANA", "GRAPES", "WATERMELON", "ORANGE", "PINEAPPLE", "STRAWBERRY", "BLUEBERRY", "RASPBERRY",
    "BLACKBERRY", "POMEGRANATE", "KIWI", "PEACH", "PLUM", "CHERRY", "APRICOT", "FIG", "PAPAYA", "GUAVA",
    "LYCHEE", "COCONUT", "MELON", "TANGERINE", "PASSIONFRUIT"
]

lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)
display = ['_' for _ in chosen_word]
print(display)
game_over = False

while not game_over:
    guessed_letter = input("GUESS A LETTER: ").upper()

    if guessed_letter in display:
        print(f"You've already guessed {guessed_letter}")
        continue

    if guessed_letter in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guessed_letter:
                display[position] = guessed_letter
        print(display)
    else:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")
        if lives == 0:
            game_over = True
            print("You lose!")

    if '_' not in display:
        game_over = True
        print("You win!")

    print(hangman_stages.stages[lives])
