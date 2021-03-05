Arrow Paint Documentation
-----------------------------
Hello...again...I guess

Anyways, here I am with another repo, but it might be too late for this kind of stuff, I dunno.
Writing markdown documents for repos *nobody* will read to seems fun tbh. *minus the fact that nobody will go to this repo, but whatever*

The Humble Beginnings
------------------------
Arrow Paint used to be a smol app, only capable of drawing in black.

Then I decided to overhaul it...

If you've dug through the code before reading this <sup>like a motherfucking scumbag</sup>, you have noticed the shit ton of comments I made, that was when I decided: *This shit is better on GitHub, even though nobody will bother themselves with reading through this but whatever, comments go brrrrrrrrrrrrrrrrrrrrrrr* and just yeeted comments everywhere.

But in case you are reading *this* first before reading the code, this was the base code:

```py
import turtle

char = turtle.Turtle()
char.speed(0)

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

turtle.done()
```

Evolution <sup>(Kiwi, you *have* to improve your naming skills)</sup>
--------------------------------------------

After a few...I dunno, time units? Anyways, after a few days or weeks or however long that was, I changed the code, because major improvements with the understanding of Python's Turtle module <sup>(the founding of the messagebox was *completely* by accident)</sup>

Anyways, this is the final code, as of me writing (typing? I dunno) this file for the GitHub Repo that I'm probably gonna make when the universe starts cooling down:

```py
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

# Clears the screen. This one is a late comment lmao
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
```
**oooooooooooooooh, shit ton of code** yes, Timmy, I know. The code above can do the following:

- Change the color of the cursor (or brush)
- Easter egg, I **love** those, but I am just milking this KONO DIO DA stuff
- Raise and Lower the cursor (or the brush, **again**), enabling or disabling the "drawing" feature at will
- Draw, of course

Then, I found [this video](https://youtu.be/HRKQlEfEMCA) and decided: *Yeah, I'm gonna need a new file just to see if this thing fucking works or not* and it did. Here is the code:

```py
import turtle

# Create and set customizations for both the turtle and the screen
cursor = turtle.Turtle()
cursor.speed(-1)
screen = turtle.Screen()
screen.title("Arrow Paint V3 by Kiwifruit")

# Defining functions for this app
def dragging(x, y):
    cursor.ondrag(None)
    cursor.setheading(cursor.towards(x, y))
    cursor.goto(x, y)
    cursor.ondrag(dragging)

def clear():
    cursor.clear()

def run():
    turtle.listen()

    cursor.ondrag(dragging)
    turtle.onkey(clear, "x")

    screen.mainloop()

# Calling All functions at once
run()
```
**Note: I have *yet* to add the other features of V2, so stay there (also, who the hell am I talking to? You are reading this file on GitHub, which means it is *already* done, but let's give my logic some sugar for now)**

Pretty short, right? I know, it was kinda weird at first as to why this was all it, but hey, I'm happy (I think). Anyways, back to coding so that these features are gonna be implemented

Kiwi from like, 20-30 minutes later, it's done! Yay
Here's the code:
```py
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
```

I just copied the code from `main.py` and just pasted in there, tweaked it a 'lil, and **BOOM**, profit.

Ending? Yes, Karlson, **ending**
--------------------------------
Tbh, it feels great that I was able to condense my 98-line Python script
into 44 lines with just adding the ability to drag. Maybe next time, I should add settings and filesaving, still kinda dunno how that stuff works tho...

Wow...I have overdone myself. [My firt repo's documentation](https://github.com/Kiwifuit/TaskRunner) was only 176 lines long

Anyways, have a nice day!