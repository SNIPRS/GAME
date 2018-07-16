# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 22:48:28 2018

@author: runni
"""
import turtle
import math
import random
#import time

score = 0 
"""Set up window"""
window = turtle.Screen()
window.bgcolor("Lightgreen")


"""draw board"""
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()


"""Set up player1"""
player = turtle.Turtle()
player.color("Blue")
player.shape("triangle")
player.penup()
player.speed(0) #animation speed

bullet = turtle.Turtle()
bullet.turtlesize(0.25,0.25)
bullet.color("Black")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.hideturtle()


"""Create goals"""
maxGoals = 1
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300,300), random.randint(-300,300))
    


"""define global variables"""
speed = 1 

"""movement functions"""
def turnleft():
    player.left(30)
def turnright():
    player.right(30)
def increasespeed():
    global speed 
    if speed <= 3 and speed >= 0: #maxforward speed
        speed += 1
    elif speed < 0:
        speed -= speed 
def decreasespeed():
    global speed 
    if speed >= -2 and speed <= 0: #maxbackwards speed
        speed += -0.5
    elif speed > 0:
        speed -= speed 
def shootStuff():
    starX = player.xcor()
    starY = player.ycor()
    head = player.heading()
    bullet.setposition(starX, starY)
    bullet.setheading(head)
    bullet.showturtle()
    bullet.pendown()
    bullet.speed(3)
    bullet.forward(500)
    bullet.penup()
    bullet.hideturtle()
    

def isCollision(t1,t2):
    d = math.sqrt((t1.xcor() - t2.xcor())**2 + (t1.ycor() - t2.ycor())**2)
    if d < 20:
        return True
    else:
        return False
def boundaryCheckPlayer(something):
    global speed
    if something.xcor() == 300 and something.ycor() == 300:
        something.setposition(297,297)
    if something.xcor() == 300 and something.ycor() == -300:
        something.setposition(297,-297)
    if something.xcor() == -300 and something.ycor() == -300:
        something.setposition(-297,-297)
    if something.xcor() == -300 and something.ycor() == 300:
        something.setposition(-297,297)
    else:
        if something.xcor() > 300 or something.xcor() < -300:
            if speed > 0:
                speed = 0
                player.backward(2)
            elif speed < 0:
                speed = 0
                player.forward(3)
        if something.ycor() > 300 or something.ycor() < -300:
            if speed > 0:
                speed = 0
                player.backward(2)
            elif speed < 0:
                speed = 0
                player.forward(3)
def boundaryCheckGoal(something):
    if something.xcor() > 300 or something.xcor() < -300:
        something.right(180)
    if something.ycor() > 300 or something.ycor() < -300:
        something.right(180)




    
"""keyboard commands"""
turtle.listen()
turtle.onkeypress(turnleft, "Left")
turtle.onkeypress(turnright, "Right")
turtle.onkeypress(increasespeed, "Up")
turtle.onkeypress(decreasespeed, "Down")
turtle.onkeypress(shootStuff, "space")
#create timer
#zero = 0
#seconds = 11
#for i in range(seconds):
#    time.sleep(1)
#    zero += 1

"""ending"""
playgame = True
while playgame:
    player.forward(speed)
    
    """Boundary check"""
    boundaryCheckPlayer(player)
    """Collision detection"""
    if isCollision(player, goals[count]):
        goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
        goals[count].right(random.randint(0,360))
        score += 1 
        """Draw score on screen"""
        mypen.undo()
        mypen.penup()
        mypen.hideturtle()
        mypen.setposition(-290, 301)
        scorestring = "Score %s" %score
        mypen.write(scorestring, False, align="left", font =("Arial", 14,"normal"))
    """Move goal"""
    for count in range(maxGoals):
        goals[count].forward(1)
        boundaryCheckGoal(goals[count])
    if score > 5:
        playgame = False
    
        


turtle.done()
turtle.bye()