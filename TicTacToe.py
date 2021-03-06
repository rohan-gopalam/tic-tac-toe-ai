import tkinter
import tkinter.font as font


def postob(i, j):
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    if i == 0 and j == 0:
        b1['text'] = "O"

    if i == 0 and j == 1:
        b2['text'] = "O"

    if i == 0 and j == 2:
        b3['text'] = "O"

    if i == 1 and j == 0:
        b4['text'] = "O"

    if i == 1 and j == 1:
        b5['text'] = "O"

    if i == 1 and j == 2:
        b6['text'] = "O"

    if i == 2 and j == 0:
        b7['text'] = "O"

    if i == 2 and j == 1:
        b8['text'] = "O"

    if i == 2 and j == 2:
        b9['text'] = "O"


def minimax(arr, isMax):
    bestScore = 0
    bestMoveO = [0, 0]
    bestMoveX = [0, 0]
    scoreVal = {"X": -1, "O": 1, "TIE": 0}

    vals = checkWin(arr)
    win = vals[0]
    winner = vals[1]

    if win:
        score = scoreVal.get(winner)
        if isMax:
            bestScore = -2
            if bestScore <= score:
                bestScore = score
            return bestScore,
        else:
            score = scoreVal.get(winner)
            bestScore = 2
            if bestScore >= score:
                bestScore = score
            return bestScore,

    if not win:

        if isMax:
            bestScore = -2
            for i in range(3):
                for j in range(3):
                    if arr[i][j] == "":
                        arr[i][j] = "O"
                        findNextBest = minimax(arr, False)
                        arr[i][j] = ""
                        if findNextBest[0] > bestScore:
                            bestScore = findNextBest[0]

            return bestScore,

        else:
            bestScore = 2
            for i in range(3):
                for j in range(3):
                    if arr[i][j] == "":
                        arr[i][j] = "X"
                        findNextBest = minimax(arr, True)
                        arr[i][j] = ""
                        if findNextBest[0] < bestScore:
                            bestScore = findNextBest[0]

            return bestScore,


def aimove():
    scenario = positions

    bestScore = -2
    bestMoveO = [0, 0]
    for i in range(3):
        for j in range(3):
            if scenario[i][j] == "":
                scenario[i][j] = "O"
                findNextBest = minimax(scenario, False)
                scenario[i][j] = ""
                if findNextBest[0] > bestScore:
                    bestScore = findNextBest[0]
                    bestMoveO = [i, j]
    positions[bestMoveO[0]][bestMoveO[1]] = "O"
    postob(bestMoveO[0], bestMoveO[1])


def buttonclick(b, i, j):
    global positions
    vals = checkWin(positions)
    win = vals[0]
    if not win:
        if positions[i][j] == "":
            b['text'] = "X"
            positions[i][j] = "X"
            checker = checkWin(positions)
            if not checker[0]:
                aimove()
    valsTwo = checkWin(positions)
    winTwo = valsTwo[0]
    winnerTwo = valsTwo[1]
    if winTwo:
        print(winnerTwo + " wins")


def resetclick():
    for i in range(3):
        for j in range(3):
            positions[i][j] = ""
    b1['text'] = ""
    b2['text'] = ""
    b3['text'] = ""
    b4['text'] = ""
    b5['text'] = ""
    b6['text'] = ""
    b7['text'] = ""
    b8['text'] = ""
    b9['text'] = ""


def checkWin(pos):
    win = False
    winner = ""

    counter = 0
    for i in range(3):
        for j in range(3):
            if pos[i][j] == "":
                counter += 1
    if counter == 0:
        win = True
        winner = "TIE"

    sides = ["X", "O"]
    for side in sides:
        for i in range(3):
            if (pos[i][0] == side and pos[i][1] == side and pos[i][2] == side) or (
                    pos[0][i] == side and pos[1][i] == side and pos[2][i] == side):
                win = True
                winner = side

        if (pos[0][0] == side and pos[1][1] == side and pos[2][2] == side) or (
                pos[0][2] == side and pos[1][1] == side and pos[2][0] == side):
            win = True
            winner = side

    return win, winner


root = tkinter.Tk()
root.title("AI TicTacToe")
titleLab = tkinter.Label(root, text="Welcome to AI TicTacToe")
titleLab.grid(row=1, column=0)
shapeLab = tkinter.Label(root, text="You are X")
shapeLab.grid(row=2, column=0)

myFont = font.Font(size=10)

rightFrame = tkinter.Frame(root)
rightFrame.grid(row=2, column=0, sticky='n')
resetFrame = tkinter.Frame(root)
resetFrame.grid(row=3, column=0, sticky='n')

positions = [["", "", ""], ["", "", ""], ["", "", ""]]
# positions = [["X", "O", "X"], ["O", "O", ""], ["", "X", ""]]

reset = tkinter.Button(resetFrame, text="reset", padx=20, pady=30, command=lambda: resetclick())
reset.grid(row=1, column=1)

# BUTTON1
b1 = tkinter.Button(rightFrame, text=" ", padx=20, pady=30, command=lambda: buttonclick(b1, 0, 0))
b1.grid(row=0, column=0)

# BUTTON2
b2 = tkinter.Button(rightFrame, text=" ", padx=20, pady=30, command=lambda: buttonclick(b2, 0, 1))
b2.grid(row=0, column=1)

# BUTTON3
b3 = tkinter.Button(rightFrame, text=" ", padx=20, pady=30, command=lambda: buttonclick(b3, 0, 2))
b3.grid(row=0, column=2)

# BUTTON4
b4 = tkinter.Button(rightFrame, text=" ", padx=20, pady=30, command=lambda: buttonclick(b4, 1, 0))
b4.grid(row=1, column=0)

# BUTTON5
b5 = tkinter.Button(rightFrame, text=" ", padx=20, pady=30, command=lambda: buttonclick(b5, 1, 1))
b5.grid(row=1, column=1)

# BUTTON6
b6 = tkinter.Button(rightFrame, text=" ", padx=20, pady=30, command=lambda: buttonclick(b6, 1, 2))
b6.grid(row=1, column=2)

# BUTTON7
b7 = tkinter.Button(rightFrame, text=" ", padx=20, pady=30, command=lambda: buttonclick(b7, 2, 0))
b7.grid(row=2, column=0)

# BUTTON8

b8 = tkinter.Button(rightFrame, text=" ", padx=20, pady=30, command=lambda: buttonclick(b8, 2, 1))
b8.grid(row=2, column=1)

# BUTTON9

b9 = tkinter.Button(rightFrame, text=" ", padx=20, pady=30, command=lambda: buttonclick(b9, 2, 2))
b9.grid(row=2, column=2)

root.mainloop()

# button_text = tkinter.StringVar()
# button = tkinter.Button(root, textvariable=button_text, command=update_button_text)
# button_text.set("a")
##

# BUTTON1


print(positions)
