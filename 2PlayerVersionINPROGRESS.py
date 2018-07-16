# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 09:57:19 2018

@author: SNIPRS
"""

"""LETS GOOOO BOISSSS"""
import turtle 
import random
import time
turtle.setundobuffer(1)

"""Set up window"""
def WindowSetup():
    window = turtle.Screen()
    window.screensize(1200, 600, "Darkblue")
    
WindowSetup()


"""Placeholder setup for now"""
explosion = turtle.Turtle()
explosion.speed(0)
explosion.shape("triangle")
explosion.penup()
explosion.goto(-1000,-1000)



"""Character class"""
class character(turtle.Turtle):
    def __init__(self, CHARshape, color, startx, starty):
        """
        Initializes a character class with parameters
        """
        turtle.Turtle.__init__(self, shape = CHARshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.forward(0)
        self.goto(startx, starty)
        self.speed = 1
#============================================================================
    def boundaryCheck(self):
        """
        Checks to see if the player object may go 
        past the boundary and corrects
        """
        if self.xcor() > 600:
            self.speed = 0
            self.setx(598)
        if self.xcor() < -600:
            self.speed = 0
            self.setx(-598)
        if self.ycor() > 300:
            self.speed = 0
            self.sety(298)
        if self.ycor() < -300:
            self.speed = 0
            self.sety(-298)
    def middleBoundaryCheck(self):
        """
        Checks the middle restrictive areas for this map
        """
        if self.xcor() >= -300 and self.xcor() <= 300:
            if self.xcor() >= -2 and self.xcor() < 2:
                if self.ycor() >= -152 and self.ycor() <= 152:
                    if self.speed > 0:
                        self.speed = 0 
                        player.backward(4)
                    elif self.speed < 0:
                        self.speed = 0
                        player.forward(4)
            if self.ycor() >= -152 and self.ycor() <= -148 or self.ycor() >= 148 and self.ycor() <= 152:
                if self.speed > 0:
                    self.speed = 0 
                    player.backward(2)
                elif self.speed < 0:
                    self.speed = 0
                    player.forward(3)
    def middleBoundaryCheck2(self):
        """
        Checks the middle restrictive areas for this map
        """
        if self.xcor() >= -300 and self.xcor() <= 300:
            if self.xcor() >= -2 and self.xcor() < 2:
                if self.ycor() >= -152 and self.ycor() <= 152:
                    if self.speed > 0:
                        self.speed = 0 
                        player2.backward(4)
                    elif self.speed < 0:
                        self.speed = 0
                        player2.forward(4)
            if self.ycor() >= -152 and self.ycor() <= -148 or self.ycor() >= 148 and self.ycor() <= 152:
                if self.speed > 0:
                    self.speed = 0 
                    player2.backward(2)
                elif self.speed < 0:
                    self.speed = 0
                    player2.forward(3)
#                    
#        if self.xcor() == 0:
#            if self.ycor() >= -152 and self.ycor() <= 152:
#                if self.speed > 0:
#                    self.speed = 0 
#                    player.backward(2)
#                elif self.speed < 0:
#                    self.speed = 0
#                    player.forward(3)

    def boundaryCheckBounce(self):
        """
        lets the object bounce off at the 
        incident angle when hitting a boundary
        """
        if self.xcor() > 595:
            if self.heading() < 90:
                self.setx(595)
                self.lt(60)
            else: 
                self.setx(595)
                self.rt(60)
        if self.xcor() < -595:
            if self.heading() > 180:
                self.setx(-595)
                self.lt(60)
            else: 
                self.setx(-595)
                self.rt(60)
        if self.ycor() > 295:
            if self.heading() > 90:
                self.sety(295)
                self.lt(60)
            else: 
                self.sety(295)
                self.rt(60)
		
        if self.ycor() < -295:
            if self.heading() > 270:
                self.sety(-295)
                self.lt(60)
            else: 
                self.sety(-295)
                self.rt(60)
        
#============================================================================
    def move(self):
        """
        moves forward at the set speed and 
        checks for boundary collision
        """
        self.forward(self.speed)
        self.boundaryCheck()
        self.middleBoundaryCheck()
    def move2(self):
        """
        moves forward at the set speed and 
        checks for boundary collision
        """
        self.forward(self.speed)
        self.boundaryCheck()
        self.middleBoundaryCheck2()
        
    def moveBounce(self):
        self.forward(self.speed)
        self.boundaryCheckBounce()
        
    def isCollision(self,other,hitbox):
        """
        other: other turtle object
        hitbox: hitbox size of other
        Returns bool
        """
        if self.distance(other) < hitbox:
            return True
        else:
            return False

class Mud(character):
    def __init__(self, CHARshape, color, startx, starty):
        character.__init__(self, CHARshape, color, startx, starty)
        self.hitbox = 30
        self.shapesize(stretch_wid=3, stretch_len=3, outline=None)
        self.speed = 0
    def isCollision(self,other,hitbox):
        """
        other: other turtle object
        hitbox: hitbox size of other
        Returns bool
        """
        if self.distance(other) < self.hitbox:
            return True
        else:
            return False
    def slow(self, other):
        boo = self.isCollision(other,self.hitbox)
        if boo:
            other.speed *= 0.9

""" Inherited classes from Character"""
class Player(character):
    def __init__(self, CHARshape, color, startx, starty):
        character.__init__(self, CHARshape, color, startx, starty)
        """
        Initializes player, sets default values
        """
        self.shapesize(stretch_wid=0.5, stretch_len=1.3, outline=None)
        self.speed = 0 
        self.Maxspeed = 3
        self.MaxBackSpeed = -2
        self.lives = 3
        
    """
    Turning
    """
    def turnLeft(self):
        self.left(30)
    def turnRight(self):
        self.right(30)
            
    """
    Speed control
    """
    def accelerate(self):
        if self.speed <= self.Maxspeed:
                self.speed += 0.5
    def decelerate(self):
        if self.speed >= self.MaxBackSpeed:
                self.speed -= 0.25
    def STOP(self):
        self.speed = 0
            
            


class Target(character):
    def __init__(self, CHARshape, color, startx, starty):
        character.__init__(self, CHARshape, color, startx, starty)
        """
        Training dummies
        """
        self.speed = random.uniform(0.2, 2)
        self.setheading(random.randint(0,360))

class Shell(character):
    def __init__(self, CHARshape, color, startx, starty):
        character.__init__(self, CHARshape, color, startx, starty)
        self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
        self.status = "ready"
        self.status2 = "ready"
        self.speed = 4
        self.goto(-1000,-1000)
    def fire1(self):
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"
    def fire2(self):
        if self.status2 == "ready":
            self.goto(player2.xcor(), player2.ycor())
            self.setheading(player2.heading())
            self.status2 = "firing"
    def move(self):
        if self.status == "firing":
            self.fd(self.speed)  
        if self.xcor() < -595 or self.xcor() > 595 or \
			self.ycor()< -295 or self.ycor()> 295:
                self.goto(-1000, -1000)
                self.status = "ready"
        if self.xcor() >= -300 and self.xcor() <= 300:
            if self.xcor() >= -2 and self.xcor() < 2:
                if self.ycor() >= -152 and self.ycor() <= 152:
                    self.goto(-1000, -1000)
                    self.status = "ready"
    def move2(self):
        if self.status2 == "firing":
            self.fd(self.speed)  
        if self.xcor() < -595 or self.xcor() > 595 or \
			self.ycor()< -295 or self.ycor()> 295:
                self.goto(-1000, -1000)
                self.status2 = "ready"
        if self.xcor() >= -300 and self.xcor() <= 300:
            if self.xcor() >= -2 and self.xcor() < 2:
                if self.ycor() >= -152 and self.ycor() <= 152:
                    self.goto(-1000, -1000)
                    self.status2 = "ready"

class Rocket(Shell):
    def __init__(self, CHARshape, color, startx, starty):
        character.__init__(self, CHARshape, color, startx, starty)
        self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
        self.status = "ready"
        self.explode = "no"
        self.speed = 2
        self.goto(-1000,-1000)
    def fire1(self):
        if self.status == "ready":
            rocket2.fire1()
            rocket3.fire1()
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"
    def fire2(self):
        if self.status == "ready":
            rocket2.fire2()
            rocket3.fire2()
            self.goto(player2.xcor(), player2.ycor())
            self.setheading(player2.heading())
            self.status = "firing"
    
    def explodeGo(self):
        explosion.goto(self.xcor(), self.ycor())
        explosion.goto(self.xcor()+3, self.ycor()+3)
        explosion.goto(self.xcor()-3, self.ycor())
        explosion.goto(self.xcor(), self.ycor()-3)
        explosion.goto(self.xcor()-3, self.ycor()+3)
        explosion.goto(self.xcor(), self.ycor()-6)
        explosion.goto(self.xcor(), self.ycor())
        explosion.goto(-1000, -1000)
        
    def move(self):
        if self.status == "firing":
            self.fd(self.speed)
            
        if self.xcor() < -595 or self.xcor() > 595 or \
			self.ycor()< -295 or self.ycor()> 295:
                self.explodeGo()
                self.goto(-1000, -1000)
                self.status = "ready"
        if self.xcor() >= -300 and self.xcor() <= 300:
            if self.xcor() >= -2 and self.xcor() < 2:
                if self.ycor() >= -152 and self.ycor() <= 152:
                    self.explodeGo()
                    self.goto(-1000, -1000)
                    self.status = "ready"        
#        if self.xcor() >= -300 and self.xcor() <= 300:
#            if self.ycor() >= -151 and self.ycor() <= -149 or self.ycor() >= 149 and self.ycor() <= 151:
#                self.explodeGo()
#                self.goto(-1000, -1000)
#                self.status = "ready"

class RocketSub1(Rocket):
    def __init__(self, CHARshape, color, startx, starty):
        character.__init__(self, CHARshape, color, startx, starty)
        self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
        self.status = "ready"
        self.explode = "no"
        self.speed = 2
        self.goto(-1000,-1000)
    def fire1(self):
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading() + 10)
            self.status = "firing" 
    def fire2(self):
        if self.status == "ready":
            self.goto(player2.xcor(), player2.ycor())
            self.setheading(player2.heading() + 10)
            self.status = "firing" 
            
class RocketSub2(Rocket):
    def __init__(self, CHARshape, color, startx, starty):
        character.__init__(self, CHARshape, color, startx, starty)
        self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
        self.status = "ready"
        self.explode = "no"
        self.speed = 2
        self.goto(-1000,-1000)
    def fire1(self):
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading() - 10)
            self.status = "firing"     
    def fire2(self):
        if self.status == "ready":
            self.goto(player2.xcor(), player2.ycor())
            self.setheading(player2.heading() - 10)
            self.status = "firing"




class FOOKINLAZORBEAM(Shell):
    def __init__(self, CHARshape, color, startx, starty):
        character.__init__(self, CHARshape, color, startx, starty)
        self.shapesize(stretch_wid=0.2, stretch_len=1.5, outline=None)
        self.status = "ready"
        self.status2 = "ready" 
        self.ammo = 50
        self.ammo2 = 50
        self.speed = 7
        self.goto(-1000,-1000)
    def move(self):
        if self.status == "firing":
            self.fd(self.speed)  
        if self.xcor() < -595 or self.xcor() > 595 or \
			self.ycor()< -295 or self.ycor()> 295:
                self.goto(-1000, -1000)
                self.status = "ready"
    def move2(self):
        if self.status2 == "firing":
            self.fd(self.speed)  
        if self.xcor() < -595 or self.xcor() > 595 or \
			self.ycor()< -295 or self.ycor()> 295:
                self.goto(-1000, -1000)
                self.status2 = "ready"
                
    def fire1(self):
        if self.ammo > 0 and self.status == "ready" :
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.ammo -= 1
            self.status = "firing"   
    def fire2(self):
        if self.ammo2 > 0 and self.status2 == "ready" :
            self.goto(player2.xcor(), player2.ycor())
            self.setheading(player2.heading())
            self.ammo2 -= 1
            self.status2 = "firing" 

class Particle(character):
    def __init__(self, CHARshape, color, startx, starty):
        character.__init__(self, CHARshape, color, startx, starty)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.goto(-1000,-1000)
        self.frame = 0

    def explode(self, startx, starty):
        self.goto(startx,starty)
        self.setheading(random.randint(0,360))
        self.frame = 1

    def move(self):
        if self.frame > 0:
            self.fd(10)
            self.frame += 1

        if self.frame > 15:
            self.frame = 0
            self.goto(-1000, -1000)
  
class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.score2 = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.pen2 = turtle.Turtle()
        self.pen3 = turtle.Turtle()
        self.pen3.ht()
        self.lives = 3
        self.lives2 = 3 
		
    def draw_border(self):
#Draw border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-600, -300)
        self.pen.pendown()
        self.pen.forward(1200)
        self.pen.left(90)
        self.pen.forward(600)
        self.pen.left(90)
        self.pen.forward(1200)
        self.pen.left(90)
        self.pen.forward(600)
        self.pen.penup()
        
        self.pen.goto(-300, 150)
        self.pen.pendown()
        self.pen.setheading(0)
        self.pen.forward(600)
        self.pen.penup()
        self.pen.goto(-300, -150)
        self.pen.pendown()
        self.pen.setheading(0)
        self.pen.forward(600)
        self.pen.penup()
        
        self.pen.goto(0,150)
        self.pen.pendown()
        self.pen.setheading(270)
        self.pen.forward(300)
        self.pen.penup()
        self.pen.goto(-1000,-1000)
        self.pen.ht()
        self.pen.pendown()
        
    def showEndGame(self):
        msg = "Game over! You may now close the window" 
        self.pen3.speed(0)
        self.pen3.color("white")
        self.pen3.pensize(3)
        self.pen3.penup()
        self.pen3.goto(-150, 0)
        self.pen3.write(msg, font=("Arial", 16, "normal"))
        self.pen3.ht()

    def show_status(self):
        self.pen.undo()
        msg = "Score: %s    Lives: %s" %(self.score, player.lives)
        self.pen.penup()
        self.pen.goto(-300, 310)
        self.pen.write(msg, font=("Arial", 16, "normal"))
        
    def show_status2(self):
        self.pen.undo()
        msg = "Score: %s    Lives: %s" %(self.score2, player2.lives)
        self.pen.penup()
        self.pen.goto(300, 310)
        self.pen.write(msg, font=("Arial", 16, "normal"))
        
    def show_controls(self):
        msg1 = "Accelerate: up arrow, Decelerate: down arrow, Turn: left and right arrows, Stop: q, Shoot: space, Shotgun: w, Particle cannon: e"
        self.pen2.speed(0)
        self.pen2.color("white")
        self.pen2.pensize(3)
        self.pen2.penup()
        self.pen2.goto(-610, -330)
        self.pen2.write(msg1, font=("Arial", 16, "normal"))
        self.pen2.ht()

player = Player("triangle", "white", 300, 0)
player2 = Player("triangle", "black", -300, 0)
player2.setheading(180)

game = Game()
game.draw_border()
game.show_status()
game.show_controls()


missile = Shell("triangle", "yellow", 0, 0)
missile2 = Shell("triangle", "yellow", 0, 0)

rocket = Rocket("circle", "black", 0, 0)
rocket2 = RocketSub1("circle", "black", 0, 0)
rocket3 = RocketSub2("circle", "black", 0, 0)

rocket2 = Rocket("circle", "black", 0, 0)
rocket22 = RocketSub1("circle", "black", 0, 0)
rocket32 = RocketSub2("circle", "black", 0, 0)

lazer = FOOKINLAZORBEAM("triangle", "Lightblue", 0,0)
lazer2 = FOOKINLAZORBEAM("triangle", "Lightblue", 0,0)

mud1 = Mud("circle", "Lightgreen", -100, 0)
mud2 = Mud("circle", "Lightgreen", 100, 0)

Targets =[]
for i in range(6):
    Targets.append(Target("circle", "red", -100, 0))
    
particles = [4]
for i in range(20):
    particles.append(Particle("circle", "orange", 0, 0))


turtle.onkeypress(player.turnLeft, "Left")
turtle.onkeypress(player.turnRight, "Right")
turtle.onkeypress(player.accelerate, "Up")
turtle.onkeypress(player.decelerate, "Down")
turtle.onkeypress(player.STOP, "j")
turtle.onkeypress(missile.fire1, "k")
turtle.onkeypress(rocket.fire1, "l")
turtle.onkeypress(lazer.fire1, ";")

turtle.onkeypress(player2.turnLeft, "a")
turtle.onkeypress(player2.turnRight, "d")
turtle.onkeypress(player2.accelerate, "w")
turtle.onkeypress(player2.decelerate, "s")
turtle.onkeypress(player2.STOP, "x")
turtle.onkeypress(missile.fire2, "c")
turtle.onkeypress(rocket.fire2, "v")
turtle.onkeypress(lazer.fire2, "b")

turtle.listen()


turtle.ht()

def missileCollision():
    if missile.isCollision(target, 20):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        target.goto(x, y)
        missile.goto(-1000, -1000)
        game.score += 100
        game.show_status()
        missile.status = "ready"
def rocketCollision():
    if rocket.isCollision(target, 20):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        target.goto(x, y)
        rocket.goto(-1000, -1000)
        rocket.explode = "yes"
        game.score += 100
        game.show_status()
        rocket.status = "ready"
def rocketCollision2():
    if rocket2.isCollision(target, 20):
        
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        target.goto(x, y)
        rocket.goto(-1000, -1000)
        rocket.explode = "yes"
        game.score += 120
        game.show_status()
        rocket.status = "ready"
def rocketCollision3():
    if rocket3.isCollision(target, 20):
        
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        target.goto(x, y)
        rocket.goto(-1000, -1000)
        rocket.explode = "yes"
        game.score += 120
        game.show_status()
        rocket.status = "ready"
def lazerCollision():
    if lazer.isCollision(target, 20):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        target.goto(x, y)
        lazer.goto(-1000, -1000)
        game.score += 80
        game.show_status()
        lazer.status = "ready"   

def playerCollision():
    if target.isCollision(player, 20):
        player.goto(300,0)
        player.speed = 0
        player.lives -= 1
        game.show_status()
def playerCollision2():
    if target.isCollision(player2, 20):
        player2.goto(300,0)
        player2.speed = 0
        player2.lives -= 1
        game.show_status()

while player.lives > 0:

    turtle.tracer(0, 0)
    player.move()
    player2.move2()
    missile.move()
    missile2.move2()
    lazer.move()
    lazer2.move2()
    rocket2.move()
    rocket22.move()
    rocket32.move()
    rocket.move()
    rocket2.move()
    rocket3.move()
    
    mud1.slow(player)
    mud2.slow(player)
    
    mud1.slow(player2)
    mud2.slow(player2)
    
    for target in Targets:
        target.moveBounce()
        missileCollision()
        
        playerCollision()
        playerCollision2()
        lazerCollision()
        rocketCollision()
        rocketCollision2()
        rocketCollision3()
    turtle.update()
    
    
    
    
if player.lives == 0:
    game.showEndGame()

turtle.done()
turtle.bye()
