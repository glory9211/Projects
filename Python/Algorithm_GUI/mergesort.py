import turtle
from time import sleep
"""
Still Under Development
"""

class Disc(turtle.Turtle):
    def __init__(self, n, canvas):
        turtle.RawTurtle.__init__(self, canvas, shape="square", visible=False)
        self.size = n
        self.pu()
        self.shapesize(n * 1.05, 1.5, 2)  # square-->rectangle
        self.fillcolor("black")
        self.st()

    def glow(self):
        self.fillcolor("red")

    def unglow(self):
        self.fillcolor("black")

    def __repr__(self):
        return "Block size: {0}".format(self.size)


class Shelf(list):
    def __init__(self, y, x=-150):
        self.y = y
        self.x = x

# clear, setup, autorun

    def move_x(self, i):
        for b in self:
            xpos, _ = b.pos()
            print(b, xpos)
            b.setx(xpos + i)

    def open_gap(self, i):
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos + 34)

    def push(self, d):
        width, _, _ = d.shapesize()  # assigning using tuple
        # align blocks by the bottom edge
        y_offset = width / 2 * 20
        d.sety(self.y + y_offset)
        d.setx(self.x + 34 * len(self))
        self.append(d)

    def pop(self, key):
        # pop works with key
        b = list.pop(self, key)
        b.glow()
        b.sety(200)
        self.close_gap(key)
        return b

    def insert(self, key, b):
        self.open_gap(key)
        list.insert(self, key, b)
        b.setx(self.x + 34 * key)
        width, _, _ = b.shapesize()
        # align blocks by the bottom edge
        y_offset = width / 2 * 20
        b.sety(self.y + y_offset)
        b.unglow()


class MergeShelf:
    def __init__(self, canvas, *values):
        self.canvas = canvas
        self.shelf = Shelf(-200)
        self.values = values

    def clear_shelf(self):
        del self.shelf[:]

    def setup(self):
        self.clear_shelf()
        for i in self.values:
            self.shelf.push(Disc(i, self.canvas))

    def lmergeSort(self, _shelf, n=0):
        if len(_shelf) > 1:
            mid = len(_shelf) // 2
            # lefthalf = _shelf[:mid]
            new_x, _ = _shelf[mid].pos()
            lefthalf = Shelf(_shelf.y, int(new_x - 150 + 25 * n))
            for x in _shelf[:mid]:
                lefthalf.push(x)
                sleep(0.1 + n / 2)
            print(lefthalf, n)
            n += 1
            self.lmergeSort(lefthalf, n)
        if len(_shelf) == 1:
            # copying not refrencing
            lefthalf = _shelf[:]
        return lefthalf

    def rmergeSort(self, _shelf, n=0):
        if len(_shelf) > 1:
            mid = len(_shelf) // 2
            # lefthalf = _shelf[:mid]
            new_x, _ = _shelf[mid].pos()
            print(new_x)
            righthalf = Shelf(_shelf.y, int(new_x+40))
            for x in _shelf[mid:]:
                righthalf.push(x)
                sleep(0.1 + n % 2)
            print(righthalf, n)
            n += 1
            self.rmergeSort(righthalf, n)
        if len(_shelf) == 1:
            # copying not refrencing
            righthalf = _shelf[:]
        return righthalf

    def mergeSort(self, _shelf, n=0, m=0):
        print("Splitting ", _shelf)
        # lefthalf = self.lmergeSort(_shelf, n)
        # print("Splitting ", _shelf)
        # righthalf = self.rmergeSort(_shelf, n)

        if len(_shelf) > 1:
            mid = len(_shelf) // 2
            # lefthalf = _shelf[:mid]
            new_x, _ = _shelf[mid].pos()
            lefthalf = Shelf(_shelf.y, int(new_x - 150 + 25 * n))
            for x in _shelf[:mid]:
                lefthalf.push(x)
                sleep(0.1 + n / 2)
            print(lefthalf, n)
            n += 1
            self.mergeSort(lefthalf, n)
            righthalf = Shelf(_shelf.y, int(new_x + 40))
            for x in _shelf[mid:]:
                righthalf.push(x)
                sleep(0.1 + m % 2)
            print(righthalf, m)
            m += 1
            self.mergeSort(righthalf, m)

            # i = 0
            # j = 0
            # k = 0

            # while i < len(lefthalf) and j < len(righthalf):
            #     if lefthalf[i].size < righthalf[j].size:
            #         _shelf[k] = lefthalf[i]
            #         i = i + 1
            #     else:
            #         _shelf[k] = righthalf[j]
            #         j = j + 1
            #     k = k + 1

            # while i < len(lefthalf):
            #     _shelf[k] = lefthalf[i]
            #     i = i + 1
            #     k = k + 1
            # while j < len(righthalf):
            #     _shelf[k] = righthalf[j]
            #     j = j + 1
            #     k = k + 1
        print("Merging ", _shelf)
