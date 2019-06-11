import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk, filedialog
from tkinter import messagebox as tmb
import os

PROGRAM_NAME = 'Footprint Editor'
FILE_NAME = None
CHANGED_TEXT = None
root = tk.Tk()
root.title(PROGRAM_NAME)

# Adding the Menu Bar

menu_bar = tk.Menu(root)

# File Menu


def new_file(event=None):
    root.title('Untitled')
    global FILE_NAME
    FILE_NAME = None
    on_content_changed()
    content_text.delete('1.0', 'end')


def open_file(event=None):
    input_filename = filedialog.askopenfilename(
        defaultextension='.txt',
        filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
    if input_filename:
        global FILE_NAME, CHANGED_TEXT
        FILE_NAME = input_filename
        root.title('{} - {}'.format(os.path.basename(FILE_NAME), PROGRAM_NAME))
        content_text.delete('1.0', 'end')
        with open(FILE_NAME) as _file:
            content_text.insert('1.0', _file.read())
    on_content_changed()
    CHANGED_TEXT = None


def save(event=None):
    global FILE_NAME, CHANGED_TEXT
    if not FILE_NAME:
        save_as()
    else:
        write_to_file(FILE_NAME)
    CHANGED_TEXT = None
    return 'break'


def save_as(event=None):
    input_filename = filedialog.asksaveasfilename(
        defaultextension='.txt',
        filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
    if input_filename:
        global FILE_NAME, CHANGED_TEXT
        FILE_NAME = input_filename
        write_to_file(FILE_NAME)
        root.title('{} - {}'.format(os.path.basename(FILE_NAME), PROGRAM_NAME))
    CHANGED_TEXT = None
    return 'break'


def write_to_file(file_name):
    try:
        content = content_text.get(1.0, 'end')
        with open(file_name, 'w') as the_file:
            the_file.write(content)
    except IOError:
        pass


def exit_editor(event=None):
    global CHANGED_TEXT
    if CHANGED_TEXT:
        dummy = 'Do you want to save the changes\nbefore leaving'
        if tmb.askyesno('Unsaved Changes', dummy):
            save()
    root.destroy()


root.protocol('WM_DELETE_WINDOW', exit_editor)  # Binding the root exit

file_menu = tk.Menu(menu_bar, tearoff=0)
file_dic = {'New': ('Ctrl+N', new_file), 'Open': ('Ctrl+O', open_file),
            'Save': ('Ctrl+S', save), 'Save As': ('Shift+Ctrl+S', save_as),
            'Exit': ('Alt+F4', exit_editor)}
file_sep = ['Save As']
for item in file_dic:
    file_menu.add_command(
        label=item, accelerator=file_dic[item][0], compound=tk.LEFT,
        underline=0, command=file_dic[item][1])
    if (item in file_sep):
        file_menu.add_separator()
menu_bar.add_cascade(label='File', menu=file_menu)

# Edit Menu


def cut():
    on_content_changed()
    content_text.event_generate("<<Cut>>")


def copy():
    on_content_changed()
    content_text.event_generate("<<Copy>>")


def paste():
    on_content_changed()
    content_text.event_generate("<<Paste>>")


def undo():
    on_content_changed()
    content_text.event_generate("<<Undo>>")


def redo(event=None):
    on_content_changed()
    content_text.event_generate("<<Redo>>")

    return 'break'


def select_all(event=None):
    content_text.tag_add('sel', '1.0', 'end')
    return 'break'


def find_text(event=None):
    search_var = tk.StringVar()
    ignore_var = tk.BooleanVar()

    def search_command():  # type lambda the auto-pep8
        return search_output(search_var.get(), ignore_var.get(),
                             content_text, search_toplevel, search_entry)
    # Finding position for windows to appear
    pos_x = int(root.winfo_width() / 2 + root.winfo_x())
    pos_y = int(root.winfo_height() / 2 + root.winfo_y())
    # Creating the Find windows
    search_toplevel = tk.Toplevel(root)
    search_toplevel.title('Find Text')
    search_toplevel.transient(root)  # to keep this above on root
    search_toplevel.resizable(False, False)
    search_toplevel.geometry('+{}+{}'.format(pos_x, pos_y))
    # widgets in the window
    tk.Label(search_toplevel, text='Find: ').grid(row=0, column=0, sticky=tk.W)
    search_entry = ttk.Entry(search_toplevel, width=25,
                             textvariable=search_var)
    search_entry.grid(row=0, column=1, padx=2, pady=2, sticky=tk.EW)
    search_entry.focus()
    # search_entry.grab_set() #direct all events to this one i.e makes modal
    ttk.Button(search_toplevel, text='Find All',
               command=search_command).grid(row=0, column=2, padx=2, pady=2)
    tk.Checkbutton(search_toplevel, text='Ignore Case',
                   variable=ignore_var).grid(row=2, column=1, sticky=tk.W)
    # overriding the default closing process to remove tags

    def close_search():
        content_text.tag_remove('match', '1.0', 'end')
        search_toplevel.destroy()
        return 'break'
    search_toplevel.protocol('WM_DELETE_WINDOW', close_search)


def search_output(pattern, if_ignore_case, content_text,
                  search_toplevel, search_entry):
    content_text.tag_remove('match', '1.0', 'end')
    matches_found = 0
    if pattern:
        start_pos = '1.0'
        while True:
            start_pos = content_text.search(
                pattern, start_pos, nocase=if_ignore_case, stopindex='end')
            if not start_pos:
                break
            end_pos = '{}+{}c'.format(start_pos, len(pattern))
            content_text.tag_add('match', start_pos, end_pos)
            matches_found += 1
            start_pos = end_pos
        content_text.tag_config('match', foreground='red', background='yellow')
    search_entry.focus_set()
    search_toplevel.title('{} matches found'.format(matches_found))


edit_dic = {'Undo': ('Ctrl+Z', undo), 'Redo': ('Ctrl+Y', redo),
            'Cut': ('Ctrl+X', cut), 'Copy': ('Ctrl+C', copy),
            'Paste': ('Ctrl+V', paste), 'Find': ('Ctrl+F', find_text),
            'Select All': ('Ctrl+A', select_all)}
edit_sep = ['Redo', 'Paste', 'Find']

edit_menu = tk.Menu(menu_bar, tearoff=0)
for item in edit_dic:
    edit_menu.add_command(
        label=item, accelerator=edit_dic[item][0], command=edit_dic[item][1],
        compound=tk.LEFT, underline=0)
    if (item in edit_sep):
        edit_menu.add_separator()
menu_bar.add_cascade(label='Edit', menu=edit_menu)

# View Menu
show_line = tk.BooleanVar()
show_cursor = tk.BooleanVar()
highlight_line_var = tk.BooleanVar()
theme_var = tk.StringVar()

view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='View', menu=view_menu)
view_menu.add_checkbutton(label='Show Line Number', variable=show_line)


themes_menu = tk.Menu(view_menu, tearoff=0)  # Themes Sub-Menu
themes_dic = {'Aquamarine': '#5B8340.#D1E7E0',
              'Bold Beige': '#4B4620.#FFF0E1',
              'Cobalt Blue': '#ffffBB.#3333aa',
              'Default': '#000000.#FFFFFF',
              'Greygarious': '#83406A.#D1D4D1',
              'Night Mode': '#FFFFFF.#000000',
              'Olive Green': '#D1E7E0.#5B8340'}
# Gave values for variable argument use


# About Menu
def about_messagebox():
    dummy = "\nTkinter GUI Application\nDevelopment Blueprints"
    tmb.showinfo('About', '{} {}'.format(PROGRAM_NAME, dummy))


def help_messagebox(event=None):
    dummy = "\nTkinter GUI Application\nDevelopment Blueprints"
    tmb.showinfo('Help', 'Help Book: {}'.format(dummy), icon='question')


about_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='About', menu=about_menu)
about_menu.add_command(label='About', command=about_messagebox)
about_menu.add_command(label='Help', command=help_messagebox)

