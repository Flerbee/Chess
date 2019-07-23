
# todo we maaaaaybe need this function so adding it to do for safekeeping
#  if
#  cell[movefile+moverank] == cell[str(chr(ord(x)+1))+y] and cell[str(chr(ord(pickfile)+1))+str(int(pickrank)+1)] == '':
# ignore this code until we make king Checks
# pieceplacementlist = [cell for cell, piece in cell.items() if piece == f"{wrook1}"]
# pieceplacement = pieceplacementlist[0]

from tkinter import *

root = Tk()

wpawnpic = PhotoImage(file='pawnw.png')
wkingpic = PhotoImage(file='kingw.png')
wqueenpic = PhotoImage(file='queenw.png')
wknightpic = PhotoImage(file='knightw.png')
wbishoppic = PhotoImage(file='bishopw.png')
wrookpic = PhotoImage(file='rookw.png')

bpawnpic = PhotoImage(file='pawnb.png')
bkingpic = PhotoImage(file='kingb.png')
bqueenpic = PhotoImage(file='queenb.png')
bknightpic = PhotoImage(file='knightb.png')
bbishoppic = PhotoImage(file='bishopb.png')
brookpic = PhotoImage(file='rookb.png')
# nopic = PhotoImage()


def dog():
    print('i like dogs')


def cat():
    print('cats')


