import time as wait

# beginning
laflame_points = 0
lama_points = 0

# middle
answer = input("which song do you like more? A) sicko mode B) DNA\n")
if answer == "A":
    laflame_points += 1
    print("STRAIGHT UP\n")
elif answer == "B":
    lama_points += 1
    print("oh yea drake is done for\n")

answer = input("is travis or kendrick better\n")
if answer == "A":
    laflame_points += 1
    print("la flame\n")
elif answer == "B":
    lama_points += 1
    print("lamar\n")

answer = input("who has more aura\n")
if answer == "A":
    laflame_points += 1
    print("priceless\n")
elif answer == "B":
    lama_points += 1
    print("why is jasper on the swing set\n")

answer = input("who has a better voice\n")
if answer == "A":
    laflame_points += 1
    print("voice crack\n")
elif answer == "B":
    lama_points += 1
    print("the art of peer pressure\n")

answer = input("who has the better music videos\n")
if answer == "A":
    laflame_points += 1
    print("sick modoe\n")
elif answer == "B":
    lama_points += 1
    print("family ties is fire\n")

# end
if laflame_points > lama_points:
    print("you like travvy patty more")
elif lama_points > laflame_points:
    print("you like pookie kendrick more")
elif laflame_points == lama_points:
    ("you are a purist and like them the same amount")