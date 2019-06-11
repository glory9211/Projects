import tkinter as tk
from tkinter import ttk, scrolledtext
import calendar
from calendar import TextCalendar
import datetime

APP_NAME = 'CALENDER APP'
MONTH_LIST = [calendar.month_name[i]
              for i in range(1, 13)]
YEAR_LIST = [i for i in range(1911, 2118)]
NOW = datetime.datetime.now()
CURRENT_MONTH = NOW.month
CURRENT_YEAR = NOW.year


class CalendarApp():

    def __init__(self, root):
        self.root = root
        self.root.title(APP_NAME)
        self.instance = TextCalendar()
        self.root.resizable(False, False)
        self.init_gui()
        self.update_display()
        self.root.mainloop()

    def init_gui(self):
        self.create_year_combobox()
        self.create_month_combobox()
        self.create_display()

    def create_year_combobox(self):
        tk.Label(self.root, text='Select Year').grid(column=0, row=0)
        self.year_widget = ttk.Combobox(
            self.root, state='readonly')
        self.year_widget['values'] = YEAR_LIST
        self.year_widget.current(YEAR_LIST.index(CURRENT_YEAR))
        self.year_widget.grid(column=1, row=0, padx=5, pady=6)
        self.year_widget.bind("<<ComboboxSelected>>", self.update_display)

    def create_month_combobox(self):
        tk.Label(self.root, text='Select Month').grid(column=2, row=0)
        self.month_widget = ttk.Combobox(
            self.root, state='readonly', )
        self.month_widget['values'] = MONTH_LIST
        self.month_widget.current(CURRENT_MONTH - 1)
        self.month_widget.grid(column=3, row=0, padx=5, pady=6)
        self.month_widget.bind("<<ComboboxSelected>>", self.update_display)

    def create_display(self):
        self.display_widget = scrolledtext.ScrolledText(
            self.root, background='#3c53d1', foreground='#ffffff',
            width=90)
        self.display_widget.grid(column=0, row=2, padx=5, pady=6, columnspan=5)

    def update_display(self, event=None):
        year = int(self.year_widget.get())
        self.display_widget.configure(state='normal')
        self.display_widget.delete('0.0', tk.END)
        self.display_widget.insert('0.0', self.instance.formatyear(year, 2, 2))
        month = self.month_widget.get()
        pos = self.display_widget.search(month, '0.0')
        self.add_tag(month, pos)
        self.display_widget.see(pos)
        self.display_widget.configure(state='disabled')

    def add_tag(self, month, start_pos):
        end_pos = '{}+{}c'.format(start_pos, len(month))
        self.display_widget.tag_add('active', start_pos, end_pos)
        self.display_widget.tag_config(
            'active', foreground='red', background='yellow')
        self.add_space()

    def add_space(self):
        def hack(start_pos):
            a = start_pos.split('.')
            a[1] = str(int(a[1]) - 1)
            a[0] = str(int(a[0]) + 1)
            return '.'.join(a)

        start_pos = '1.0'
        while True:
            start_pos = self.display_widget.search(
                '\n', start_pos, stopindex='end')
            if not start_pos:
                break
            end_pos = '{}+{}c'.format(start_pos, 2)
            i_value = hack(start_pos)
            self.display_widget.insert(i_value, '\t')
            start_pos = end_pos


root = tk.Tk()

CalendarApp(root)