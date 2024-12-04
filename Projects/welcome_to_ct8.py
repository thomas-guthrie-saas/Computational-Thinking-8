###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("drawbridge")
mySprite = codesters.Sprite("cool_dog")
mySprite.say("Bow wow young blud")
mySprite2 = codesters.Sprite("fox",150,-50)
mySprite2.say("What does the fox say?")