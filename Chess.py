# !!!press alt+6 to find to do items!!!
# todo capture !!!!!!COMPLETED!!!!!!
# todo movement for bishop, queen, king, knight, and pawn
# todo win conditions - Checks, checkmate, draws such as stalemate, !!(HARD)!!
# todo player 1 and 2 turn configurations
# todo unique moves - castling, en pssante, pawn promotion


from tkinter import *


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

        A8 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[7])])
        A8.place(x=24, y=22)
        B8 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[7])])
        B8.place(x=24 + 71, y=22)
        C8 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[7])])
        C8.place(x=24 + 71 * 2, y=22)
        D8 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[7])])
        D8.place(x=24 + 71 * 3, y=22)
        E8 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[7])])
        E8.place(x=24 + 71 * 4, y=22)
        F8 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[7])])
        F8.place(x=24 + 71 * 5, y=22)
        G8 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[7])])
        G8.place(x=24 + 71 * 6, y=22)
        H8 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[7])])
        H8.place(x=24 + 71 * 7, y=22)

        A7 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[6])])
        A7.place(x=24, y=22 + 71)
        B7 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[6])])
        B7.place(x=24 + 71, y=22 + 71)
        C7 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[6])])
        C7.place(x=24 + 71 * 2, y=22 + 71)
        D7 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[6])])
        D7.place(x=24 + 71 * 3, y=22 + 71)
        E7 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[6])])
        E7.place(x=24 + 71 * 4, y=22 + 71)
        F7 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[6])])
        F7.place(x=24 + 71 * 5, y=22 + 71)
        G7 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[6])])
        G7.place(x=24 + 71 * 6, y=22 + 71)
        H7 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[6])])
        H7.place(x=24 + 71 * 7, y=22 + 71)

        A6 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[5])])
        A6.place(x=24, y=22 + 71 * 2)
        B6 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[5])])
        B6.place(x=24 + 71, y=22 + 71 * 2)
        C6 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[5])])
        C6.place(x=24 + 71 * 2, y=22 + 71 * 2)
        D6 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[5])])
        D6.place(x=24 + 71 * 3, y=22 + 71 * 2)
        E6 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[5])])
        E6.place(x=24 + 71 * 4, y=22 + 71 * 2)
        F6 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[5])])
        F6.place(x=24 + 71 * 5, y=22 + 71 * 2)
        G6 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[5])])
        G6.place(x=24 + 71 * 6, y=22 + 71 * 2)
        H6 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[5])])
        H6.place(x=24 + 71 * 7, y=22 + 71 * 2)

        A5 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[4])])
        A5.place(x=24, y=22 + 71 * 3)
        B5 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[4])])
        B5.place(x=24 + 71, y=22 + 71 * 3)
        C5 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[4])])
        C5.place(x=24 + 71 * 2, y=22 + 71 * 3)
        D5 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[4])])
        D5.place(x=24 + 71 * 3, y=22 + 71 * 3)
        E5 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[4])])
        E5.place(x=24 + 71 * 4, y=22 + 71 * 3)
        F5 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[4])])
        F5.place(x=24 + 71 * 5, y=22 + 71 * 3)
        G5 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[4])])
        G5.place(x=24 + 71 * 6, y=22 + 71 * 3)
        H5 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[4])])
        H5.place(x=24 + 71 * 7, y=22 + 71 * 3)

        A4 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[3])])
        A4.place(x=24, y=22 + 71 * 4)
        B4 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[3])])
        B4.place(x=24 + 71, y=22 + 71 * 4)
        C4 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[3])])
        C4.place(x=24 + 71 * 2, y=22 + 71 * 4)
        D4 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[3])])
        D4.place(x=24 + 71 * 3, y=22 + 71 * 4)
        E4 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[3])])
        E4.place(x=24 + 71 * 4, y=22 + 71 * 4)
        F4 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[3])])
        F4.place(x=24 + 71 * 5, y=22 + 71 * 4)
        G4 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[3])])
        G4.place(x=24 + 71 * 6, y=22 + 71 * 4)
        H4 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[3])])
        H4.place(x=24 + 71 * 7, y=22 + 71 * 4)

        A3 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[2])])
        A3.place(x=24, y=22 + 71 * 5)
        B3 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[2])])
        B3.place(x=24 + 71, y=22 + 71 * 5)
        C3 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[2])])
        C3.place(x=24 + 71 * 2, y=22 + 71 * 5)
        D3 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[2])])
        D3.place(x=24 + 71 * 3, y=22 + 71 * 5)
        E3 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[2])])
        E3.place(x=24 + 71 * 4, y=22 + 71 * 5)
        F3 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[2])])
        F3.place(x=24 + 71 * 5, y=22 + 71 * 5)
        G3 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[2])])
        G3.place(x=24 + 71 * 6, y=22 + 71 * 5)
        H3 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[2])])
        H3.place(x=24 + 71 * 7, y=22 + 71 * 5)

        A2 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[1])])
        A2.place(x=24, y=22 + 71 * 6)
        B2 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[1])])
        B2.place(x=24 + 71, y=22 + 71 * 6)
        C2 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[1])])
        C2.place(x=24 + 71 * 2, y=22 + 71 * 6)
        D2 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[1])])
        D2.place(x=24 + 71 * 3, y=22 + 71 * 6)
        E2 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[1])])
        E2.place(x=24 + 71 * 4, y=22 + 71 * 6)
        F2 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[1])])
        F2.place(x=24 + 71 * 5, y=22 + 71 * 6)
        G2 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[1])])
        G2.place(x=24 + 71 * 6, y=22 + 71 * 6)
        H2 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[1])])
        H2.place(x=24 + 71 * 7, y=22 + 71 * 6)

        A1 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[0])])
        A1.place(x=24, y=22 + 71 * 7)
        B1 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[0])])
        B1.place(x=24 + 71, y=22 + 71 * 7)
        C1 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[0])])
        C1.place(x=24 + 71 * 2, y=22 + 71 * 7)
        D1 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[0])])
        D1.place(x=24 + 71 * 3, y=22 + 71 * 7)
        E1 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[0])])
        E1.place(x=24 + 71 * 4, y=22 + 71 * 7)
        F1 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[0])])
        F1.place(x=24 + 71 * 5, y=22 + 71 * 7)
        G1 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[0])])
        G1.place(x=24 + 71 * 6, y=22 + 71 * 7)
        H1 = Button(root, width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[0])])
        H1.place(x=24 + 71 * 7, y=22 + 71 * 7)

        fix1 = Frame(root, width=327, height=612, bg='brown')
        fix1.place(x=24 + 71 * 8, y=0)
        fix2 = Frame(root, height=21, width=612, bg='brown')
        fix2.place(x=24, y=591)