# End Menu Bar

# Shortcut Icons Frame
icons = ('new_file', 'open_file', 'save', 'cut',
         'copy', 'paste', 'undo', 'redo', 'find_text')
shortcut_bar = tk.Frame(root, height=25, background='light sea green')
shortcut_bar.pack(fill=tk.X, expand='no')
for icon in icons:
    toolbar_icon = tk.PhotoImage(
        file=os.path.join('icons', '{}.gif'.format(icon)),)
    cmd = eval(icon)
    toolbar = tk.Button(shortcut_bar, background='light sea green',
                        border=0, image=toolbar_icon, command=cmd)
    toolbar.image = toolbar_icon
    toolbar.pack(side='left', padx=2, pady=2)

# Line Number Bar


def on_content_changed(event=None):
    toggle_highlight()
    update_line_numbers()
    update_cursor_info()


def get_line_numbers():  # return string as 1\n2\n3\n4\n...........
    output = ''
    if show_line.get():
        row, col = content_text.index('end').split('.')
        for i in range(1, int(row)):
            output += str(i) + '\n'
    return output


def update_line_numbers():
    line_numbers = get_line_numbers()
    line_number_bar.config(state='normal')
    line_number_bar.delete('1.0', 'end')
    line_number_bar.insert('1.0', line_numbers)
    line_number_bar.config(state='disabled')
    pos_cursor_linebar = content_text.index(tk.INSERT)
    line_number_bar.see(pos_cursor_linebar)


