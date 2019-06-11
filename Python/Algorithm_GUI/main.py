import tkinter as tk
from hanoi import Tower_of_Hanoi
from insertion_sort import SortShelf
from tkinter import ttk
from mergesort import MergeShelf
from selectionsort import SSortShelf
from quicksort import QSortShelf
from code_handler import CodeFormat
from HardHandler import Hardcore
import os


class App():

    """
    Main App runner Class
    (still under development) --> Merge Sort, Pause Button
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Project DSA")
        # For fixed size win
        # self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.create_code_window()
        self.create_canvas()
        # self.create_control_options()
        self.create_buttons()
        self.create_option_window()

    def create_code_window(self):
        self.code_window = tk.Text(
            self.root, wrap=tk.WORD, width=40)
        self.code_window.grid(column=0, row=1, sticky=(
            'n', 'w', 'e', 's'), rowspan=2)
        

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, width=700, height=630)
        self.canvas.grid(column=1, row=1, sticky=(
            'n', 'w', 'e', 's'), columnspan=2)
        

    def create_algorithm_combobox(self):
        tk.Label(self.Option_Frame, text='Select Algorithm:').grid(
            column=0, row=0, padx=10, pady=3)
        self.algorithm_widget = ttk.Combobox(
            self.Option_Frame, state='readonly')
        self.algorithm_widget['values'] = ('Tower of Hanoi', 'Insertion Sort',
                                           'Selection Sort', 'Quick Sort')
        self.algorithm_widget.current(0)
        self.algorithm_widget.grid(column=1, row=0, padx=5, pady=6)

    def create_case_combobox(self):
        self.case_label = tk.Label(
            self.Option_Frame, text='Select Case:')
        self.case_label.grid(column=2, row=0, padx=10, pady=3)
        self.case_widget = ttk.Combobox(
            self.Option_Frame, state='readonly')
        self.case_widget['values'] = (
            'Best Case', 'Average Case', 'Worst Case')
        self.case_widget.current(1)
        self.case_widget.grid(column=3, row=0, padx=5, pady=6)

    def hanoi_case_manager(self, event=None):
        # Show hide hanoi Disk and Case Combobox
        if self.algorithm_widget.get() == 'Tower of Hanoi':
            self.case_widget.grid_remove()
            self.case_label.grid_remove()
            self.hanoi_label.grid()
            self.disk_widget.grid()
        else:
            self.disk_widget.grid_remove()
            self.hanoi_label.grid_remove()
            self.case_widget.grid()
            self.case_label.grid()

    def hanoi_disks(self):
        self.hanoi_label = tk.Label(
            self.Option_Frame, text='Hanoi Discs:')
        self.hanoi_label.grid(column=4, row=0, padx=10, pady=3)
        self.disk_widget = ttk.Combobox(
            self.Option_Frame, state='readonly')
        self.disk_widget['values'] = [i + 1 for i in range(6)]
        self.disk_widget.current(4)
        # self.disk_widget.current('Normal')
        self.disk_widget.grid(column=5, row=0, padx=5, pady=6)

    def ModeSet(self):
        if self.v.get() == 1:  # Noob Mode
            self.algorithm_widget['values'] = (
                'Tower of Hanoi', 'Insertion Sort',
                'Selection Sort', 'Quick Sort')
            self.case_widget.config(state='readonly')
            self.disk_widget.config(state='readonly')
            # does not matters if exists or not as variables name will be
            # overwritten and latest will show

        if self.v.get() == 2:  # Hardcore Mode
            self.algorithm_widget['values'] = ('Bubble Sort', 'Heap Sort',
                                               'Insertion Sort 2',
                                               'Merge Sort', 'Quick Sort 2',
                                               'Radix Sort', 'Bucket Sort',
                                               'Selection Sort 2')
            self.case_widget.config(state='disabled')
            self.disk_widget.config(state='disabled')

        if self.v.get() == 3:  # Larceny Mode
            self.algorithm_widget['values'] = 'Kruskal'
            self.case_widget.config(state='disabled')
            self.disk_widget.config(state='disabled')

        self.algorithm_widget.current(0)
        self.case_widget.current(1)  # Average Case while disabled
        self.hanoi_case_manager()

    def create_radiobuttons(self):
        # Simple codes, Pygame codes, Attachment codes
        self.v = tk.IntVar()
        ttk.Radiobutton(
            self.Option_Frame, text='Noob Mode', variable=self.v, value=1,
            command=self.ModeSet).grid(column=7, row=0, padx=10, pady=3)
        ttk.Radiobutton(
            self.Option_Frame, text='Hardcore Mode', variable=self.v, value=2,
            command=self.ModeSet).grid(column=8, row=0, padx=10, pady=3)
        ttk.Radiobutton(
            self.Option_Frame, text='Larceny Mode', variable=self.v, value=3,
            command=self.ModeSet).grid(column=9, row=0, padx=10, pady=3)
        self.v.set(1)
        # preset and creation completed

    def create_option_window(self):
        self.Option_Frame = tk.LabelFrame(self.root)
        self.Option_Frame.grid(
            column=0, row=2, columnspan=3, sticky=('n', 'w', 's', 'e'))
        self.create_algorithm_combobox()
        self.create_case_combobox()
        self.hanoi_disks()
        self.create_radiobuttons()
        self.algorithm_widget.bind(
            "<<ComboboxSelected>>", self.hanoi_case_manager)
        self.hanoi_case_manager()
        

    def create_buttons(self):
        self.button_Label = tk.LabelFrame(self.root, text="Control Menu")
        self.run_button = ttk.Button(self.button_Label, text="Run",
                                     command=self.auto_run, width=50)
        self.run_button.grid(
            column=0, row=1, padx=10, pady=2)
        ttk.Button(self.button_Label, text="Pause",
                   command=self.pause, width=50).grid(
            column=1, row=1, padx=10, pady=2)
        ttk.Button(self.button_Label, text="Reset",
                   command=self.reset_canvas, width=50).grid(
            column=2, row=1, padx=10, pady=2)
        self.button_Label.grid(
            column=0, row=3, columnspan=3,
            sticky=('n', 'w', 'e', 's'), padx=20)

    def value_case(self):
        case = self.case_widget.get()
        if case == 'Best Case':
            return (1, 2, 3, 4, 5, 6, 7, 8, 9)
        if case == 'Average Case':
            return (4, 2, 8, 1, 5, 3, 7, 6, 9)
        if case == 'Worst Case':
            return (9, 8, 7, 6, 5, 4, 3, 2, 1)

    def hanoi_run(self, al):
        discs = int(self.disk_widget.get())
        self.tower = Tower_of_Hanoi(discs, self.handler, self.canvas)
        self.clear_canvas()
        self.tower.setup(al)
        self.tower.auto_run_hanoi()

    def isort_run(self, al):
        values = self.value_case()
        shelf = SortShelf(self.canvas, self.handler, *values)
        self.clear_canvas()
        shelf.setup(al)
        shelf.isort()

    def merge_run(self):  # still in development
        values = self.value_case()
        shelf = MergeShelf(self.canvas, *values)
        self.clear_canvas()
        shelf.setup()
        shelf.mergeSort(shelf.shelf)

    def selection_run(self, al):
        values = self.value_case()
        shelf = SSortShelf(self.canvas, self.handler, *values)
        self.clear_canvas()
        shelf.setup(al)
        shelf.ssort()

    def quick_run(self, al):
        values = self.value_case()
        shelf = QSortShelf(self.canvas, self.handler, *values)
        self.clear_canvas()
        shelf.setup(al)
        shelf.qsort(shelf.shelf, 0, len(values) - 1)

    def auto_run(self):  # make run button disabled
        """Function responsible for Run button"""
        self.run_button.config(state='disabled')
        algorithm = self.algorithm_widget.get()
        self.handler = CodeFormat(self.code_window)
        _Hardcore = Hardcore()
        if algorithm == 'Tower of Hanoi':
            self.hanoi_run(algorithm)
        if algorithm == 'Insertion Sort':
            self.isort_run(algorithm)
        if algorithm == 'Quick Sort':
            self.quick_run(algorithm)
        if algorithm == 'Selection Sort':
            self.selection_run(algorithm)
        if algorithm == 'Kruskal':
            os.system('processing-java --sketch="A:\\Code\\Learn\\Project" --run')
            # Wriet the cmd command for the code to RUn

        else:
            _Hardcore.openwindow(algorithm)
        self.run_button.config(state='normal')

    def pause(self):  # still in development
        pass

    def clear_canvas(self):
        self.canvas.delete("all")
        

    def reset_canvas(self, event=None):  # Button for reset
        # clean canvas, button state, code window
        self.clear_canvas()
        self.run_button.config(state='normal')
        self.code_window.delete(1.0, tk.END)
        # self.tower.clear_tree()
        # self.tower.setup()


if __name__ == '__main__':
    try:
        
        root = tk.Tk()
        ex = App(root)
        root.mainloop()
    except Exception as E:
        print(E)
