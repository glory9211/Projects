import tkinter as tk 
from tkinter import ttk
from tkcolorpicker import askcolor

root=tk.Tk()

# a=tk.Entry(root,text='hello',bg='khaki').grid(column=1,row=1)
style = ttk.Style(root)
style.theme_use('clam')

askcolor((255,255,0),root,'Pick Color')




root.mainloop()