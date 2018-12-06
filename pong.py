# CS-UY 1114
# Final project

import turtle
import time
import random
import math

turtle.setup(1000, 900)
pong = turtle.Screen()
pong.title("Pong")
pong.bgcolor("black")
turtle.color("white")

# This variable represents the x position
# of the player's paddle. Initially, it
# will be 0 (i.e. in the center). The y
# position of the paddles never changes,
# so we don't need a variable for it.
user1x = 0

# This variable represents the x position
# of the computer's paddle. Initially, it
# will be 0 (i.e. in the center)
user2x = 0

# These variables store the current x and y
# position of the ball. Their values will be
# updates on each frame, as the ball moves.
ballx = 0
bally = -50

# These variables store the current x and y
# velocity of the ball. Their values will be
# updates on each frame, as the ball moves.
ballvx = 0
ballvy = 0

# These variables store the current score 
# of the game.
user1points = 0
user2points = 0


def draw_rectangle(orientation):
    turtle.seth(orientation)
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(80)


def draw_frame():
    """
    signature: () -> NoneType
    Given the current state of the game in
    the global variables, draw all visual
    elements on the screen: the paddles,
    the ball, and the current score.
    Please note that this is your only function
    where drawing should happen (i.e. the only
    function where you call functions in the
    turtle module). Other functions in this
    program merely update the state of global
    variables.
    This function also should not modify any
    global variables.
    Hint: write this function first!
    """
    turtle.up()
    turtle.setposition(ballx, bally)
    turtle.down()
    turtle.dot(30, "white")
    turtle.up()
    turtle.setposition(user1x, -450)
    turtle.down()
    draw_rectangle(90)
    turtle.up()
    turtle.setposition(user2x, 350)
    turtle.down()
    draw_rectangle(270)
    turtle.up()
    turtle.setposition(-500, 350)
    turtle.down()
    turtle.seth(0)
    turtle.forward(1000)
    turtle.up()
    turtle.setposition(-475, 416)
    turtle.write("You have " + str(user1points) + " points")
    turtle.setposition(-475, 383)
    turtle.write("The computer has " + str(user2points) + " points")


def key_left():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the user's paddle
    appropriately by modifying the variable
    user1x.
    """
    global user1x
    if user1x > -410:
        user1x -= 30


def key_right():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the user's paddle
    appropriately by modifying the variable
    user1x.
    """
    global user1x
    if user1x < 410:
        user1x += 30


def reset():
    """
    signature: () -> NoneType
    Reset the global variables representing
    the position and velocity of the ball and
    the position of the paddlesto their initial
    state, effectively restarting the game. The
    initial velocity of the ball should be random
    (but there there must be nonzero vertical
    velocity), but the speed of the ball should
    be the same in every game.
    """
    global user1x, user2x, ballvx, ballvy, ballx, bally
    ballx, bally = 0, -50
    user1x, user2x = 0, 0
    ballvx = 0
    while ballvx == 0:
        ballvx = random.randint(-8, 8)
        ballvy = (64 - ballvx ** 2) ** 0.5
    while ballvy == 0:
        ballvx = random.randint(-8, 8)
        ballvy = (64 - ballvx ** 2) ** 0.5


def ai():
    """
    signature: () -> NoneType
    Perform the 'artificial intelligence' of
    the game, by moving the computer's paddle
    to an appropriate location by updating
    the user2x variable. The computer
    paddle should move towards the ball in an
    attempt to get under it.
    """
    global user2x
    if bally > 0:
        if user2x + 75 < ballx:
            user2x += 10
        elif user2x - 75 > ballx:
            user2x -= 10


def angle_on_bounce(userx):
    """
    sig: int -> None
    Sets the velocity for the paddle depending on where the ball hits it
    """
    global ballvx, ballvy
    angle = (abs(ballx - userx) / 75) * (70 * math.pi / 180)
    ballvy = math.cos(angle) * 8
    ballvx = math.sqrt(64 - (ballvy ** 2))
    if ballx - userx < 0:
        ballvx = -1 * abs(ballvx)
    if userx == user2x:
        ballvy = -1 * abs(ballvy)
    else:
        ballvy = abs(ballvy)
    print(ballx - userx, angle)


def physics():
    """
    signature: () -> NoneType
    This function handles the physics of the game
    by updating the position and velocity of the
    ball depending on its current location. This
    function should detect if the ball has collided
    with a paddle or a wall, and if so, adjust the
    direction of the ball (as stored in the ballvx
    and ballvy variables) appropriately. If the ball
    has not collided with anything, the position of the
    ball should be updated according to its current
    velocity.
    This function should also detect if one of
    the two players has missed the ball. If so, it
    should award a point to the other player, and
    then call the reset() function to start a new
    round.
    """
    global ballx, bally, ballvx, ballvy, user1points, user2points
    if bally > 330:
        user1points += 1
        reset()
    if bally < -430:
        user2points += 1
        reset()
    if bally > 310 and abs(ballx - user2x) < 75:
        angle_on_bounce(user2x)
    if bally < -410 and abs(ballx - user1x) < 75:
        print(bally)
        angle_on_bounce(user1x)
    if ballx > 480:
        ballvx = -1 * abs(ballvx)
    if ballx < -480:
        ballvx = abs(ballvx)
    ballx += ballvx
    bally += ballvy


def main():
    """
    signature: () -> NoneType
    Run the pong game. You shouldn't need to
    modify this function.
    """
    turtle.tracer(0, 0)
    turtle.hideturtle()
    turtle.onkey(key_left, "Left")
    turtle.onkey(key_right, "Right")
    turtle.listen()
    reset()
    while True:
        physics()
        ai()
        turtle.clear()
        draw_frame()
        turtle.update()
        time.sleep(0.01)


main()
