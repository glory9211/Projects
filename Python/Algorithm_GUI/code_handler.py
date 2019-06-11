import tkinter as tk
import os

# Change the FOLDER variable for another directory
CURRENT_DIRECTORY = os.path.dirname(__file__)
FOLDER = 'Pseudo'


class CodeFormat:

    """Pass the tkinter text widget for perfroming
    insertion/configuration of text"""

    def __init__(self, widget):
        self.code_window = widget

    def read_file(self, filename):
        file = os.path.join(CURRENT_DIRECTORY, FOLDER, filename)
        with open(file) as f:
            data = f.read()
        return data.split('\n')

    def insert_data(self, pseudo):
        for n, string in enumerate(pseudo, 0):
            self.code_window.insert(tk.END, string, 'line{}'.format(n))
            self.code_window.insert(tk.END, '\n\n', 'line{}'.format(n))
            self.code_window.insert(tk.END, '\n')

    def tagged_insert(self, al):
        self.delete_text()
        if al == 'Tower of Hanoi':
            pseudo = self.read_file('hanoi.txt')
            self.insert_data(pseudo)
        if al == 'Insertion Sort':
            pseudo = self.read_file('insertion.txt')
            self.insert_data(pseudo)
        if al == 'Selection Sort':
            pseudo = self.read_file('selection.txt')
            self.insert_data(pseudo)
        if al == 'Quick Sort':
            pseudo = self.read_file('quick.txt')
            self.insert_data(pseudo)

    def config_tag(self, n, bg, fg):
        labelfont = ('helvetica', 10)
        self.code_window.tag_config('line{}'.format(
            n), background=bg, foreground=fg, font=labelfont)

    def tag_reset(self):
        for tag in self.code_window.tag_names():
            self.code_window.tag_delete(tag)

    def delete_text(self):
        self.code_window.delete('1.0', tk.END)
