import turtle
from tkinter import messagebox, colorchooser

cursor = turtle.Turtle()
cursor.speed(-1)
screen = turtle.Screen()
screen.title("Arrow Paint V3 by Kiwifruit")


def dragging(x, y):
    cursor.ondrag(None)
    cursor.setheading(cursor.towards(x, y))
    cursor.goto(x, y)
    cursor.ondrag(dragging)

def clear():
    cursor.clear()

def lowerPen():
    cursor.pendown()
    messagebox.showinfo("Drawing is Enabled", "Drawing is Enabled") 
    turtle.listen()
def raisePen():
    cursor.penup()
    messagebox.showinfo("Drawing is Disabled", "Drawing is Disabled") 
    turtle.listen()

def color():
    chosenColor = colorchooser.askcolor()
    cursor.color(chosenColor)
    turtle.listen()

def run():
    turtle.listen()

    cursor.ondrag(dragging)
    turtle.onkey(color, "r")
    turtle.onkey(raisePen, "q")
    turtle.onkey(lowerPen, "e")
    turtle.onkey(clear, "x")

    screen.mainloop()

run()