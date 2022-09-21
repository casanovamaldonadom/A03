######################################################################
# Author: Melany Casanova-Maldonado
# Username: casanovamaldonadom
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To create useful functions
# Google Doc Link: https://docs.google.com/document/d/1O4429F5CyyDgYA5l3CZfSW88ajpoBmokd15yLaS0NAg/edit?usp=sharing
######################################################################
import turtle

bird_turtle = turtle.Turtle()
bird_turtle.shape('turtle')
bird_turtle.color('black')
bird_turtle.pensize(5)
bird_turtle.speed(0)

def drawbird():
    """Uses two semicircles to create the birds in the sky."""
    bird_turtle.right(30)
    bird_turtle.pendown()
    bird_turtle.circle(-50, 100)
    bird_turtle.left(75)
    bird_turtle.circle(-50, 100)

def main():
    """Draws the sea, the sun, birds, and a sailboat against a blue background"""

    wn = turtle.Screen()
    wn.bgcolor('#c4ebf8')

    water_turtle = turtle.Turtle()
    water_turtle.shape('turtle')
    water_turtle.color('darkblue')
    water_turtle.speed(0)
    water_turtle.pensize(10)

    water_turtle.penup()
    water_turtle.right(90)
    water_turtle.forward(170)
    water_turtle.pendown()
    water_turtle.begin_fill()
    water_turtle.left(90)
    water_turtle.forward(350)
    water_turtle.right(180)
    water_turtle.forward(710)

    water_turtle.left(90)
    water_turtle.forward(160)
    water_turtle.left(90)
    water_turtle.forward(710)
    water_turtle.left(90)
    water_turtle.forward(160)
    water_turtle.end_fill()
    water_turtle.hideturtle()

    bird_turtle.penup()
    bird_turtle.left(90)
    bird_turtle.forward(130)

    drawbird()

    bird_turtle.penup()
    bird_turtle.right(115)
    bird_turtle.forward(420)
    bird_turtle.right(90)

    drawbird()

    bird_turtle.penup()
    bird_turtle.right(22)
    bird_turtle.forward(130)
    bird_turtle.left(90)
    bird_turtle.forward(250)
    bird_turtle.left(90)

    drawbird()

    bird_turtle.hideturtle()

    sun_turtle = turtle.Turtle()
    sun_turtle.pensize(10)
    sun_turtle.speed(0)
    sun_turtle.color('#fdd102')
    sun_turtle.shape('turtle')

    sun_turtle.penup()
    sun_turtle.left(90)
    sun_turtle.forward(220)
    sun_turtle.right(90)
    sun_turtle.forward(300)
    sun_turtle.begin_fill()
    sun_turtle.pendown()
    sun_turtle.circle(100)
    sun_turtle.end_fill()
    sun_turtle.hideturtle()

    boat_body_turtle = turtle.Turtle()
    boat_body_turtle.color('#895009')
    boat_body_turtle.pensize(7)
    boat_body_turtle.speed(0)
    boat_body_turtle.shape('turtle')

    boat_body_turtle.penup()
    boat_body_turtle.right(90)
    boat_body_turtle.forward(165)
    boat_body_turtle.right(90)
    boat_body_turtle.forward(110)
    boat_body_turtle.pendown()
    boat_body_turtle.begin_fill()
    boat_body_turtle.forward(170)
    boat_body_turtle.right(60)
    boat_body_turtle.forward(94)
    boat_body_turtle.right(120)
    boat_body_turtle.forward(250)
    boat_body_turtle.right(110)
    boat_body_turtle.forward(85)
    boat_body_turtle.end_fill()

    boat_body_turtle.penup()
    boat_body_turtle.color('black')
    boat_body_turtle.right(70)
    boat_body_turtle.forward(90)
    boat_body_turtle.right(90)
    boat_body_turtle.forward(80)
    boat_body_turtle.pendown()
    boat_body_turtle.forward(170)
    boat_body_turtle.penup()

    boat_body_turtle.color('white')
    boat_body_turtle.right(130)
    boat_body_turtle.pendown()
    boat_body_turtle.begin_fill()
    boat_body_turtle.forward(170)
    boat_body_turtle.right(140)
    boat_body_turtle.forward(130)
    boat_body_turtle.right(90)
    boat_body_turtle.forward(110)
    boat_body_turtle.end_fill()
    boat_body_turtle.penup()

    boat_body_turtle.right(180)
    boat_body_turtle.forward(220)
    boat_body_turtle.right(90)
    boat_body_turtle.color('black')
    style = ('Bradley Hand', 20, 'bold')
    boat_body_turtle.write('Melany wuz heer', font=style, align='center')
    boat_body_turtle.hideturtle()

    wn.exitonclick()

main()
