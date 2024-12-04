###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("spring")
mySprite = codesters.Sprite("cardinal")
mySprite.say(" great job you did it!")




print("\n\nWhen you have found the CARDINAL, click here, then use CTRL C to end the program\n\n")
mySprite2= codesters.Sprite("baseball",-200,200)