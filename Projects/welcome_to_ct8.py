###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("fall")
mySprite = codesters.Sprite("cardinal")
mySprite.say("Good job finding me!")


print("this is the new last instruction")
mySprite2 = codesters.Sprite("baseball",-200,200)