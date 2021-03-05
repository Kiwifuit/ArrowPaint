import turtle
from tkinter import Tk, colorchooser, messagebox, Button, Label

root = Tk()
root.title("Keybindings")

# Custom Functions for this program

# Hides the Tk window
def closePrompt():
    root.withdraw()
def showPrompt():
    root.deiconify()

# Basic Movement functions
def up():
    char.setheading(90)
    char.forward(10)
def down():
    char.setheading(270)
    char.forward(10)
def left():
    char.setheading(180)
    char.forward(10)
def right():
    char.setheading(0)
    char.forward(10)

# Raise and Lower the turtle pen
def lowerPen():
    char.pendown()
    messagebox.showinfo("Drawing is Enabled", "Drawing is Enabled") # Alerts the user when the pen is lowered
    turtle.listen() # Makes the program listen again for the keystrokes (below) after executing the code above
def raisePen():
    char.penup()
    messagebox.showinfo("Drawing is Disabled", "Drawing is Disabled") # Alerts the user when the pen is raised
    turtle.listen() # Makes the program listen again for the keystrokes (below) after executing the code above

# Color Selector
def color():
    root.withdraw()
    chosenColor = colorchooser.askcolor()
    char.color(chosenColor)
    turtle.listen() # Makes the program listen again for the keystrokes (below) after executing the code above

# Easter Egg
def dio():
    messagebox.showwarning("Dio", "KONO DIO DA")

# Clears the screen
def clear():
    char.clear()
    messagebox.showinfo("Canvas Cleared", "Canvas Cleared!\nYou may draw again")

# This whole block of code is for the Tk Window
# It is used so that the keybindings are shown upon program startup

# Make Tk widgets
keybindings = Label(root, text = "Keybindings: ")
keysText = Label(root, text = "WSAD to Move\nQ and E to Disable/Enable Drawing\nC to clear\n` to pick another color\nO to show this window again\nBTW, what does / do?")
hidePrompt = Button(root, text = "Hide this Window", command = closePrompt)

# Show the Tk widgets defined earlier
keybindings.place(x=0, y=0) # Upper-Left edge of the window
keysText.place(x=0, y=30) # Below the text
hidePrompt.place(x=50, y=150) # At the edge of the window

# Char (Turtle) data
char = turtle.Turtle()
char.speed(0)

# Screen data
screen = turtle.Screen()
screen.title("Arrow Paint")

# Make Turtle Listen to Keystrokes. Used for the keybindings thingy
turtle.listen()

# Keybindings

# Do not edit the keybindings. I will add a feature to allow that in the near future

# Misc keybindings
turtle.onkey(color, "`")
turtle.onkey(raisePen, "q")
turtle.onkey(lowerPen, "e")
turtle.onkey(dio, "/")
turtle.onkey(showPrompt, "o")
turtle.onkey(clear, "c")

# Movement keybindings
turtle.onkey(up, "w")
turtle.onkey(down, "s")
turtle.onkey(left, "a")
turtle.onkey(right, "d")


turtle.done() # For the window to stay open