class Chess:
    def chess_board():
        # chessboard = PhotoImage(file='chessboard.png')
        # chessbo = Label(root, image=chessboard)
        # chessbo.photo = chessboard
        # chessbo.pack(side=LEFT)

        A8 = Button(root, image=pp.dicpic[pp.dic_chess['A8']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[7]), dc.squarecheck()])
        A8.place(x=24, y=22)
        B8 = Button(root, image=pp.dicpic[pp.dic_chess['B8']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[7]), dc.squarecheck()])
        B8.place(x=24 + 71, y=22)
        C8 = Button(root, image=pp.dicpic[pp.dic_chess['C8']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[7]), dc.squarecheck()])
        C8.place(x=24 + 71 * 2, y=22)
        D8 = Button(root, image=pp.dicpic[pp.dic_chess['D8']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[7]), dc.squarecheck()])
        D8.place(x=24 + 71 * 3, y=22)
        E8 = Button(root, image=pp.dicpic[pp.dic_chess['E8']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[7]), dc.squarecheck()])
        E8.place(x=24 + 71 * 4, y=22)
        F8 = Button(root, image=pp.dicpic[pp.dic_chess['F8']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[7]), dc.squarecheck()])
        F8.place(x=24 + 71 * 5, y=22)
        G8 = Button(root, image=pp.dicpic[pp.dic_chess['G8']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[7]), dc.squarecheck()])
        G8.place(x=24 + 71 * 6, y=22)
        H8 = Button(root, image=pp.dicpic[pp.dic_chess['H8']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[7]), dc.squarecheck()])
        H8.place(x=24 + 71 * 7, y=22)

        A7 = Button(root, image=pp.dicpic[pp.dic_chess['A7']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[6]), dc.squarecheck()])
        A7.place(x=24, y=22 + 71)
        B7 = Button(root, image=pp.dicpic[pp.dic_chess['B7']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[6]), dc.squarecheck()])
        B7.place(x=24 + 71, y=22 + 71)
        C7 = Button(root, image=pp.dicpic[pp.dic_chess['C7']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[6]), dc.squarecheck()])
        C7.place(x=24 + 71 * 2, y=22 + 71)
        D7 = Button(root, image=pp.dicpic[pp.dic_chess['D7']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[6]), dc.squarecheck()])
        D7.place(x=24 + 71 * 3, y=22 + 71)
        E7 = Button(root, image=pp.dicpic[pp.dic_chess['E7']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[6]), dc.squarecheck()])
        E7.place(x=24 + 71 * 4, y=22 + 71)
        F7 = Button(root, image=pp.dicpic[pp.dic_chess['F7']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[6]), dc.squarecheck()])
        F7.place(x=24 + 71 * 5, y=22 + 71)
        G7 = Button(root, image=pp.dicpic[pp.dic_chess['G7']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[6]), dc.squarecheck()])
        G7.place(x=24 + 71 * 6, y=22 + 71)
        H7 = Button(root, image=pp.dicpic[pp.dic_chess['H7']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[6]), dc.squarecheck()])
        H7.place(x=24 + 71 * 7, y=22 + 71)

        A6 = Button(root, image=pp.dicpic[pp.dic_chess['A6']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[5]), dc.squarecheck()])
        A6.place(x=24, y=22 + 71 * 2)
        B6 = Button(root, image=pp.dicpic[pp.dic_chess['B6']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[5]), dc.squarecheck()])
        B6.place(x=24 + 71, y=22 + 71 * 2)
        C6 = Button(root, image=pp.dicpic[pp.dic_chess['C6']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[5]), dc.squarecheck()])
        C6.place(x=24 + 71 * 2, y=22 + 71 * 2)
        D6 = Button(root, image=pp.dicpic[pp.dic_chess['D6']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[5]), dc.squarecheck()])
        D6.place(x=24 + 71 * 3, y=22 + 71 * 2)
        E6 = Button(root, image=pp.dicpic[pp.dic_chess['E6']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[5]), dc.squarecheck()])
        E6.place(x=24 + 71 * 4, y=22 + 71 * 2)
        F6 = Button(root, image=pp.dicpic[pp.dic_chess['F6']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[5]), dc.squarecheck()])
        F6.place(x=24 + 71 * 5, y=22 + 71 * 2)
        G6 = Button(root, image=pp.dicpic[pp.dic_chess['G6']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[5]), dc.squarecheck()])
        G6.place(x=24 + 71 * 6, y=22 + 71 * 2)
        H6 = Button(root, image=pp.dicpic[pp.dic_chess['H6']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[5]), dc.squarecheck()])
        H6.place(x=24 + 71 * 7, y=22 + 71 * 2)

        A5 = Button(root, image=pp.dicpic[pp.dic_chess['A5']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[4]), dc.squarecheck()])
        A5.place(x=24, y=22 + 71 * 3)
        B5 = Button(root, image=pp.dicpic[pp.dic_chess['B5']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[4]), dc.squarecheck()])
        B5.place(x=24 + 71, y=22 + 71 * 3)
        C5 = Button(root, image=pp.dicpic[pp.dic_chess['C5']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[4]), dc.squarecheck()])
        C5.place(x=24 + 71 * 2, y=22 + 71 * 3)
        D5 = Button(root, image=pp.dicpic[pp.dic_chess['D5']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[4]), dc.squarecheck()])
        D5.place(x=24 + 71 * 3, y=22 + 71 * 3)
        E5 = Button(root, image=pp.dicpic[pp.dic_chess['E5']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[4]), dc.squarecheck()])
        E5.place(x=24 + 71 * 4, y=22 + 71 * 3)
        F5 = Button(root, image=pp.dicpic[pp.dic_chess['F5']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[4]), dc.squarecheck()])
        F5.place(x=24 + 71 * 5, y=22 + 71 * 3)
        G5 = Button(root, image=pp.dicpic[pp.dic_chess['G5']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[4]), dc.squarecheck()])
        G5.place(x=24 + 71 * 6, y=22 + 71 * 3)
        H5 = Button(root, image=pp.dicpic[pp.dic_chess['H5']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[4]), dc.squarecheck()])
        H5.place(x=24 + 71 * 7, y=22 + 71 * 3)

        A4 = Button(root, image=pp.dicpic[pp.dic_chess['A4']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[3]), dc.squarecheck()])
        A4["activebackground"] = 'brown'
        A4.place(x=24, y=22 + 71 * 4)
        B4 = Button(root, image=pp.dicpic[pp.dic_chess['B4']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[3]), dc.squarecheck()])
        B4.place(x=24 + 71, y=22 + 71 * 4)
        C4 = Button(root, image=pp.dicpic[pp.dic_chess['C4']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[3]), dc.squarecheck()])
        C4.place(x=24 + 71 * 2, y=22 + 71 * 4)
        D4 = Button(root, image=pp.dicpic[pp.dic_chess['D4']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[3]), dc.squarecheck()])
        D4.place(x=24 + 71 * 3, y=22 + 71 * 4)
        E4 = Button(root, image=pp.dicpic[pp.dic_chess['E4']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[3]), dc.squarecheck()])
        E4.place(x=24 + 71 * 4, y=22 + 71 * 4)
        F4 = Button(root, image=pp.dicpic[pp.dic_chess['F4']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[3]), dc.squarecheck()])
        F4.place(x=24 + 71 * 5, y=22 + 71 * 4)
        G4 = Button(root, image=pp.dicpic[pp.dic_chess['G4']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[3]), dc.squarecheck()])
        G4.place(x=24 + 71 * 6, y=22 + 71 * 4)
        H4 = Button(root, image=pp.dicpic[pp.dic_chess['H4']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[3]), dc.squarecheck()])
        H4.place(x=24 + 71 * 7, y=22 + 71 * 4)

        A3 = Button(root, image=pp.dicpic[pp.dic_chess['A3']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[2]), dc.squarecheck()])
        A3.place(x=24, y=22 + 71 * 5)
        B3 = Button(root, image=pp.dicpic[pp.dic_chess['B3']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[2]), dc.squarecheck()])
        B3.place(x=24 + 71, y=22 + 71 * 5)
        C3 = Button(root, image=pp.dicpic[pp.dic_chess['C3']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[2]), dc.squarecheck()])
        C3.place(x=24 + 71 * 2, y=22 + 71 * 5)
        D3 = Button(root, image=pp.dicpic[pp.dic_chess['D3']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[2]), dc.squarecheck()])
        D3.place(x=24 + 71 * 3, y=22 + 71 * 5)
        E3 = Button(root, image=pp.dicpic[pp.dic_chess['E3']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[2]), dc.squarecheck()])
        E3.place(x=24 + 71 * 4, y=22 + 71 * 5)
        F3 = Button(root, image=pp.dicpic[pp.dic_chess['F3']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[2]), dc.squarecheck()])
        F3.place(x=24 + 71 * 5, y=22 + 71 * 5)
        G3 = Button(root, image=pp.dicpic[pp.dic_chess['G3']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[2]), dc.squarecheck()])
        G3.place(x=24 + 71 * 6, y=22 + 71 * 5)
        H3 = Button(root, image=pp.dicpic[pp.dic_chess['H3']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[2]), dc.squarecheck()])
        H3.place(x=24 + 71 * 7, y=22 + 71 * 5)

        A2 = Button(root, image=pp.dicpic[pp.dic_chess['A2']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[1]), dc.squarecheck()])
        A2.place(x=24, y=22 + 71 * 6)
        B2 = Button(root, image=pp.dicpic[pp.dic_chess['B2']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[1]), dc.squarecheck()])
        B2.place(x=24 + 71, y=22 + 71 * 6)
        C2 = Button(root, image=pp.dicpic[pp.dic_chess['C2']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[1]), dc.squarecheck()])
        C2.place(x=24 + 71 * 2, y=22 + 71 * 6)
        D2 = Button(root, image=pp.dicpic[pp.dic_chess['D2']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[1]), dc.squarecheck()])
        D2.place(x=24 + 71 * 3, y=22 + 71 * 6)
        E2 = Button(root, image=pp.dicpic[pp.dic_chess['E2']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[1]), dc.squarecheck()])
        E2.place(x=24 + 71 * 4, y=22 + 71 * 6)
        F2 = Button(root, image=pp.dicpic[pp.dic_chess['F2']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[1]), dc.squarecheck()])
        F2.place(x=24 + 71 * 5, y=22 + 71 * 6)
        G2 = Button(root, image=pp.dicpic[pp.dic_chess['G2']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[1]), dc.squarecheck()])
        G2.place(x=24 + 71 * 6, y=22 + 71 * 6)
        H2 = Button(root, image=pp.dicpic[pp.dic_chess['H2']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[1]), dc.squarecheck()])
        H2.place(x=24 + 71 * 7, y=22 + 71 * 6)

        A1 = Button(root, image=pp.dicpic[pp.dic_chess['A1']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[0]), dc.squarecheck()])
        A1.place(x=24, y=22 + 71 * 7)
        B1 = Button(root, image=pp.dicpic[pp.dic_chess['B1']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[0]), dc.squarecheck()])
        B1.place(x=24 + 71, y=22 + 71 * 7)
        C1 = Button(root, image=pp.dicpic[pp.dic_chess['C1']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[0]), dc.squarecheck()])
        C1.place(x=24 + 71 * 2, y=22 + 71 * 7)
        D1 = Button(root, image=pp.dicpic[pp.dic_chess['D1']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[0]), dc.squarecheck()])
        D1.place(x=24 + 71 * 3, y=22 + 71 * 7)
        E1 = Button(root, image=pp.dicpic[pp.dic_chess['E1']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[0]), dc.squarecheck()])
        E1.place(x=24 + 71 * 4, y=22 + 71 * 7)
        F1 = Button(root, image=pp.dicpic[pp.dic_chess['F1']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[0]), dc.squarecheck()])
        F1.place(x=24 + 71 * 5, y=22 + 71 * 7)
        G1 = Button(root, image=pp.dicpic[pp.dic_chess['G1']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[0]), dc.squarecheck()])
        G1.place(x=24 + 71 * 6, y=22 + 71 * 7)
        H1 = Button(root, image=pp.dicpic[pp.dic_chess['H1']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[0]), dc.squarecheck()])
        H1.place(x=24 + 71 * 7, y=22 + 71 * 7)

        fix1 = Frame(root, width=327, height=612, bg='black')
        fix1.place(x=24 + 71 * 8, y=0)
        fix2 = Frame(root, height=21, width=612, bg='black')
        fix2.place(x=24, y=591)

    ##############################################################################


