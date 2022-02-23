import wordle
from tkinter import *
from ttkthemes import themed_tk as tk
import pyglet
import keyboard
import math

# Made by Pratham Mehta

word = ""

grey = "#787c7e"
green = "#6aaa64"
yellow = "#c9b458"

i = 0

combination = ""


wordle = wordle.Wordle()

wordle.reset()
wordle.read()

pyglet.font.add_file('Inter.ttf')

window = tk.ThemedTk()
window.get_themes()
window.set_theme("black")
window.geometry("1200x700")
window.configure(bg = "#FFFFFF")
window.title("Wordle")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

one = Entry(window, highlightthickness=1, bd = 0, font=("Inter ExtraLight", 30 * -1), justify = "center")

one.place(
    x = 210.0,
    y = 90.0,
    width = 65.0,
    height = 65.0
)

one.config(highlightbackground = grey)

two = Entry(window, highlightthickness=1, bd = 0, font=("Inter ExtraLight", 30 * -1), justify = "center")

two.place(
    x = 301.0,
    y = 90.0,
    width = 65.0,
    height = 65.0
)

two.config(highlightbackground = grey)

three = Entry(window, highlightthickness=1, bd = 0, font=("Inter ExtraLight", 30 * -1), justify = "center")

three.place(
    x = 392.0,
    y = 90.0,
    width = 65.0,
    height = 65.0
)

three.config(highlightbackground = grey)

four = Entry(window, highlightthickness=1, bd = 0, font=("Inter ExtraLight", 30 * -1), justify = "center")

four.place(
    x = 483.0,
    y = 90.0,
    width = 65.0,
    height = 65.0
)

four.config(highlightbackground = grey)

five = Entry(window, highlightthickness=1, bd = 0, font=("Inter ExtraLight", 30 * -1), justify = "center")

five.place(
    x = 574.0,
    y = 90.0,
    width = 65.0,
    height = 65.0
)

five.config(highlightbackground = grey)

six = Entry(window, highlightthickness=1, bd = 0, font=("Inter ExtraLight", 30 * -1), justify = "center")

six.place(
    x = 665.0,
    y = 90.0,
    width = 65.0,
    height = 65.0
)

six.config(highlightbackground = grey)

credit = Text(window, highlightthickness=1, bd = 0, font=("Inter ExtraLight", 30 * -1))

credit.place(
    x=505,
    y=545,
    width=225,
    height=65
)

credit.config(highlightbackground = grey)

credit.tag_configure('tag-center', justify='center')

credit.insert(END, "Pratham M.", 'tag-center')

T = Text(window, highlightthickness=1, bd = 0, font=("Inter ExtraLight", 30 * -1))

T.place(
    x=770,
    y=90,
    width=343,
    height=520
)

T.config(highlightbackground = grey)

oneBits = Text(window, highlightthickness=1, bd = 0, font=("Inter ExtraLight", 30 * -1))

oneBits.place(x=88, y=90, width=82, height=65)

oneBits.config(highlightbackground = grey)

oneBits.tag_configure('tag-center', justify='center')

total = Text(window, highlightthickness=1, bd = 0, font=("Inter ExtraLight", 30 * -1))

total.place(x=88, y=545, width=148, height=65)

total.config(highlightbackground = grey)

total.tag_configure('tag-center', justify='center')

total.insert(END, round(math.log(len(wordle.words), 2),2), 'tag-center')

widgets = [one, two, three, four, five, six]

focus = 0

def color(e):
    one.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")
    two.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")
    three.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")
    four.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")
    five.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")
    six.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")
    
    six.bind("<n>", none)
    six.bind("<y>", yellow)
    six.bind("<g>", green)

    if i == 5:
        return 0

def focus(i):
    widgets[i].focus_set()

six.bind("<Return>", color)

one.bind("<space>", lambda event, i = 1: focus(i))
two.bind("<space>", lambda event, i = 2: focus(i))
three.bind("<space>", lambda event, i = 3: focus(i))
four.bind("<space>", lambda event, i = 4: focus(i))
five.bind("<space>", lambda event, i = 5: focus(i))

one.focus_set()

def unbindAll():
    six.unbind("<g>")
    six.unbind("<y>")
    six.unbind("<n>")
    six.bind("<Return>", check)

def clear():
    global i, combination
    
    one.config(state = "normal")
    two.config(state = "normal")
    three.config(state = "normal")
    four.config(state = "normal")
    five.config(state = "normal")
    six.config(state = "normal")

    one.delete(0, END)
    two.delete(0, END)
    three.delete(0, END)
    four.delete(0, END)
    five.delete(0, END)
    six.delete(0, END)

    six.bind("<Return>", color)

    i = 0
    combination = ""
    
def none(e):
    global widgets, i, six, combination

    combination += "n"

    if i != 5:
        widgets[i].config(disabledbackground = grey)

    else:
        widgets[i].config(disabledbackground = grey)
        unbindAll()

    i = i + 1

def yellow(e):
    global widgets, i, six, combination

    combination += "y"

    if i != 5:
        widgets[i].config(disabledbackground = "#c9b458")

    else:
        widgets[i].config(disabledbackground = "#c9b458")
        unbindAll()

    i = i + 1

def green(e):
    global widgets, i, six, combination

    combination += "g"

    if i != 5:
        widgets[i].config(disabledbackground = "#6aaa64")

    else:
        widgets[i].config(disabledbackground = "#6aaa64")
        unbindAll()

    i = i + 1

def check(e):
    global word, combination, wordle
    
    word = one.get() + two.get() + three.get() + four.get() + five.get() + six.get()
    word = word.replace(" ", "")

    six.unbind("<Return>")

    wordsLength = len(wordle.words)

    entered = word
    outcome = combination
    
    wordle.combinations = [outcome]
    wordle.analyze(entered, True)

    posLength = len(wordle.possibilities)
    
    wordle.words = wordle.possibilities
    wordle.possibilities = []
    wordle.combinations = []

    with open("combinations.txt") as f:
        contents = f.read().splitlines() 
        wordle.combinations.append(contents)

    wordle.combinations = wordle.combinations.pop()

    wordle.freq = {}

    for word in wordle.words:
        wordle.analyze(word, False)

    T.delete('1.0', END)
    oneBits.delete('1.0', END)

    try:
        oneBits.insert(END, round(math.log(wordsLength, 2) - math.log(posLength, 2), 2), 'tag-center')

    except:
        pass

    prev = float(total.get("1.0","end").strip())
    total.delete('1.0', END)
    total.insert(END, round(prev - float(oneBits.get("1.0","end").strip()), 2), 'tag-center')

    for word in wordle.top():
        T.insert(END, word + " - " + str(round(wordle.freq.get(word), 2)) + "\n")

    clear()

window.resizable(False, False)
window.mainloop()
