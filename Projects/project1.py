###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("winter")

q1 = codesters.Triangle(100, 100, 200, 'blue')
q2 = codesters.Square(-100, 100, 200, 'gray')
q3 = codesters.Circle(-100, -100, 200, 'red')
q4 = codesters.Triangle(100, -100, 200, 'green')

s1 = codesters.Sprite("speaker", 100, 100)
s1.set_size(0.3)
s2 = codesters.Sprite("cardinal", -100, -100)
s2.set_size(1)
s3 = codesters.Sprite("chillguy", 100, -100)
s3.set_size(0.175)
s4 = codesters.Sprite("scoot", -100, 100)
s4.set_size(.322)

message1 = codesters.Text("this is my sigma coat of arms",0,220,"black")
message2 = codesters.Text("bottom text",0,-220,"black")