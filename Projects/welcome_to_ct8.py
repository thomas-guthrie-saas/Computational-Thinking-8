###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("fall")
mySprite = codesters.Sprite("cardinal")
mySprite.say("Good job finding me!")



print("This is the new last instruction")
mySprite2 = codesters.Sprite("baseball" , -160 , 160)
mySprite2 = codesters.Sprite("soccerball",0,0)