##############################################################################
# pickcell = 'placeholder'
#
movecell = 'o0aceholder'



##############################################################################


# class Cells(DicCheck):
#     rank = []
#     for i in range(0, 8):
#         rank[i] = rank.append(None)
#     for i in range(0, 8):
#         rank[i] = str(chr(65 + i))
#
#     file = []
#     for i in range(0, 8):
#         file[i] = file.append(None)
#     for i in range(0, 8):
#         file[i] = str(int(1 + i))
#
#     position = None
#     position2 = None
#
#     def call_cell(self, r, f):
#         if Cells.position is None:
#             coordinate = r + f
#             Cells.position = coordinate
#             print(f"{Cells.position} is pickcell")
#
#             global pickcell
#             pickcell = Cells.position
#             global pickfile
#             pickfile = pickcell[0]
#             global pickrank
#             pickrank = pickcell[1]
#             print(pickcell)
#             self.squarecheck()
#
#
#
#         else:
#             coordinate1 = r + f
#             position2 = coordinate1
#             print(f"{position2} is movecell")
#             # self.rook(self)
#             global movecell
#             movecell = position2
#             global movefile
#             movefile = movecell[0]
#             global moverank
#             moverank = movecell[1]
#             print(movecell)
#             print(movefile)
#             print(moverank)
#             self.movecheck()
#             Cells.position = None





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
    dic_chess = {'A1': 'wrook1', 'B1': '', 'C1': 'wbishop1', 'D1': 'wqueen', 'E1': 'wking', 'F1': 'wbishop2',
                 'G1': 'wknight2', 'H1': 'wrook2',
                 'A2': '', 'B2': '', 'C2': 'wpawn3', 'D2': 'wpawn4', 'E2': 'wpawn5', 'F2': 'wpawn6', 'G2': 'wpawn7',
                 'H2': 'wpawn8',
                 'A3': '', 'B3': '', 'C3': '', 'D3': '', 'E3': '', 'F3': '', 'G3': '', 'H3': '',
                 'A4': ' ', 'B4': '', 'C4': '', 'D4': 'wrook1', 'E4': '', 'F4': '', 'G4': '', 'H4': '',
                 'A5': ' ', 'B5': '', 'C5': '', 'D5': '', 'E5': '', 'F5': '', 'G5': '', 'H5': '',
                 'A6': '', 'B6': '', 'C6': '', 'D6': '', 'E6': '', 'F6': '', 'G6': '', 'H6': '',
                 'A7': 'bpawn1', 'B7': 'bpawn2', 'C7': 'bpawn3', 'D7': 'bpawn4', 'E7': 'bpawn5', 'F7': 'bpawn6',
                 'G7': 'bpawn7', 'H7': 'bpawn8',
                 'A8': 'brook1', 'B8': 'bknight1', 'C8': 'bbishop1', 'D8': 'bqueen', 'E8': 'bking', 'F8': 'bbishop2',
                 'G8': 'bknight2', 'H8': 'brook2'}

    def capture():
        # todo PiecePosition.dic_chess[f'{movecell}'] = sidebar
        PiecePosition.dic_chess[f'{movecell}'] = PiecePosition.dic_chess[f'{pickcell}']
        PiecePosition.dic_chess[f'{pickcell}'] = ''
        print("on GANG")

    def movepiece():
        PiecePosition.dic_chess[f'{movecell}'] = PiecePosition.dic_chess[f'{pickcell}']
        PiecePosition.dic_chess[f'{pickcell}'] = ''
        print("huuu")


