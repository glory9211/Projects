import os

# Change the FOLDER variable for another directory
CURRENT_DIRECTORY = os.path.dirname(__file__)
FOLDER = 'Hardcore'


class Hardcore:

    """ Class to execute pygame codes """

    def openwindow(self, al):
        if al == 'Bubble Sort':
            file = os.path.join(CURRENT_DIRECTORY, FOLDER, 'bubble_sort.py')
            os.system('python ' + file)
        if al == 'Heap Sort':
            file = os.path.join(CURRENT_DIRECTORY, FOLDER, 'heap_sort.py')
            os.system('python ' + file)
        if al == 'Insertion Sort 2':
            file = os.path.join(CURRENT_DIRECTORY, FOLDER, 'insertion_sort.py')
            os.system('python ' + file)
        if al == 'Merge Sort':
            file = os.path.join(CURRENT_DIRECTORY, FOLDER, 'merge_sort.py')
            os.system('python ' + file)
        if al == 'Quick Sort 2':
            file = os.path.join(CURRENT_DIRECTORY, FOLDER, 'quick_sort.py')
            os.system('python ' + file)
        if al == 'Radix Sort':
            file = os.path.join(CURRENT_DIRECTORY, FOLDER, 'radix_sort.py')
            os.system('python ' + file)
        if al == 'Bucket Sort':
            file = os.path.join(CURRENT_DIRECTORY, FOLDER, 'bucket_sort.py')
            os.system('python ' + file)
        if al == 'Selection Sort 2':
            file = os.path.join(CURRENT_DIRECTORY, FOLDER, 'selection_sort.py')
            os.system('python ' + file)

