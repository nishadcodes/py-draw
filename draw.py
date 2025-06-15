import turtle
import pygame
import sys

colorstate = "Black"
# Music handlers
pygame.init()
pygame.mixer.init()
bgmusic = pygame.mixer.Sound("Hermione.mp3")
bgmusic.play(loops = -1)

# Turtle setup
pen = turtle.Pen()
pen.pencolor("black")
color = turtle.Pen()
color.pencolor("black")
# Screen setup
screen = turtle.Screen()
screen.title("Sketchpad")

# Color key info
pen.penup()
pen.goto(-screen.window_width()//2 + 15, screen.window_height()//2 - 20)
pen.pendown()
pen.pencolor("black")
pen.write("B key for black", font=("Arial", 8, "bold"))
pen.penup()
pen.sety(pen.ycor() - 20)
pen.write("E key for eraser", font=("Arial", 8, "bold"))
pen.sety(pen.ycor() - 20)
pen.write("O key for orange", font=("Arial", 8, "bold"))
pen.sety(pen.ycor() - 20)
pen.write("C key for clear(inc. this)", font=("Arial", 8, "bold"))
pen.sety(pen.ycor() - 20)
pen.write("Q key to quit", font=("Arial", 8, "bold"))
pen.sety(pen.ycor() - 20)
pen.write("U key for pen up", font=("Arial", 8, "bold"))
pen.sety(pen.ycor() - 20)
pen.write("D key for pen down", font=("Arial", 8, "bold"))
def colorinfo():
    color.penup()
    color.goto(-screen.window_width()//2 + 15, -screen.window_height()//2 - 20)
    color.write("Color =" + colorstate)
    screen.ontimer(colorinfo, 50)
pen.home()
pen.pendown()

# Movement functions
def move_up():
    pen.setheading(90)
    pen.forward(5)

def move_down():
    pen.setheading(270)
    pen.forward(5)

def move_left():
    pen.setheading(180)
    pen.forward(5)

def move_right():
    pen.setheading(0)
    pen.forward(5)

# Color changers
def black():
    pen.pencolor("black")
    colorstate = "Black"
    color.clear()

def orange():
    pen.pencolor("orange")
    colorstate("Orange")
    color.clear()

def eraser():
    pen.pencolor("white")
    colorstate = "Erasing"
    color.clear()
# General funtions
def clear():
    pen.clear()

def kill():
    sys.exit()

def pup():
    pen.penup()

def pdown():
    pen.pendown
# Key bindings
colorinfo()
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(black, "b")
screen.onkeypress(orange, "o")
screen.onkeypress(eraser, "e")
screen.onkeypress(clear, "c")
screen.onkeypress(kill, "q")
screen.onkeypress(pup, "u")
screen.onkeypress(pdown, "d")
screen.mainloop()