class PieceRules(PiecePosition):

    # rulesets acting on pieces. not the rule set of the game such as draws or checkmates

    def rook():
        rm.whiterookright()
        rm.whiterookleft()
        rm.whiterookdown()
        rm.whiterookup()


# if cell[pickfile+pickrank] == 'wrook1' or cell[pickfile+pickrank] == 'wrook2' or
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


class DicCheck(PiecePosition):

    # def check(self):
    #     if Cells.position is None:
    #         self.squarecheck()
    #     else:
    #         self.movecheck()



    def squarecheck():
        pickfile = pickcell[0]
        pickrank = pickcell[1]
        dicpick = pickcell[0] + pickcell[1]


        if PiecePosition.dic_chess[dicpick] == 'wrook1' or PiecePosition.dic_chess[dicpick] == 'wrook2' or \
                PiecePosition.dic_chess[dicpick] == 'brook1' or PiecePosition.dic_chess[dicpick] == 'brook2':
            mp.rook()
            print(rm.possible_rook_capture)
            print(rm.possible_rook_move)
            # possible move list will be reset, only for now. later we will bind it to happen when move cell is clicked
            rm.possible_rook_capture = []
            rm.possible_rook_move = []
            print(rm.possible_rook_capture)
            print(rm.possible_rook_move)
        elif PiecePosition.dic_chess[dicpick] == 'wbishop1' or PiecePosition.dic_chess[dicpick] == 'wbishop2' or \
                PiecePosition.dic_chess[dicpick] == 'bbishop1' or PiecePosition.dic_chess[dicpick] == 'bbishop2':
            # mp.bishop()
            # print(rm.possible_bishop_capture)
            # print(rm.possible_bishop_move)
            print('bishop nigga')
        elif PiecePosition.dic_chess[dicpick] == 'wknight1' or PiecePosition.dic_chess[dicpick] == 'wknight2' or \
                PiecePosition.dic_chess[dicpick] == 'bknight1' or PiecePosition.dic_chess[dicpick] == 'bknight2':
            print('knight nigga')
        # mp.knight()
        # print(rm.possible_knight_capture)
        # print(rm.possible_knight_move)
        elif PiecePosition.dic_chess[dicpick] == 'wqueen' or PiecePosition.dic_chess[dicpick] == 'bqueen':
            print('queen nigga')
        elif PiecePosition.dic_chess[dicpick] == 'wking' or PiecePosition.dic_chess[dicpick] == 'bking':
            print('king nigga')
        elif PiecePosition.dic_chess[dicpick] == '':
            print('invalid move')
        else:
            print('pawn nigga')

    def movecheck():
        movefile = movecell[0]
        moverank = movecell[1]
        dicmove = movecell[0] + movecell[1]

        if PiecePosition.dic_chess[dicmove][0] == 'b':
            PiecePosition.capture()

        else:
            PiecePosition.movepiece()

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
            print(pickcell)
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
            print(movecell)
            print(movefile)
            print(moverank)
            self.movecheck()
            Cells.position = None

# ----------------------------------objects
dc = DicCheck
rm = ValidRookMovement
mp = PieceRules
square = Cells

main = Chess
root = Tk()
root.config(background='brown')

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
print(square.position)
root.mainloop()
