from insertion_sort import SortShelf


class SSortShelf(SortShelf):
    """ Sort created with Ingeritance of SortShelf"""

    def __init__(self, canvas, handler, *values):
        SortShelf.__init__(self, canvas, handler, *values)

    def formatcode(self):
        self.editor.config_tag(0, 'white', 'red')
        self.editor.config_tag(1, 'grey', 'yellow')
        self.editor.config_tag(2, 'black', 'white')
        self.editor.config_tag(3, 'white', 'green')

    def ssort(self):
        length = len(self.shelf)
        for j in range(0, length - 1):
            imin = j
            for i in range(j + 1, length):
                if self.shelf[i].size < self.shelf[imin].size:
                    imin = i
            if imin != j:
                self.shelf.insert(j, self.shelf.pop(imin))
