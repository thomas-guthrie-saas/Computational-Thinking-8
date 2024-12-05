###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("summer")
mySprite = codesters.Sprite("cardinal")
mySprite.say("yo")


print("\n\nWhen you have found the CARDINAL, click here, then use CTRL C to end the program\n\n")
print("This is the new last instruction")
mySprite2 = codesters.Sprite("waterbottle",50,0)