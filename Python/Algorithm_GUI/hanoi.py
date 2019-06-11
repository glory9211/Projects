import turtle


class Disc(turtle.Turtle):
    """
    Integrating Turtle demo animations with tkinter
    """
    def __init__(self, n, canvas):
        turtle.RawTurtle.__init__(self, canvas, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n * 1.5, 2)  # square-->rectangle
        self.fillcolor(n / 6., 0, 1 - n / 6.)
        self.st()


class Tower(list):
    # inheriting list for iter, next, del and slicing
    "Hanoi tower, a subclass of built-in type list"

    def __init__(self, x):
        "create an empty tower. x is x-position of peg"
        self.x = x

    def push(self, d):
        d.setx(self.x)
        d.sety(-150 + 34 * len(self))
        self.append(d)

    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d


class Tower_of_Hanoi:

    def __init__(self, no_of_disks, handler, canvas):
        self.n = no_of_disks
        self.canvas = canvas
        self.t1 = Tower(-250)
        self.t2 = Tower(0)
        self.t3 = Tower(250)
        self.editor = handler
        # self.setup()

    def clear_tree(self):
        del self.t1[:]
        del self.t2[:]
        del self.t3[:]

    def formatcode(self):
        self.editor.config_tag(0, 'white', 'red')
        self.editor.config_tag(1, 'grey', 'yellow')
        self.editor.config_tag(2, 'black', 'white')
        self.editor.config_tag(3, 'grey', 'yellow')
        self.editor.config_tag(4, 'black', 'white')
        self.editor.config_tag(5, 'grey', 'yellow')
        self.editor.config_tag(6, 'black', 'white')
        self.editor.config_tag(7, 'white', 'green')
        self.editor.config_tag(8, 'orange', 'white')

    def setup(self, al):
        self.clear_tree()
        self.editor.tag_reset()
        self.editor.tagged_insert(al)
        self.formatcode()
        for i in range(self.n, 0, -1):
            self.t1.push(Disc(i, self.canvas))
        

    def auto_run_hanoi(self):
        self.hanoi(self.n, self.t1, self.t2, self.t3)

    def hanoi(self, n, from_, with_, to_):
        if n > 0:
            self.hanoi(n - 1, from_, to_, with_)
            to_.push(from_.pop())
            self.hanoi(n - 1, with_, from_, to_)