# pickcell = 'placeholder'
#
# movecell = 'placeholder'


##############################################################################


class PiecePosition:
    wrook1 = 'wrook1'
    wrook2 = 'wrook2'
    brook1 = 'brook1'
    brook2 = 'brook2'

    wknight1 = 'wknight1'
    wknight2 = 'wknight2'
    bknight1 = 'bknight1'
    bknight2 = 'bknight2'

    wbishop1 = 'wbishop1'
    wbishop2 = 'wbishop2'
    bbishop1 = 'bbishop1'
    bbishop2 = 'bbishop2'

    wqueen = 'wqueen'
    wking = 'wking'
    bqueen = 'bqueen'
    bking = 'bking'

    wpawn1 = 'wpawn1'
    wpawn2 = 'wpawn2'
    wpawn3 = 'wpawn3'
    wpawn4 = 'wpawn4'
    wpawn5 = 'wpawn5'
    wpawn6 = 'wpawn6'
    wpawn7 = 'wpawn7'
    wpawn8 = 'wpawn8'
    bpawn1 = 'bpawn1'
    bpawn2 = 'bpawn2'
    bpawn3 = 'bpawn3'
    bpawn4 = 'bpawn4'
    bpawn5 = 'bpawn5'
    bpawn6 = 'bpawn6'
    bpawn7 = 'bpawn7'
    bpawn8 = 'bpawn8'
    # dictionary of cells
    dic_chess = {'A1': 'wrook1', 'B1': 'wknight1', 'C1': 'wbishop1', 'D1': 'wqueen', 'E1': 'wking', 'F1': 'wbishop2',
                 'G1': 'wknight2', 'H1': 'wrook2',
                 'A2': 'wpawn1', 'B2': 'wpawn2', 'C2': 'wpawn3', 'D2': 'wpawn4', 'E2': 'wpawn5', 'F2': 'wpawn6',
                 'G2': 'wpawn7',
                 'H2': 'wpawn8',
                 'A3': '', 'B3': '', 'C3': '', 'D3': '', 'E3': '', 'F3': '', 'G3': '', 'H3': '',
                 'A4': '', 'B4': '', 'C4': '', 'D4': 'bbishop1', 'E4': '', 'F4': '', 'G4': '', 'H4': '',
                 'A5': '', 'B5': '', 'C5': '', 'D5': '', 'E5': '', 'F5': '', 'G5': '', 'H5': '',
                 'A6': '', 'B6': '', 'C6': '', 'D6': '', 'E6': '', 'F6': '', 'G6': '', 'H6': '',
                 'A7': 'bpawn1', 'B7': 'bpawn2', 'C7': 'bpawn3', 'D7': 'bpawn4', 'E7': 'bpawn5', 'F7': 'bpawn6',
                 'G7': 'bpawn7', 'H7': 'bpawn8',
                 'A8': 'brook1', 'B8': 'bknight1', 'C8': 'bbishop1', 'D8': 'bqueen', 'E8': 'bking', 'F8': 'bbishop2',
                 'G8': 'bknight2', 'H8': 'brook2'}

    dicpic = {'wrook1': wrookpic, 'wrook2': wrookpic, 'brook1': brookpic, 'brook2': brookpic,
              'wbishop1': wbishoppic, 'wbishop2': wbishoppic, 'bbishop1': bbishoppic, 'bbishop2': bbishoppic,
              'wknight1': wknightpic, 'wknight2': wknightpic, 'bknight1': bknightpic, 'bknight2': bknightpic,
              'wpawn1': wpawnpic, 'wpawn2': wpawnpic, 'wpawn3': wpawnpic, 'wpawn4': wpawnpic,
              'wpawn5': wpawnpic, 'wpawn6': wpawnpic, 'wpawn7': wpawnpic, 'wpawn8': wpawnpic,
              'bpawn1': bpawnpic, 'bpawn2': bpawnpic, 'bpawn3': bpawnpic, 'bpawn4': bpawnpic,
              'bpawn5': bpawnpic, 'bpawn6': bpawnpic, 'bpawn7': bpawnpic, 'bpawn8': bpawnpic,
              'wqueen': wqueenpic, 'bqueen': bqueenpic, 'wking': wkingpic, 'bking': bkingpic, '': None}

    def capture():
        # todo PiecePosition.dic_chess[f'{movecell}'] = sidebar
        PiecePosition.dic_chess[f'{movecell}'] = PiecePosition.dic_chess[f'{pickcell}']
        PiecePosition.dic_chess[f'{pickcell}'] = ''

    def movepiece():
        PiecePosition.dic_chess[f'{movecell}'] = PiecePosition.dic_chess[f'{pickcell}']
        PiecePosition.dic_chess[f'{pickcell}'] = ''


