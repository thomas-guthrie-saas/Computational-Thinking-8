###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("fall")
mySprite = codesters.Sprite("cardinal")
mySprite.say("Good job finding me!")


print("\n\nWhen you have found the CARDINAL, click here, then use CTRL C to end the program\n\n")
print ("This is the new last instruction")
mySprite2 = codesters.Sprite("baseball",-180,180)
mySprite2 = codesters.Sprite("kitten",-160,-180)