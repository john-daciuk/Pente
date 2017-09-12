from graphics import *
from PenteButton import *

def setupwin():
    win = GraphWin('Pente!', 850, 850)
    win.setCoords(0, 0, 120, 125)
    background = 'seashell'
    win.setBackground(background)
    return win, background


def determine(board, bc, wc):
    if bc == 5:
        winner = 'Black'
        game_over = True
        reason = 'Black made 5 captures'
        return winner, game_over, reason
    elif wc == 5:
        winner = 'White'
        game_over = True
        reason = 'White made 5 captures'
        return winner, game_over, reason
    elif board.connect5() == 'white wins':
        winner = 'White'
        game_over = True
        reason = 'White connected 5'
        return winner, game_over, reason
    elif board.connect5() == 'black wins':
        winner = 'Black'
        game_over = True
        reason = 'Black connected 5'
        return winner, game_over, reason
    else:
        return 'not_over'

def results(winner, reason, win):
    m1 = Text(Point(60, 117), '{} WINS!  {}'.format(winner.upper(), reason.upper()))
    m1.setSize(18)
    rect = Rectangle(Point(20, 114), Point(100, 120))
    m1.setFace('courier')
    m1.setTextColor('grey3')
    rect.draw(win)
    m1.draw(win)

def main():
    win, background = setupwin()
    board = PenteBoard(win)
    bcaptures = 0
    wcaptures = 0
    move = 0
    game_over = False


    while game_over == False:

        move += 1
        while True:
            p = win.getMouse()
            if board.board_clicked(p):
                if board.bsquares[board.sqaure_clicked(p, 'black', move)] == move:
                    break

        if board.capture(move, background) == 'black captures':
            bcaptures += 1
            center = Point(5, -5 + bcaptures * 20)
            circ = Circle(center, 3)
            circ.setFill('white')
            circ.draw(win)
            circ = Circle(Point(center.getX(), center.getY() + 10), 3)
            circ.setFill('white')
            circ.draw(win)
        board.refresh()



        if determine(board, bcaptures, wcaptures) != 'not_over':
            winner, game_over, reason = determine(board, bcaptures, wcaptures)
            break

        move += 1
        while True:
            p = win.getMouse()
            if board.board_clicked(p):
                if board.wsquares[board.sqaure_clicked(p, 'white', move)] == move:
                    break
        if board.capture(move, background) == 'white captures':
            wcaptures += 1
            center = Point(115, -5 + wcaptures * 20)
            circ = Circle(center, 3)
            circ.setFill('black')
            circ.draw(win)
            circ = Circle(Point(center.getX(), center.getY() + 10), 3)
            circ.setFill('black')
            circ.draw(win)
        board.refresh()


        if determine(board, bcaptures, wcaptures) != 'not_over':
            winner, game_over, reason = determine(board, bcaptures, wcaptures)

    results(winner, reason, win)
    p = win.getMouse()
    p = win.getMouse()
    win.close()




if __name__ == "__main__": main()
