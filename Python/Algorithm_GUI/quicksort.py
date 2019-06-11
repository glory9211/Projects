from insertion_sort import SortShelf
from time import sleep


class QSortShelf(SortShelf):
    def __init__(self, canvas, *values):
        SortShelf.__init__(self, canvas, *values)

    def swap(self, a, b):
        a_x, a_y = a.pos()
        b_x, b_y = b.pos()
        a.sety(10)
        b.sety(10)
        a.setx(b_x)
        a.sety(a_y)
        b.setx(a_x)
        b.sety(b_y)

    def formatcode(self):
        self.editor.config_tag(0, 'white', 'red')
        self.editor.config_tag(1, 'grey', 'yellow')
        self.editor.config_tag(2, 'black', 'white')
        self.editor.config_tag(3, 'grey', 'yellow')
        self.editor.config_tag(4, 'black', 'white')
        self.editor.config_tag(5, 'grey', 'yellow')
        self.editor.config_tag(6, 'black', 'white')
        self.editor.config_tag(7, 'white', 'green')

    def partition(self, alist, first, last):
        # print("entry", alist)
        pivotvalue = alist[first]
        pivotvalue.pivot()
        leftmark = first + 1
        alist[leftmark].glow()
        rightmark = last
        alist[rightmark].glow()
        # sleep(0.2)

        done = False
        while not done:

            while leftmark <= rightmark and (
                    alist[leftmark].size <= pivotvalue.size):
                # alist[leftmark-1].unglow()
                sleep(0.2)
                # alist[leftmark].glow()
                leftmark = leftmark + 1
                if leftmark < 8:
                    alist[leftmark].glow()
                    alist[leftmark - 1].unglow()
                    sleep(0.2)

            while alist[rightmark].size >= pivotvalue.size and (
                    rightmark >= leftmark):
                sleep(0.2)
                # alist[rightmark].glow()
                rightmark = rightmark - 1
                if rightmark > 0:
                    alist[rightmark].glow()
                    alist[rightmark + 1].unglow()
                    sleep(0.2)

            if rightmark < leftmark:
                done = True
            else:
                self.swap(alist[leftmark], alist[rightmark])
                alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp
        self.swap(alist[first], alist[rightmark])
        # reset code
        # print("exit", alist)
        pivotvalue.dull()

        return rightmark

    def qsort(self, alist, first, last):
        # self.swap(self.shelf[2], self.shelf[4])

        if first < last:

            splitpoint = self.partition(alist, first, last)
            self.qsort(alist, first, splitpoint - 1)
            self.qsort(alist, splitpoint + 1, last)

            for x in alist:
                x.unglow()

        # find place for pivot
