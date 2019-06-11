import tkinter as tk
from tkinter import ttk, scrolledtext

DEFAULT_TABLE_LIMIT = 10
PROGRAM_NAME = 'Multiplication Table'
DEMO_TABLE_VALUE= 43

class MultiplicationTable():

    def __init__(self, root):
        self.root = root
        self.table_limit = DEFAULT_TABLE_LIMIT
        self.root.title(PROGRAM_NAME)
        self.entry_number = tk.IntVar()
        self.entry_number.set(DEMO_TABLE_VALUE)
        self.init_gui()
        self.root.mainloop()

    def init_gui(self):
        self.create_display()
        self.create_limit_spinbox()
        self.create_value_entry()
        self.create_enter_button()
        self.entry_value_changed()

    def create_enter_button(self):
        ttk.Button(self.root, text='Generate',
                   command=self.entry_value_changed).pack(side=tk.LEFT, padx=4, pady=4)

    def create_limit_spinbox(self):
        tk.Label(text='Set table limit').pack(side=tk.LEFT, padx=4, pady=4)
        self.limit_spinbox = tk.Spinbox(
            self.root, from_=10, to=10000, command=self.change_table_limit)
        self.limit_spinbox.pack(side=tk.LEFT, padx=4, pady=4)

    def change_table_limit(self):
        value = int(self.limit_spinbox.get())
        self.table_limit = value if value > 0 else DEFAULT_TABLE_LIMIT

    def create_value_entry(self):
        tk.Label(text='Enter the number').pack(side=tk.LEFT, padx=4, pady=4)
        ttk.Entry(self.root, width=5, textvariable=self.entry_number).pack(side=tk.LEFT, padx=4, pady=4)
        # def entry value change

    def create_display(self):
        self.display_widget = scrolledtext.ScrolledText(
            self.root, background='khaki', foreground='light sea green')
        self.display_widget.pack(side=tk.BOTTOM)

    def data_to_print(self, cursor):
        return self.entry_number.get(), cursor, self.entry_number.get() * cursor

    def entry_value_changed(self):
        if self.entry_number.get() > 0:
            self.display_widget.delete('0.0', tk.END)
            for i in range(self.table_limit):
                self.display_widget.insert(
                    tk.INSERT, '{} X {} = {} \n'.format(*self.data_to_print(i+1)))


root = tk.Tk()
MultiplicationTable(root)
