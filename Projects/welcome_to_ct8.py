###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("fall")
mySprite = codesters.Sprite("cardinal")
mySprite.say("Good job finding me!")

mySprite3 = codesters.Sprite("cat",125,-50)
mySprite3.say("Meow")
mySprite3.set_size(0.25)

MySprite4 = codesters.Sprite("kitten",-125,-100)
MySprite4.say("i will eat u when ur dead")
MySprite4.say_size(0.5)


print("\n\nWhen you have found the CARDINAL, click here, then use CTRL C to end the program\n\n")
print("This is the new last instruction")
mySprite2 = codesters.Sprite("baseball",-250,250)