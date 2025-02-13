# Section 1 - Setup
import codesters, random, os, time
from codesters import StageClass
stage = StageClass()
stage.disable_floor()

stage.set_background("astroworld")
player = codesters.Sprite("grammy")
object_speed = 1
lives = 3

# Section 2 - Objects

def falling_object():
    global object_speed, lives

    if lives >= 0:
        x = random.randint(-200, 200)
        y = 275
        object = codesters.Sprite("travis", x, y)
        object.set_size(1)
        object.set_y_speed(object_speed)

stage.event_interval(falling_object, 10)
        
def gameover():
    exit(2)

# Section 3 - Collision
def collision(player, object):
    global lives

    if object.get_image_name() == "travis":
        stage.remove_sprite(object)
        print(lives)
        lives -= 1
        if lives >= 1:
            player.say(f"{lives} lives!",4)
        elif lives == 1:
            player.say(f"{lives} life!", 4)
        else:
            player.say(f"Out of lives - you lose!", 5)
            gameover()
player.event_collision(collision)

# Section 4 - Controls

# Right key
def go_right():
    player.move_right(5)

def go_left():
    player.move_left(5)

player.event_key("d", go_right)
player.event_key("right", go_right)
player.event_key("a", go_left)
player.event_key("left", go_left)