class PieceRules(PiecePosition):

    # rulesets acting on pieces. not the rule set of the game such as draws or checkmates

    def rook():
        rm.whiterookright()
        rm.whiterookleft()
        rm.whiterookdown()
        rm.whiterookup()
    def bishop():
        bm.whitebishopupright()
        bm.whitebishopupleft()
        bm.whitebishopdownright()
        bm.whitebishopdownleft()
    def bishopblack():
        bm.blackbishopupright()
        bm.blackbishopupleft()
        bm.blackbishopdownright()
        bm.blackbishopdownleft()
    # if cell[pickfile+pickrank] == 'wrook1' or cell[pickfile+pickrank] == 'wrook2' or
    def queen():
        qm.whitequeenright()
        qm.whitequeenleft()
        qm.whitequeenupright()
        qm.whitequeendownright()
        qm.whitequeendownleft()
        qm.whitequeenupleft()
        qm.whitequeenup()
        qm.whitequeendown()

    def king():
        km.whitekingright()
        km.whitekingleft()
        km.whitekingupright()
        km.whitekingdownright()
        km.whitekingdownleft()
        km.whitekingupleft()
        km.whitekingup()
        km.whitekingdown()

class ValidKingMovement(PiecePosition):


    possible_king_move = []
    possible_king_capture = []

    def whitekingright():

        x = pickfile
        y = pickrank

        if ord(x) <= 71:
            x = str(chr(ord(x) + 1))
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidKingMovement.possible_king_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidKingMovement.possible_king_capture.append(f'{x}{y}')

            else:
                pass
    def whitekingleft():

        x = pickfile
        y = pickrank

        if ord(x) >= 66:
            x = str(chr(ord(x) - 1))
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidKingMovement.possible_king_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidKingMovement.possible_king_capture.append(f'{x}{y}')

            else:
                pass
    def whitekingup():

        x = pickfile
        y = pickrank

        if int(y) <= 7:
            y = int(y) + 1
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidKingMovement.possible_king_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidKingMovement.possible_king_capture.append(f'{x}{y}')

            else:
                pass
    def whitekingdown():

        x = pickfile
        y = pickrank

        if int(y) >= 2:
            y = int(y) - 1
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidKingMovement.possible_king_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidKingMovement.possible_king_capture.append(f'{x}{y}')

            else:
                pass
    def whitekingupright():
        x = pickfile
        y = pickrank
        if int(y) <= 7 and ord(x) <= 71:
            y = int(y) + 1
            x = str(chr(ord(x) + 1))
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidKingMovement.possible_king_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidKingMovement.possible_king_capture.append(f'{x}{y}')

            else:
                pass
    def whitekingupleft():
        x = pickfile
        y = pickrank
        if int(y) <= 7 and ord(x) >= 66:
            y = int(y) + 1
            x = str(chr(ord(x) -1))
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidKingMovement.possible_king_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidKingMovement.possible_king_capture.append(f'{x}{y}')

            else:
                pass
    def whitekingdownright():
        x = pickfile
        y = pickrank
        if int(y) >= 2 and ord(x) <= 71:
            y = int(y) - 1
            x = str(chr(ord(x) + 1))
        if PiecePosition.dic_chess[f"{x}{y}"] == '':
            ValidKingMovement.possible_king_move.append(f'{x}{y}')

        elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
            ValidKingMovement.possible_king_capture.append(f'{x}{y}')

        else:
            pass
    def whitekingdownleft():
        x = pickfile
        y = pickrank
        if int(y) >= 2 and ord(x) >= 66:
            y = int(y) - 1
            x = str(chr(ord(x) - 1))
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidKingMovement.possible_king_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidKingMovement.possible_king_capture.append(f'{x}{y}')

            else:
                pass






            # cell[pickfile+pickrank] == 'brook1' or cell[pickfile+pickrank] == 'brook2':
