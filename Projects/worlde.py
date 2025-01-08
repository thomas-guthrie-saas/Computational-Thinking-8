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

# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    print("Make a guess:")
    guess_word = input()
    output = ""

    print(guess_word)
    print(len.guess_word)


    if guess_word == hidden_word:
        os.system('clear')
        print("You win")
        wait.sleep(3)
        break
    
    
    for x in range(5):
        if guess_word[x] == hidden_word[x]:
            output += "🟩"
        elif guess_word[x] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"
    

    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        os.system('clear')
        print("You win")
        wait.sleep(3)
        break

os.system('clear')
if i > 1:
    print(f"You used {i+1} guesses.")
elif 1 > i:
    print(f"You used {i+1} guess.")
else:
    print("oops")
wait.sleep(3)
exit(2)