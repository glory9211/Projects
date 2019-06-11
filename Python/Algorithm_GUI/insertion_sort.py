import turtle


class Disc(turtle.Turtle):
    """Disc object build with turtle.Turtle"""

    def __init__(self, n, canvas):
        turtle.RawTurtle.__init__(self, canvas, shape="square", visible=False)
        self.size = n
        self.pu()
        self.shapesize(n * 1.05, 1.5, 2)  # square-->rectangle
        self.fillcolor("black")
        self.st()

    def glow(self):
        self.fillcolor("red")

    def pivot(self):
        self.fillcolor("green")

    def dull(self):
        self.fillcolor("grey")

    def unglow(self):
        self.fillcolor("black")

    def __repr__(self):
        return "Block size: {0}".format(self.size)


class Writer(turtle.Turtle):
    """Turtle Object to write on screen"""

    def __init__(self, canvas):
        turtle.RawTurtle.__init__(self, canvas, shape="square", visible=False)
        self.shapesize(1, 1, 1)
        self.ht()

    def show_text(self, text):
        self.goto(0, -250)
        self.write(text, align="center", font=("Courier", 16, "bold"))


class Shelf(list):
    """Container For Discs"""

    def __init__(self, y):
        self.y = y
        self.x = -150

# clear, setup, autorun

    def close_gap(self, i):
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos - 34)

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


class SortShelf:
    """Shelf Extension For applying Sorts"""

    def __init__(self, canvas, handler, *values):
        self.canvas = canvas
        self.shelf = Shelf(-200)
        self.values = values
        self.editor = handler
        self.writer = Writer(self.canvas)

    def clear_shelf(self):
        del self.shelf[:]

    def formatcode(self):
        self.editor.config_tag(0, 'white', 'red')
        self.editor.config_tag(1, 'grey', 'yellow')
        self.editor.config_tag(2, 'black', 'white')
        self.editor.config_tag(3, 'grey', 'yellow')
        self.editor.config_tag(4, 'black', 'white')
        self.editor.config_tag(5, 'white', 'green')

    def setup(self, al):
        self.clear_shelf()
        self.editor.tag_reset()
        self.editor.tagged_insert(al)
        self.formatcode()
        self.writer.show_text(al)
        for i in self.values:
            self.shelf.push(Disc(i, self.canvas))

    def isort(self):
        # self.editor.config_tag(0, 'white', 'red')
        # self.writer.show_text('Insertion Sort')
        length = len(self.shelf)
        # sleep(2.5)
        # self.editor.tag_reset(0)
        for i in range(1, length):
            hole = i
            # self.editor.config_tag(1, 'white', 'red')
            while hole > 0 and self.shelf[i].size < self.shelf[hole - 1].size:
                hole = hole - 1
            # self.editor.config_tag(2, 'white', 'red')
            self.shelf.insert(hole, self.shelf.pop(i))
