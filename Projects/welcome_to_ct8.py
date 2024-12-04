###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("summer")
mySprite = codesters.Sprite("fish")
mySprite.say("Yo what's up")
mySprite2 = codesters.Sprite("nothing",0,0)