line_number_bar = tk.Text(root, width=4, padx=3, takefocus=0,
                          border=0, background='khaki', state='disabled',
                          wrap='none')
line_number_bar.pack(fill=tk.Y, side='left')
line_number_bar.yview(tk.END)

root.config(menu=menu_bar)  # show Menu Bar

# Main Text Widget

# content_text = tk.Text(root, wrap='word')
# content_text.pack(fill=tk.BOTH, expand='yes')
# scroll_bar = tk.Scrollbar(content_text)
# content_text.configure(yscrollcommand=scroll_bar.set)
# scroll_bar.configure(command=content_text.yview)
# scroll_bar.pack(side='right', fill=tk.Y)


def change_in_text(event=None):
    global CHANGED_TEXT
    CHANGED_TEXT = True


def highlight_line():
    content_text.tag_remove('active_line', '1.0', 'end')
    content_text.tag_add(
        'active_line', 'insert linestart', 'insert lineend+1c')
    content_text.after(100, toggle_highlight)


def undo_highlight():
    content_text.tag_remove('active_line', '1.0', 'end')


def toggle_highlight():

    if highlight_line_var.get():
        highlight_line()
    else:
        undo_highlight()


content_text = scrolledtext.ScrolledText(root, wrap='word', undo=True)
content_text.tag_config('active_line', background='ivory2')
content_text.pack(expand='yes', fill=tk.BOTH)
content_text.bind('<Control-Y>', redo)  # Binding with Y
content_text.bind('<Control-y>', redo)  # Binding with y
content_text.bind('<Control-a>', select_all)  # Binding with a
content_text.bind('<Control-A>', select_all)  # Binding with A
content_text.bind('<Control-f>', find_text)  # Binding with f
content_text.bind('<Control-F>', find_text)  # Binding with F
content_text.bind('<Control-n>', new_file)  # Binding with n
content_text.bind('<Control-N>', new_file)  # Binding with N
content_text.bind('<Control-o>', open_file)  # Binding with o
content_text.bind('<Control-O>', open_file)  # Binding with O
content_text.bind('<Control-s>', save)  # Binding with s
content_text.bind('<Control-S>', save)  # Binding with S
content_text.bind('<Shift Control-s>', save_as)  # Binding with s
content_text.bind('<Shift Control-S>', save_as)  # Binding with S
content_text.bind('<KeyPress-F1>', help_messagebox)  # Binding with F1
content_text.bind('<Alt F4>', exit_editor)  # Binding with Alt+F4
content_text.bind('<<Modified>>', change_in_text)  # only change in text area
content_text.bind('<Key>', on_content_changed)  # special + char

# THINGS WITH ERRORS
view_menu.add_checkbutton(
    label='Highlight Current Line', variable=highlight_line_var,
    command=toggle_highlight)

# Cursor Info Bar


def show_cursor_info():
    if show_cursor.get():
        cursor_info_bar.pack(side=tk.RIGHT, anchor=tk.SE)
    else:
        cursor_info_bar.pack_forget()


def update_cursor_info(event=None):
    row, col = content_text.index(tk.INSERT).split('.')
    cursor_info_bar.config(text='Line: {} | Column: {}'.format(row, col))


cursor_info_bar = tk.Label(
    content_text, text='Line: 1 | Column: 1', background='white')
cursor_info_bar.pack(side=tk.RIGHT, anchor=tk.SE)


view_menu.add_checkbutton(
    label='Show Cursor Location at Bottom', variable=show_cursor,
    command=show_cursor_info)

# Themes Setting UP


def change_theme():
    theme_choice = theme_var.get()
    fg_bg_colors = themes_dic.get(theme_choice)
    fg_color, bg_color = fg_bg_colors.split('.')
    content_text.config(foreground=fg_color, background=bg_color)


for item in themes_dic:
    themes_menu.add_radiobutton(
        label=item, variable=theme_var, command=change_theme)
view_menu.add_cascade(label='Themes', menu=themes_menu)

# Setting defaults
show_cursor.set(True)
highlight_line_var.set(True)
show_line.set(True)
theme_var.set('Default')
# Program Starts
content_text.focus()
root.mainloop()