# FIXME calling all pickfile and pickrank 'x' and 'y' might cause some problems so we can decide
# if we wanna change those variables or if that is redundant

class ValidRookMovement(PiecePosition):
    possible_rook_move = []
    possible_rook_capture = []

    def whiterookright():

        x = pickfile
        y = pickrank

        while ord(x) <= 71:

            x = str(chr(ord(x) + 1))
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')
                break
            else:
                break

    def whiterookleft():

        x = pickfile
        y = pickrank

        while ord(x) >= 66:
            x = str(chr(ord(x) - 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')
                break
            else:
                break

    def whiterookup():

        x = pickfile
        y = pickrank

        while int(y) <= 7:
            y = int(y) + 1

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')
                break
            else:
                break

    def whiterookdown():

        x = pickfile
        y = pickrank

        while int(y) >= 2:
            y = int(y) - 1

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')
                break
            else:
                break

class ValidBishopMovement(PiecePosition):
    possible_bishop_move = []
    possible_bishop_capture = []

    def whitebishopupright():
        x = pickfile
        y = pickrank
        while int(y) <= 7 and ord(x) <= 71:
            y = int(y) + 1
            x = str(chr(ord(x) + 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidBishopMovement.possible_bishop_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidBishopMovement.possible_bishop_capture.append(f'{x}{y}')
                break
            else:
                break
    def blackbishopupright():
        x = pickfile
        y = pickrank
        while int(y) <= 7 and ord(x) <= 71:
            y = int(y) - 1
            x = str(chr(ord(x) - 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidBishopMovement.possible_bishop_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidBishopMovement.possible_bishop_capture.append(f'{x}{y}')
                break
            else:
                break

    def whitebishopupleft():
        x = pickfile
        y = pickrank
        while int(y) <= 7 and ord(x) >= 66:
            y = int(y) + 1
            x = str(chr(ord(x) - 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidBishopMovement.possible_bishop_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidBishopMovement.possible_bishop_capture.append(f'{x}{y}')
                break
            else:
                break

    def blackbishopupleft():
        x = pickfile
        y = pickrank
        while int(y) <= 7 and ord(x) >= 66:
            y = int(y) - 1
            x = str(chr(ord(x) + 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidBishopMovement.possible_bishop_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidBishopMovement.possible_bishop_capture.append(f'{x}{y}')
                break
            else:
                break
    def whitebishopdownright():
        x = pickfile
        y = pickrank
        while int(y) >= 2 and ord(x) <= 71:
            y = int(y) - 1
            x = str(chr(ord(x) + 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidBishopMovement.possible_bishop_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidBishopMovement.possible_bishop_capture.append(f'{x}{y}')
                break
            else:
                break
    def blackbishopdownright():
        x = pickfile
        y = pickrank
        while int(y) >= 2 and ord(x) <= 71:
            y = int(y) + 1
            x = str(chr(ord(x) - 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidBishopMovement.possible_bishop_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidBishopMovement.possible_bishop_capture.append(f'{x}{y}')
                break
            else:
                break
    def whitebishopdownleft():

        x = pickfile
        y = pickrank
        while int(y) >= 2 and ord(x) >= 66:
            y = int(y) - 1
            x = str(chr(ord(x) - 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidBishopMovement.possible_bishop_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidBishopMovement.possible_bishop_capture.append(f'{x}{y}')
                break
            else:
                break
    def blackbishopdownleft():

        x = pickfile
        y = pickrank
        while int(y) >= 2 and ord(x) >= 66:
            y = int(y) + 1
            x = str(chr(ord(x) + 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidBishopMovement.possible_bishop_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidBishopMovement.possible_bishop_capture.append(f'{x}{y}')
                break
            else:
                break

class ValidQueenMovement(PiecePosition):
    possible_queen_move = []
    possible_queen_capture = []

    def whitequeenupright():
        x = pickfile
        y = pickrank
        while int(y) <= 7 and ord(x) <= 71:
            y = int(y) + 1
            x = str(chr(ord(x) + 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidQueenMovement.possible_queen_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidQueenMovement.possible_queen_capture.append(f'{x}{y}')
                break
            else:
                break
    def whitequeendownleft():
        x = pickfile
        y = pickrank
        while int(y) >= 2 and ord(x) >= 66:
            y = int(y) - 1
            x = str(chr(ord(x) - 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidQueenMovement.possible_queen_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidQueenMovement.possible_queen_capture.append(f'{x}{y}')
                break
            else:
                break

    def whitequeendownright():
        x = pickfile
        y = pickrank
        while int(y) >= 2 and ord(x) <= 71:
            y = int(y) - 1
            x = str(chr(ord(x) + 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidQueenMovement.possible_queen_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidQueenMovement.possible_queen_capture.append(f'{x}{y}')
                break
            else:
                break

    def whitequeenupleft():
        x = pickfile
        y = pickrank
        while int(y) <= 7 and ord(x) >= 66:
            y = int(y) + 1
            x = str(chr(ord(x) - 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidQueenMovement.possible_queen_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidQueenMovement.possible_queen_capture.append(f'{x}{y}')
                break
            else:
                break

    def whitequeendown():

        x = pickfile
        y = pickrank

        while int(y) >= 2:
            y = int(y) - 1

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidQueenMovement.possible_queen_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidQueenMovement.possible_queen_capture.append(f'{x}{y}')
                break
            else:
                break

    def whitequeenup():

        x = pickfile
        y = pickrank

        while int(y) <= 7:
            y = int(y) + 1

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidQueenMovement.possible_queen_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidQueenMovement.possible_queen_capture.append(f'{x}{y}')
                break
            else:
                break

    def whitequeenleft():

        x = pickfile
        y = pickrank

        while ord(x) >= 66:
            x = str(chr(ord(x) - 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidQueenMovement.possible_queen_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidQueenMovement.possible_queen_capture.append(f'{x}{y}')
                break
            else:
                break
    def whitequeenright():

        x = pickfile
        y = pickrank

        while ord(x) <= 71:
            x = str(chr(ord(x) + 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidQueenMovement.possible_queen_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidQueenMovement.possible_queen_capture.append(f'{x}{y}')
                break
            else:
                break
class DicCheck(ValidRookMovement,ValidBishopMovement):

    def movecheck():

        #ROOOOOOOK
        movefile = movecell[0]
        moverank = movecell[1]
        dicmove =str(movecell[0] + movecell[1])
        if dicmove in ValidRookMovement.possible_rook_move:
            PiecePosition.movepiece()
            ValidRookMovement.possible_rook_move = []
            ValidRookMovement.possible_rook_capture = []
        elif dicmove in ValidRookMovement.possible_rook_capture:
            PiecePosition.capture()
            ValidRookMovement.possible_rook_capture = []
            ValidRookMovement.possible_rook_move = []
        else:
            pass
        #BISHUP
        if dicmove in ValidBishopMovement.possible_bishop_move:
            PiecePosition.movepiece()
            print("dogs")
            ValidBishopMovement.possible_bishop_move = []
            ValidBishopMovement.possible_bishop_capture = []
        elif dicmove in ValidBishopMovement.possible_bishop_capture:
            PiecePosition.capture()
            print("cats")
            ValidBishopMovement.possible_bishop_capture = []
            ValidBishopMovement.possible_bishop_move = []
        else:
            print("dogcats")
        #QUEEEEEEN
        if dicmove in ValidQueenMovement.possible_queen_move:
            PiecePosition.movepiece()
            print("dog1")
            ValidQueenMovement.possible_queen_move = []
            ValidQueenMovement.possible_queen_capture = []
        elif dicmove in ValidQueenMovement.possible_queen_capture:
            PiecePosition.capture()
            print("cats1")
            ValidQueenMovement.possible_queen_capture = []
            ValidQueenMovement.possible_queen_move = []
        else:
            print("dogcats1")
        ####KINNNG

        if dicmove in ValidKingMovement.possible_king_move:
            PiecePosition.movepiece()
            print("dog5")
            ValidKingMovement.possible_king_move = []
            ValidKingMovement.possible_king_capture = []
        elif dicmove in ValidKingMovement.possible_king_capture:
            PiecePosition.capture()
            print("cats5")
            ValidKingMovement.possible_king_capture = []
            ValidKingMovement.possible_king_move = []
        else:
            print("dogcats51")

    def squarecheck():
        pickfile = pickcell[0]
        pickrank = pickcell[1]
        dicpick = pickcell[0] + pickcell[1]

        if PiecePosition.dic_chess[dicpick] == 'wrook1' or PiecePosition.dic_chess[dicpick] == 'wrook2' or \
                PiecePosition.dic_chess[dicpick] == 'brook1' or PiecePosition.dic_chess[dicpick] == 'brook2':
            mp.rook()

            # possible move list will be reset, only for now. later we will bind it to happen when move cell is clicked

        elif PiecePosition.dic_chess[dicpick] == 'wbishop1' or PiecePosition.dic_chess[dicpick] == 'wbishop2':
            mp.bishop()

        elif PiecePosition.dic_chess[dicpick] == 'bbishop1' or PiecePosition.dic_chess[dicpick] == 'bbishop2':
            mp.bishopblack()

            # print(rm.possible_bishop_capture)
            # print(rm.possible_bishop_move)
            
        elif PiecePosition.dic_chess[dicpick] == 'wknight1' or PiecePosition.dic_chess[dicpick] == 'wknight2' or \
                PiecePosition.dic_chess[dicpick] == 'bknight1' or PiecePosition.dic_chess[dicpick] == 'bknight2':
            print('knight nigga')
        # mp.knight()
        # print(rm.possible_knight_capture)
        # print(rm.possible_knight_move)
        elif PiecePosition.dic_chess[dicpick] == 'wqueen' or PiecePosition.dic_chess[dicpick] == 'bqueen':
           
            mp.queen()
        elif PiecePosition.dic_chess[dicpick] == 'wking' or PiecePosition.dic_chess[dicpick] == 'bking':
            mp.king()
        elif PiecePosition.dic_chess[dicpick] == '':
            print("pick again ni")

        else:
            print('pawn nigga')



            # PiecePosition.dic_chess[f'{movecell}'] = PiecePosition.dic_chess[f'{pickcell}']
            # PiecePosition.dic_chess[f'{pickcell}'] = ''


class Cells(DicCheck):
    rank = []
    for i in range(0, 8):
        rank[i] = rank.append(None)
    for i in range(0, 8):
        rank[i] = str(chr(65 + i))

    file = []
    for i in range(0, 8):
        file[i] = file.append(None)
    for i in range(0, 8):
        file[i] = str(int(1 + i))

    position = None
    position2 = None

    def call_cell(self, r, f):
        if Cells.position is None:
            coordinate = r + f
            Cells.position = coordinate
            print(f"{Cells.position} is pickcell")

            global pickcell
            pickcell = Cells.position
            global pickfile
            pickfile = pickcell[0]
            global pickrank
            pickrank = pickcell[1]

            self.squarecheck()



        else:
            coordinate1 = r + f
            position2 = coordinate1
            print(f"{position2} is movecell")
            # self.rook(self)
            global movecell
            movecell = position2
            global movefile
            movefile = movecell[0]
            global moverank
            moverank = movecell[1]

            self.movecheck()
            if PiecePosition.dic_chess[movecell] != '':
                main.chess_board()
            # PiecePosition.dic_chess[f'{movecell}'] = PiecePosition.dic_chess[f'{pickcell}']
            # PiecePosition.dic_chess[f'{pickcell}'] = ''
            Cells.position = None


square = Cells
dc = DicCheck
rm = ValidRookMovement
bm = ValidBishopMovement
bbm = ValidBishopMovement
qm = ValidQueenMovement
km = ValidKingMovement
mp = PieceRules
pp = PiecePosition
main = Chess

root.config(background='black')

root.minsize(918, 612)
root.maxsize(918, 612)

milk = Menu(root)
root.config(menu=milk)

friendMenu = Menu(milk)
milk.add_cascade(label="friends", menu=friendMenu)
friendMenu.add_command(label='dogs', command=dog)
friendMenu.add_separator()
friendMenu.add_command(label='cats', command=cat)

creditMenu = Menu(milk)
milk.add_cascade(label='credits', menu=creditMenu)
creditMenu.add_command(label='do you like cheese', command=dog)

exitMenu = Menu(milk)
milk.add_cascade(label='Exit', menu=exitMenu)
exitMenu.add_command(label="Are you sure?", command=root.destroy)

playButton = Button(root, text="Play Chess", width=20, height=3, fg="Black", bg="grey", command=main.chess_board).place(
    x=375, y=175)
exitButton = Button(root, text='Exit', width=20, height=3, fg="Black", bg='grey', command=root.destroy).place(x=375,
                                                                                                              y=275)

root.mainloop()

