import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

# Main_frame

win = tk.Tk()
win.title("Python GUI")


# Mighty_Python

mighty = tk.LabelFrame(win, text='Mighty_Python')
mighty.grid(column=0, row=0, padx=5, pady=5)

# Name

ttk.Label(mighty, text='Enter a name:').grid(column=0, row=0, sticky=tk.W)
nameVar = tk.StringVar()
Box_Name = ttk.Entry(mighty, width=12, textvariable=nameVar)
Box_Name.grid(column=0, row=1, sticky=tk.W)

# Number

ttk.Label(mighty, text='Choose a number:').grid(column=1, row=0)
numberVar = tk.StringVar()
Box_Number = ttk.Combobox(
    mighty, width=12, textvariable=numberVar, state='readonly')
Box_Number['values'] = [i for i in range(10)]
Box_Number.current(0)
Box_Number.grid(column=1, row=1)

# Button


def click_me():

    B1.configure(text='clicked')


B1 = ttk.Button(mighty, text='click me', command=click_me)
B1.grid(column='2', row='1')

# Check_Box

checkVar = []
state = ['disabled', 'normal', 'active']
textList = ['Disabled', 'Unckecked', 'Enabled']

for cur in range(3):
    checkVar.append(tk.IntVar())            # need for more than one variable
    curCheck = tk.Checkbutton(
        mighty, text=textList[cur], variable=checkVar[cur], state=state[cur])
    optList = [curCheck.select, curCheck.deselect, curCheck.select]
    optList[cur]()
    curCheck.grid(column=cur, row=3, sticky=tk.W)

# Radio_Button
color = ['Blue', 'Gold', 'Red']
radVar = tk.IntVar()           # no need for more than one variable
radVar.set(99)


def rad_call():
    radValue = radVar.get()
    if radValue == 0:
        win.configure(background=color[0])
    elif radValue == 1:
        win.configure(background=color[1])
    elif radValue == 2:
        win.configure(background=color[2])


for cur in range(3):
    curRad = tk.Radiobutton(
        mighty, text=color[cur], variable=radVar, value=cur, command=rad_call)
    curRad.grid(column=cur, row=4, sticky=tk.W)

# Scrolled_text

Box_Scrolled = scrolledtext.ScrolledText(
    mighty, width=30, height=3, wrap=tk.WORD)
Box_Scrolled.grid(column=0, columnspan=3)

# Button Frame

button_frame = ttk.Labelframe(mighty, text='Labels in a frame')
button_frame.grid(column=0, row=7, padx=20, pady=20)

for label in range(3):
    ttk.Label(button_frame, text="Label_{}".format(label)
              ).grid(column=0, row=label, padx=5, pady=5)

for child in button_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Menu Bar

menu_bar = Menu(win)
win.config(menu=menu_bar)

# Exit


def _quit():
    win.quit()
    win.destroy()
    exit()

# File Menu


file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=_quit)
menu_bar.add_cascade(label='File', menu=file_menu)

# Help Menu

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label='About')
help_menu.add_separator()
help_menu.add_command(label='Info')
menu_bar.add_cascade(label='Help', menu=help_menu)

# Run

Box_Name.focus()
win.mainloop()
