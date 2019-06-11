import sqlite3
import tkinter as tk
from tkinter import ttk

APP_NAME = 'LOGIN MODEL'


class Login():

    def __init__(self, root):
        self.root = root
        self.root.title(APP_NAME)
        self.gui_init()

    def gui_init(self):
        self.create_username()
        self.create_password()
        self.create_login_button()
        self.create_user_button()
        # self.create_success()
        # self.create_faile()

    def create_username(self):
        self.username_var = tk.StringVar()
        tk.Label(self.root, text='Username',).grid(
            row=0, column=0, padx=5, pady=3)
        ttk.Entry(self.root, textvariable=self.username_var).grid(
            row=0, column=1, padx=5, pady=3)
        # self.username_var.trace('w', self.create_success)

    def create_password(self):
        tk.Label(self.root, text='Password',).grid(
            row=1, column=0, padx=5, pady=3)
        self.password_widget = ttk.Entry(self.root, show='*').grid(
            row=1, column=1, padx=5, pady=3)

    def create_login_button(self):
        ttk.Button(self.root, text='Login', command=None).grid(
            row=2, column=0, padx=5, pady=3)

    def create_user_button(self):
        ttk.Button(self.root, text='Create User', command=None).grid(
            row=2, column=1, padx=5, pady=3)

    def create_success(self, *args):
        # tk.Label(self.root, text=self.username_var.get()).grid(row=3, column=2)
        # if in database show success
        pass
    def create_faile(self):
    	# if not in database print failed
    	pass
    	

if __name__ == '__main__':
    root = tk.Tk()
    Login(root)
    root.mainloop()
