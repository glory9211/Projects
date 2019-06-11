import tkinter as tk


root = tk.Tk()

frame = tk.Frame(root)

tk.Label(frame, text="Pack demo of side and fill").pack()
tk.Button(frame, text="A").pack(side=tk.LEFT, fill=tk.Y)
tk.Button(frame, text="B").pack(side=tk.TOP, fill=tk.X)
tk.Button(frame, text="C").pack(side=tk.RIGHT, fill=tk.NONE)
tk.Button(frame, text="D").pack(side=tk.BOTTOM, fill=tk.BOTH)
frame.pack()
tk.Label(root, text="Pack demo of expand").pack()
tk.Button(root, text="I donot expand").pack()
tk.Button(root, text="I donot fill X but I expand").pack(expand=1)
tk.Button(root, text="I fill X and expand").pack(expand=1, fill=tk.X)
tk.Scale(root, label="volume", to=10,).pack()

root.mainloop()
