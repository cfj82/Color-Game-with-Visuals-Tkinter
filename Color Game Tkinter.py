# Color Game

from tkinter import *
import random

root = Tk()
root.title("Color Game")
root.configure(width=300, height=250,)
root.geometry("350x350")

color_bank = ["YELLOW", "ORANGE", "BLUE", "GREEN", "RED", "BLACK", "PURPLE"]
time = 30
score = 0


def start(event):
    global time
    if time == 30:
        count_dwn()
    color()

def count_dwn():
    global time
    if time > 0:
        time = time - 1
        time_lbl.config(text="Time Left:" + str(time))  # set label output
        time_lbl.after(1000, count_dwn)  # delay 1 second
    if time == 0:
        time_lbl.config(text="Game Over!")

def color():
    global time
    global score
    if time > 0:
        if enter.get().lower() == color_bank[1].lower():
            score = score + 1
    elif time == 0:
        time_lbl.config("Game Over!")  # set label output

    enter.delete(0, END)  # delete after entry
    random.shuffle(color_bank)  # random choose from list
    score_output.config(text="Score: " + str(score))  # set label output
    color_lbl.config(fg=str(color_bank[0]), text=str(color_bank[1]))  # set label output. different positions in list


# frames
f0 = Frame(root, bg="#000000")
f0.pack(fill="both", expand=True,)
f1 = Frame(root, bg="#000000")
f1.pack(fill="both", expand=True)
f2 = Frame(root, bg="#000000")
f2.pack(fill="both", expand=True)
f3 = Frame(root, bg="#000000")
f3.pack(fill="both", expand=True)


# label for score
score_output = Label(f0, font=("verdana", 17), anchor="center", relief=FLAT, border=15,
                bg="#5DADE2", text="Score: " + str(score))  # label set to always show
score_output.pack(fill="both", expand=True, padx=60, pady=5)

# color label
color_lbl = Label(f1, font=("verdana", 25, "bold"), anchor="center", relief=RAISED, border=15,  # label set in function
                 bg="#EBEDEF", )
color_lbl.pack(fill="both", expand=True, padx=5, pady=5)

# time left label
time_lbl = Label(f2, font=("verdana", 15), anchor="center", relief=FLAT, border=15,
                 bg="#5DADE2", text="Time Left:" + str(time))  # label set to always show
time_lbl.pack(fill="both", expand=True, padx=60, pady=5)

# entry widget
enter = Entry(f3, font=("verdana", 18), relief=SUNKEN, border=15, justify="center",
                 bg="#744697")
enter.pack(fill="both", expand=True, padx=5, pady=5)
enter.bind('<Return>', start)
enter.focus()

# create menu
my_menu = Menu(root)
root.config(menu = my_menu)

# create options dropdown for menu
option_menu = Menu(my_menu, tearoff=False)  # tearoff is dotted line.... ugly
my_menu.add_cascade(label="Options", menu = option_menu)  # create function for menu
option_menu.add_command(label = "Quit", command = root.quit)
# option_menu.add_separator()        # adds line to separate

root.mainloop()
