import random
import os
import time as wait

# Pick a word at random
os.system('clear')
print("Welcome to wordle!")
wait.sleep(1)
os.system('clear')
wait.sleep(.3)
word_list = ["loopy","heart","audio","laugh","trial"]
hidden_word = random.choice(word_list)
print(hidden_word)

# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    

    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

print(f"You used {i+1} guesses")
