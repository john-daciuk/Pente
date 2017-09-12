from graphics import *
from math import *


class PenteBoard:

    def __init__(self, win):

        self.win = win
        self.wsquares = [0] * 100
        self.bsquares = [0] * 100

        r = Rectangle(Point(10, 10), Point(110, 110))
        r.setWidth(2)
        r.draw(win)
        for i in range(10):
            vline = Line(Point(20 + 10*i, 10), Point(20 + 10*i, 110))
            vline.draw(win)
            hline = Line(Point(10, 20 + 10*i), Point(110, 20 + 10*i))
            hline.draw(win)

    def board_clicked(self, p):
        if 10 < p.getX() < 110 and 10 < p.getY() < 110:
            return True

    def sqaure_clicked(self, p, color, move):
        for i in range(0, 10):
            for j in range(0, 10):
                sq_num = 10 * i + j
                if 10 * (i + 1) < p.getX() < 10 * (i + 2) and 10 * (j + 1) < p.getY() < 10 * (j + 2):

                    if color == 'black' and self.wsquares[sq_num] == 0 and self.bsquares[sq_num] == 0:
                        self.bsquares[sq_num] = move
                    if color == 'white' and self.bsquares[sq_num] == 0 and self.wsquares[sq_num] == 0:
                        self.wsquares[sq_num] = move
                    return sq_num

    def refresh(self):

        for i in range(100):
            if self.wsquares[i] != 0:
                cx = int(i / 10) * 10 + 15
                cy = (i % 10) * 10 + 15
                cpoint = Point(cx, cy)
                circ = Circle(cpoint, 4)
                circ.setFill('white')
                circ.draw(self.win)

        for i in range(100):
            if self.bsquares[i] != 0:
                cx = int(i / 10) * 10 + 15
                cy = (i % 10) * 10 + 15
                cpoint = Point(cx, cy)
                circ = Circle(cpoint, 4)
                circ.setFill('black')
                circ.draw(self.win)

    def connect5(self):

        for i in range(100):

            if i + 36 < 100:
                if self.wsquares[i] != 0 and self.wsquares[i + 9] != 0 and self.wsquares[i + 18] != 0 and self.wsquares[i + 27] != 0 and self.wsquares[i + 36] != 0:
                    return 'white wins'
            if i + 44 < 100:
                if self.wsquares[i] != 0 and self.wsquares[i + 11] != 0 and self.wsquares[i + 22] != 0 and self.wsquares[i + 33] != 0 and self.wsquares[i + 44] != 0:
                    return 'white wins'
            if i + 4 < 100:
                if self.wsquares[i] != 0 and self.wsquares[i + 1] != 0 and self.wsquares[i + 2] != 0 and self.wsquares[i + 3] != 0 and self.wsquares[i + 4] != 0:
                    return 'white wins'
            if i + 40 < 100:
                if self.wsquares[i] != 0 and self.wsquares[i + 10] != 0 and self.wsquares[i + 20] != 0 and self.wsquares[i + 30] != 0 and self.wsquares[i + 40] != 0:
                    return 'white wins'
            if i + 36 < 100:
                if self.bsquares[i] != 0 and self.bsquares[i + 9] != 0 and self.bsquares[i + 18] != 0 and self.bsquares[i + 27] != 0 and self.bsquares[i + 36] != 0:
                    return 'black wins'
            if i + 44 < 100:
                if self.bsquares[i] != 0 and self.bsquares[i + 11] != 0 and self.bsquares[i + 22] != 0 and self.bsquares[i + 33] != 0 and self.bsquares[i + 44] != 0:
                    return 'black wins'
            if i + 4 < 100:
                if self.bsquares[i] != 0 and self.bsquares[i + 1] != 0 and self.bsquares[i + 2] != 0 and self.bsquares[i + 3] != 0 and self.bsquares[i + 4] != 0:
                    return 'black wins'
            if i + 40 < 100:
                if self.bsquares[i] != 0 and self.bsquares[i + 10] != 0 and self.bsquares[i + 20] != 0 and self.bsquares[i + 30] != 0 and self.bsquares[i + 40] != 0:
                    return 'black wins'

    def capture(self, move, background):

        for i in range(100):

            if i - 9 > -1 and i + 18 < 100:
                if self.wsquares[i] != 0 and self.wsquares[i + 9] != 0:
                    if self.bsquares[i - 9] != 0 and self.bsquares[i + 18] != 0:
                        if self.bsquares[i - 9] == move or self.bsquares[i + 18] == move:
                            self.wsquares[i] = 0
                            self.wsquares[i + 9] = 0
                            cx = int(i / 10) * 10 + 15
                            cy = (i % 10) * 10 + 15
                            cpoint = Point(cx, cy)
                            circ = Circle(cpoint, 4.3)
                            circ.setFill(background)
                            circ.setOutline(background)
                            circ.draw(self.win)
                            cx = int((i + 9) / 10) * 10 + 15
                            cy = ((i + 9) % 10) * 10 + 15
                            cpoint = Point(cx, cy)
                            circ = Circle(cpoint, 4.3)
                            circ.setFill(background)
                            circ.setOutline(background)
                            circ.draw(self.win)
                            return 'black captures'

            if i - 11 > -1 and i + 22 < 100:
                if self.wsquares[i] != 0 and self.wsquares[i + 11] != 0:
                    if self.bsquares[i - 11] != 0 and self.bsquares[i + 22] != 0:
                        if self.bsquares[i - 11] == move or self.bsquares[i + 22] == move:
                            self.wsquares[i] = 0
                            self.wsquares[i + 11] = 0
                            cx = int(i / 10) * 10 + 15
                            cy = (i % 10) * 10 + 15
                            cpoint = Point(cx, cy)
                            circ = Circle(cpoint, 4.3)
                            circ.setFill(background)
                            circ.setOutline(background)
                            circ.draw(self.win)
                            cx = int((i + 11) / 10) * 10 + 15
                            cy = ((i + 11) % 10) * 10 + 15
                            cpoint = Point(cx, cy)
                            circ = Circle(cpoint, 4.3)
                            circ.setFill(background)
                            circ.setOutline(background)
                            circ.draw(self.win)
                            return 'black captures'

            if i - 9 > -1 and i + 18 < 100:
                if self.bsquares[i] != 0 and self.bsquares[i + 9] != 0:
                    if self.wsquares[i - 9] != 0 and self.wsquares[i + 18] != 0:
                        if self.wsquares[i - 9] == move or self.wsquares[i + 18] == move:
                            self.bsquares[i] = 0
                            self.bsquares[i + 9] = 0
                            cx = int(i / 10) * 10 + 15
                            cy = (i % 10) * 10 + 15
                            cpoint = Point(cx, cy)
                            circ = Circle(cpoint, 4.3)
                            circ.setFill(background)
                            circ.setOutline(background)
                            circ.draw(self.win)
                            cx = int((i + 9) / 10) * 10 + 15
                            cy = ((i + 9) % 10) * 10 + 15
                            cpoint = Point(cx, cy)
                            circ = Circle(cpoint, 4.3)
                            circ.setFill(background)
                            circ.setOutline(background)
                            circ.draw(self.win)
                            return 'white captures'

            if i - 11 > -1 and i + 22 < 100:
                if self.bsquares[i] != 0 and self.bsquares[i + 11] != 0:
                    if self.wsquares[i - 11] != 0 and self.wsquares[i + 22] != 0:
                        if self.wsquares[i - 11] == move or self.wsquares[i + 22] == move:
                            self.bsquares[i] = 0
                            self.bsquares[i + 11] = 0
                            cx = int(i / 10) * 10 + 15
                            cy = (i % 10) * 10 + 15
                            cpoint = Point(cx, cy)
                            circ = Circle(cpoint, 4.3)
                            circ.setFill(background)
                            circ.setOutline(background)
                            circ.draw(self.win)
                            cx = int((i + 11) / 10) * 10 + 15
                            cy = ((i + 11) % 10) * 10 + 15
                            cpoint = Point(cx, cy)
                            circ = Circle(cpoint, 4.3)
                            circ.setFill(background)
                            circ.setOutline(background)
                            circ.draw(self.win)
                            return 'white captures'

            if i - 10 > -1 and i + 20 < 100:
                if self.wsquares[i] != 0 and self.wsquares[i + 10] != 0:
                    if self.bsquares[i - 10] != 0 and self.bsquares[i + 20] != 0:
                        if self.bsquares[i - 10] == move or self.bsquares[i + 20] == move:
                            self.wsquares[i] = 0
                            self.wsquares[i + 10] = 0
                            cx = int(i / 10) * 10 + 15
                            cy = (i % 10) * 10 + 15
                            cpoint = Point(cx, cy)
                            circ = Circle(cpoint, 4.3)
                            circ.setFill(background)
                            circ.setOutline(background)
                            circ.draw(self.win)
                            cx = int((i + 10) / 10) * 10 + 15
                            cy = ((i + 10) % 10) * 10 + 15
                            cpoint = Point(cx, cy)
                            circ = Circle(cpoint, 4.3)
                            circ.setFill(background)
                            circ.setOutline(background)
                            circ.draw(self.win)
                            return 'black captures'

            if i - 1 > -1 and i + 2 < 100:
                if self.wsquares[i] != 0 and self.wsquares[i + 1] != 0:
                    if self.bsquares[i - 1] != 0 and self.bsquares[i + 2] != 0:
                        if self.bsquares[i - 1] == move or self.bsquares[i + 2] == move:
                            self.wsquares[i] = 0
                            self.wsquares[i + 1] = 0
                            cx = int(i / 10) * 10 + 15
                            cy = (i % 10) * 10 + 15
                            cpoint = Point(cx, cy)
                            circ = Circle(cpoint, 4.3)
                            circ.setFill(background)
                            circ.setOutline(background)
                            circ.draw(self.win)
                            cx = int((i + 1) / 10) * 10 + 15
                            cy = ((i + 1) % 10) * 10 + 15
                            cpoint = Point(cx, cy)
                            circ = Circle(cpoint, 4.3)
                            circ.setFill(background)
                            circ.setOutline(background)
                            circ.draw(self.win)
                            return 'black captures'

            if i - 10 > -1 and i + 20 < 100:
                if self.bsquares[i] != 0 and self.bsquares[i + 10] != 0:
                    if self.wsquares[i - 10] != 0 and self.wsquares[i + 20] != 0:
                        if self.wsquares[i - 10] == move or self.wsquares[i + 20] == move:
                            self.bsquares[i] = 0
                            self.bsquares[i + 10] = 0
                            cx = int(i / 10) * 10 + 15
                            cy = (i % 10) * 10 + 15
                            cpoint = Point(cx, cy)
                            circ = Circle(cpoint, 4.3)
                            circ.setFill(background)
                            circ.setOutline(background)
                            circ.draw(self.win)
                            cx = int((i + 10) / 10) * 10 + 15
                            cy = ((i + 10) % 10) * 10 + 15
                            cpoint = Point(cx, cy)
                            circ = Circle(cpoint, 4.3)
                            circ.setFill(background)
                            circ.setOutline(background)
                            circ.draw(self.win)
                            return 'white captures'

            if i - 1 > -1 and i + 2 < 100:
                if self.bsquares[i] != 0 and self.bsquares[i + 1] != 0:
                    if self.wsquares[i - 1] != 0 and self.wsquares[i + 2] != 0:
                        if self.wsquares[i - 1] == move or self.wsquares[i + 2] == move:
                            self.bsquares[i] = 0
                            self.bsquares[i + 1] = 0
                            cx = int(i / 10) * 10 + 15
                            cy = (i % 10) * 10 + 15
                            cpoint = Point(cx, cy)
                            circ = Circle(cpoint, 4.3)
                            circ.setFill(background)
                            circ.setOutline(background)
                            circ.draw(self.win)
                            cx = int((i + 1) / 10) * 10 + 15
                            cy = ((i + 1) % 10) * 10 + 15
                            cpoint = Point(cx, cy)
                            circ = Circle(cpoint, 4.3)
                            circ.setFill(background)
                            circ.setOutline(background)
                            circ.draw(self.win)
                            return 'white captures'
