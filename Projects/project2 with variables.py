import time as wait
import os

# beginning
laflame_points = 0
lama_points = 0

q1 = "Which song do you like more?\nA) Sicko mode\nB) DNA\n"
q2 = "Which one do you like more?\nA) Travis Scott\nB) Kendrick Lamar\n"
q3 = "Who has more aura?\nA) Travis Scott\nB) Kendrick Lamar\n"
q4 = "Who has a better voice?\nA) Travis Scott\nB) Kendrick Lamar\n"
q5 = "Who has the better music videos\nA) Travis Scott\nB) Kendrick Lamar\n"

# middle
while True:
    os.system('clear')
    answer = input(q1)
    if answer == "A" or answer == "a":
        laflame_points += 1
        os.system('clear')
        print("STRAIGHT UP")
        wait.sleep(1)
        break
    elif answer == "B" or answer == "b":
        lama_points += 1
        os.system('clear')
        print("Oh yea drake is done for")
        wait.sleep(1)
        break
    else:
        os.system('clear')
        print("Try again")
        wait.sleep(1)
while True:
    os.system('clear')
    answer = input(q2)
    if answer == "A" or answer == "a":
        laflame_points += 1
        os.system('clear')
        print("La Flame!!1!!1!")
        wait.sleep(1)
        break
    elif answer == "B" or answer == "b":
        lama_points += 1
        os.system('clear')
        print("Lama!11!")
        wait.sleep(1)
        break
    else:
        os.system('clear')
        print("Try again")
        wait.sleep(1)

while True:
    os.system('clear')
    answer = input(q3)
    if answer == "A" or answer == "a":
        laflame_points += 1
        os.system('clear')
        print("Priceless")
        wait.sleep(1)
        break
    elif answer == "B" or answer == "b":
        lama_points += 1
        os.system('clear')
        print("Why is jasper on the swing set")
        wait.sleep(1)
        break
    else:
        os.system('clear')
        print("Try again")
        wait.sleep(1)

while True:
    os.system('clear')
    answer = input(q4)
    if answer == "A" or answer == "a":
        laflame_points += 1
        os.system('clear')
        print("Eeyehh")
        wait.sleep(1)
        break
    elif answer == "B" or "b":
        lama_points += 1
        os.system('clear')
        print("U")
        wait.sleep(1)
        break
    else:
        os.system('clear')
        print("Try again")
        wait.sleep(1)

while True:
    os.system('clear')
    answer = input(q5)
    if answer == "A" or "a":
        laflame_points += 1
        os.system('clear')
        print("Sicking Mode")
        wait.sleep(1)
        break
    elif answer == "B" or "b":
        lama_points += 1
        os.system('clear')
        print("Family ties")
        wait.sleep(1)
        break
    else:
        os.system('clear')
        print("Try again")
        wait.sleep(1)

# end
os.system('clear')
wait.sleep(.5)
print("Drumroll Please...")
wait.sleep(2.5)
if laflame_points > lama_points:
    print("You like travvy patty more!")
elif lama_points > laflame_points:
    print("You like kendrick wendrick more!")
elif laflame_points == lama_points:
    ("You are a purist and like them the same amount.")
wait.sleep(4)
os.system('clear')
print("Thanks for playing.")
wait.sleep(4)
os.system('clear')
exit(2)