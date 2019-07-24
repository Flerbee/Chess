from tkinter import *

root = Tk()

wpawnpic = PhotoImage(file = 'pawnw.png')
wkingpic = PhotoImage(file = 'kingw.png')
wqueenpic = PhotoImage(file = 'queenw.png')
wknightpic = PhotoImage(file = 'knightw.png')
wbishoppic = PhotoImage(file = 'bishopw.png')
wrookpic = PhotoImage(file = 'rookw.png')

bpawnpic = PhotoImage(file = 'pawnb.png')
bkingpic = PhotoImage(file = 'kingb.png')
bqueenpic = PhotoImage(file = 'queenb.png')
bknightpic = PhotoImage(file = 'knightb.png')
bbishoppic = PhotoImage(file = 'bishopb.png')
brookpic = PhotoImage(file = 'rookb.png')
nopic = None

def dog():
    print('i like dogs')

def cat():
    print('cats')

class Chess:


    def chess_board():
        A8 = Button(root, image=pp.dicpic[pp.dic_chess['A8']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[7]), dc.squarecheck()])
        B8 = Button(root, image=pp.dicpic[pp.dic_chess['B8']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[7]), dc.squarecheck()])
        C8 = Button(root, image=pp.dicpic[pp.dic_chess['C8']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[7]), dc.squarecheck()])
        D8 = Button(root, image=pp.dicpic[pp.dic_chess['D8']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[7]), dc.squarecheck()])
        E8 = Button(root, image=pp.dicpic[pp.dic_chess['E8']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[7]), dc.squarecheck()])
        F8 = Button(root, image=pp.dicpic[pp.dic_chess['F8']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[7]), dc.squarecheck()])
        G8 = Button(root, image=pp.dicpic[pp.dic_chess['G8']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[7]), dc.squarecheck()])
        H8 = Button(root, image=pp.dicpic[pp.dic_chess['H8']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[7]), dc.squarecheck()])

        A7 = Button(root, image=pp.dicpic[pp.dic_chess['A7']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[6]), dc.squarecheck()])
        B7 = Button(root, image=pp.dicpic[pp.dic_chess['B7']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[6]), dc.squarecheck()])
        C7 = Button(root, image=pp.dicpic[pp.dic_chess['C7']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[6]), dc.squarecheck()])
        D7 = Button(root, image=pp.dicpic[pp.dic_chess['D7']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[6]), dc.squarecheck()])
        E7 = Button(root, image=pp.dicpic[pp.dic_chess['E7']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[6]), dc.squarecheck()])
        F7 = Button(root, image=pp.dicpic[pp.dic_chess['F7']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[6]), dc.squarecheck()])
        G7 = Button(root, image=pp.dicpic[pp.dic_chess['G7']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[6]), dc.squarecheck()])
        H7 = Button(root, image=pp.dicpic[pp.dic_chess['H7']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[6]), dc.squarecheck()])

        A6 = Button(root, image=pp.dicpic[pp.dic_chess['A6']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[5]), dc.squarecheck()])
        B6 = Button(root, image=pp.dicpic[pp.dic_chess['B6']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[5]), dc.squarecheck()])
        C6 = Button(root, image=pp.dicpic[pp.dic_chess['C6']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[5]), dc.squarecheck()])
        D6 = Button(root, image=pp.dicpic[pp.dic_chess['D6']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[5]), dc.squarecheck()])
        E6 = Button(root, image=pp.dicpic[pp.dic_chess['E6']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[5]), dc.squarecheck()])
        F6 = Button(root, image=pp.dicpic[pp.dic_chess['F6']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[5]), dc.squarecheck()])
        G6 = Button(root, image=pp.dicpic[pp.dic_chess['G6']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[5]), dc.squarecheck()])
        H6 = Button(root, image=pp.dicpic[pp.dic_chess['H6']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[5]), dc.squarecheck()])

        A5 = Button(root, image=pp.dicpic[pp.dic_chess['A5']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[4]), dc.squarecheck()])
        B5 = Button(root, image=pp.dicpic[pp.dic_chess['B5']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[4]), dc.squarecheck()])
        C5 = Button(root, image=pp.dicpic[pp.dic_chess['C5']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[4]), dc.squarecheck()])
        D5 = Button(root, image=pp.dicpic[pp.dic_chess['D5']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[4]), dc.squarecheck()])
        E5 = Button(root, image=pp.dicpic[pp.dic_chess['E5']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[4]), dc.squarecheck()])
        F5 = Button(root, image=pp.dicpic[pp.dic_chess['F5']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[4]), dc.squarecheck()])
        G5 = Button(root, image=pp.dicpic[pp.dic_chess['G5']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[4]), dc.squarecheck()])
        H5 = Button(root, image=pp.dicpic[pp.dic_chess['H5']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[4]), dc.squarecheck()])

        A4 = Button(root, image=pp.dicpic[pp.dic_chess['A4']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[3]), dc.squarecheck()])
        B4 = Button(root, image=pp.dicpic[pp.dic_chess['B4']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[3]), dc.squarecheck()])
        C4 = Button(root, image=pp.dicpic[pp.dic_chess['C4']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[3]), dc.squarecheck()])
        D4 = Button(root, image=pp.dicpic[pp.dic_chess['D4']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[3]), dc.squarecheck()])
        E4 = Button(root, image=pp.dicpic[pp.dic_chess['E4']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[3]), dc.squarecheck()])
        F4 = Button(root, image=pp.dicpic[pp.dic_chess['F4']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[3]), dc.squarecheck()])
        G4 = Button(root, image=pp.dicpic[pp.dic_chess['G4']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[3]), dc.squarecheck()])
        H4 = Button(root, image=pp.dicpic[pp.dic_chess['H4']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[3]), dc.squarecheck()])

        A3 = Button(root, image=pp.dicpic[pp.dic_chess['A3']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[2]), dc.squarecheck()])
        B3 = Button(root, image=pp.dicpic[pp.dic_chess['B3']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[2]), dc.squarecheck()])
        C3 = Button(root, image=pp.dicpic[pp.dic_chess['C3']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[2]), dc.squarecheck()])
        D3 = Button(root, image=pp.dicpic[pp.dic_chess['D3']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[2]), dc.squarecheck()])
        E3 = Button(root, image=pp.dicpic[pp.dic_chess['E3']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[2]), dc.squarecheck()])
        F3 = Button(root, image=pp.dicpic[pp.dic_chess['F3']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[2]), dc.squarecheck()])
        G3 = Button(root, image=pp.dicpic[pp.dic_chess['G3']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[2]), dc.squarecheck()])
        H3 = Button(root, image=pp.dicpic[pp.dic_chess['H3']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[2]), dc.squarecheck()])

        A2 = Button(root, image=pp.dicpic[pp.dic_chess['A2']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[1]), dc.squarecheck()])
        B2 = Button(root, image=pp.dicpic[pp.dic_chess['B2']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[1]), dc.squarecheck()])
        C2 = Button(root, image=pp.dicpic[pp.dic_chess['C2']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[1]), dc.squarecheck()])
        D2 = Button(root, image=pp.dicpic[pp.dic_chess['D2']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[1]), dc.squarecheck()])
        E2 = Button(root, image=pp.dicpic[pp.dic_chess['E2']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[1]), dc.squarecheck()])
        F2 = Button(root, image=pp.dicpic[pp.dic_chess['F2']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[1]), dc.squarecheck()])
        G2 = Button(root, image=pp.dicpic[pp.dic_chess['G2']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[1]), dc.squarecheck()])
        H2 = Button(root, image=pp.dicpic[pp.dic_chess['H2']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[1]), dc.squarecheck()])

        A1 = Button(root, image=pp.dicpic[pp.dic_chess['A1']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[0], square.file[0]), dc.squarecheck()])
        B1 = Button(root, image=pp.dicpic[pp.dic_chess['B1']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[1], square.file[0]), dc.squarecheck()])
        C1 = Button(root, image=pp.dicpic[pp.dic_chess['C1']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[2], square.file[0]), dc.squarecheck()])
        D1 = Button(root, image=pp.dicpic[pp.dic_chess['D1']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[3], square.file[0]), dc.squarecheck()])
        E1 = Button(root, image=pp.dicpic[pp.dic_chess['E1']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[4], square.file[0]), dc.squarecheck()])
        F1 = Button(root, image=pp.dicpic[pp.dic_chess['F1']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[5], square.file[0]), dc.squarecheck()])
        G1 = Button(root, image=pp.dicpic[pp.dic_chess['G1']], width=71, height=71, bg='darkred',
                    command=lambda: [square.call_cell(square, square.rank[6], square.file[0]), dc.squarecheck()])
        H1 = Button(root, image=pp.dicpic[pp.dic_chess['H1']], width=71, height=71, bg='brown',
                    command=lambda: [square.call_cell(square, square.rank[7], square.file[0]), dc.squarecheck()])

        fix1 = Frame(root, width=327, height=612, bg='black')
        fix1.place(x=24 + 71 * 8, y=0)
        fix2 = Frame(root, height=21, width=612, bg='black')
        fix2.place(x=24, y=591)

        A8.place(x=24, y=22)
        B8.place(x=24 + 71, y=22)
        C8.place(x=24 + 71 * 2, y=22)
        D8.place(x=24 + 71 * 3, y=22)
        E8.place(x=24 + 71 * 4, y=22)
        F8.place(x=24 + 71 * 5, y=22)
        G8.place(x=24 + 71 * 6, y=22)
        H8.place(x=24 + 71 * 7, y=22)
        A7.place(x=24, y=22 + 71)
        B7.place(x=24 + 71, y=22 + 71)
        C7.place(x=24 + 71 * 2, y=22 + 71)
        D7.place(x=24 + 71 * 3, y=22 + 71)
        E7.place(x=24 + 71 * 4, y=22 + 71)
        F7.place(x=24 + 71 * 5, y=22 + 71)
        G7.place(x=24 + 71 * 6, y=22 + 71)
        H7.place(x=24 + 71 * 7, y=22 + 71)
        A6.place(x=24, y=22 + 71 * 2)
        B6.place(x=24 + 71, y=22 + 71 * 2)
        C6.place(x=24 + 71 * 2, y=22 + 71 * 2)
        D6.place(x=24 + 71 * 3, y=22 + 71 * 2)
        E6.place(x=24 + 71 * 4, y=22 + 71 * 2)
        F6.place(x=24 + 71 * 5, y=22 + 71 * 2)
        G6.place(x=24 + 71 * 6, y=22 + 71 * 2)
        H6.place(x=24 + 71 * 7, y=22 + 71 * 2)
        A5.place(x=24, y=22 + 71 * 3)
        B5.place(x=24 + 71, y=22 + 71 * 3)
        C5.place(x=24 + 71 * 2, y=22 + 71 * 3)
        D5.place(x=24 + 71 * 3, y=22 + 71 * 3)
        E5.place(x=24 + 71 * 4, y=22 + 71 * 3)
        F5.place(x=24 + 71 * 5, y=22 + 71 * 3)
        G5.place(x=24 + 71 * 6, y=22 + 71 * 3)
        H5.place(x=24 + 71 * 7, y=22 + 71 * 3)
        A4.place(x=24, y=22 + 71 * 4)
        B4.place(x=24 + 71, y=22 + 71 * 4)
        C4.place(x=24 + 71 * 2, y=22 + 71 * 4)
        D4.place(x=24 + 71 * 3, y=22 + 71 * 4)
        E4.place(x=24 + 71 * 4, y=22 + 71 * 4)
        F4.place(x=24 + 71 * 5, y=22 + 71 * 4)
        G4.place(x=24 + 71 * 6, y=22 + 71 * 4)
        H4.place(x=24 + 71 * 7, y=22 + 71 * 4)
        A3.place(x=24, y=22 + 71 * 5)
        B3.place(x=24 + 71, y=22 + 71 * 5)
        C3.place(x=24 + 71 * 2, y=22 + 71 * 5)
        D3.place(x=24 + 71 * 3, y=22 + 71 * 5)
        E3.place(x=24 + 71 * 4, y=22 + 71 * 5)
        F3.place(x=24 + 71 * 5, y=22 + 71 * 5)
        G3.place(x=24 + 71 * 6, y=22 + 71 * 5)
        H3.place(x=24 + 71 * 7, y=22 + 71 * 5)
        A2.place(x=24, y=22 + 71 * 6)
        B2.place(x=24 + 71, y=22 + 71 * 6)
        C2.place(x=24 + 71 * 2, y=22 + 71 * 6)
        D2.place(x=24 + 71 * 3, y=22 + 71 * 6)
        E2.place(x=24 + 71 * 4, y=22 + 71 * 6)
        F2.place(x=24 + 71 * 5, y=22 + 71 * 6)
        G2.place(x=24 + 71 * 6, y=22 + 71 * 6)
        H2.place(x=24 + 71 * 7, y=22 + 71 * 6)
        A1.place(x=24, y=22 + 71 * 7)
        B1.place(x=24 + 71, y=22 + 71 * 7)
        C1.place(x=24 + 71 * 2, y=22 + 71 * 7)
        D1.place(x=24 + 71 * 3, y=22 + 71 * 7)
        E1.place(x=24 + 71 * 4, y=22 + 71 * 7)
        F1.place(x=24 + 71 * 5, y=22 + 71 * 7)
        G1.place(x=24 + 71 * 6, y=22 + 71 * 7)
        H1.place(x=24 + 71 * 7, y=22 + 71 * 7)

    # def chess_board_black:
    #     A8 = Button(root, image=pp.dicpic[pp.dic_chess['A8']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[0], square.file[7]), dc.squarecheck()])
    #     B8 = Button(root, image=pp.dicpic[pp.dic_chess['B8']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[1], square.file[7]), dc.squarecheck()])
    #     C8 = Button(root, image=pp.dicpic[pp.dic_chess['C8']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[2], square.file[7]), dc.squarecheck()])
    #     D8 = Button(root, image=pp.dicpic[pp.dic_chess['D8']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[3], square.file[7]), dc.squarecheck()])
    #     E8 = Button(root, image=pp.dicpic[pp.dic_chess['E8']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[4], square.file[7]), dc.squarecheck()])
    #     F8 = Button(root, image=pp.dicpic[pp.dic_chess['F8']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[5], square.file[7]), dc.squarecheck()])
    #     G8 = Button(root, image=pp.dicpic[pp.dic_chess['G8']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[6], square.file[7]), dc.squarecheck()])
    #     H8 = Button(root, image=pp.dicpic[pp.dic_chess['H8']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[7], square.file[7]), dc.squarecheck()])
    #
    #     A7 = Button(root, image=pp.dicpic[pp.dic_chess['A7']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[0], square.file[6]), dc.squarecheck()])
    #     B7 = Button(root, image=pp.dicpic[pp.dic_chess['B7']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[1], square.file[6]), dc.squarecheck()])
    #     C7 = Button(root, image=pp.dicpic[pp.dic_chess['C7']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[2], square.file[6]), dc.squarecheck()])
    #     D7 = Button(root, image=pp.dicpic[pp.dic_chess['D7']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[3], square.file[6]), dc.squarecheck()])
    #     E7 = Button(root, image=pp.dicpic[pp.dic_chess['E7']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[4], square.file[6]), dc.squarecheck()])
    #     F7 = Button(root, image=pp.dicpic[pp.dic_chess['F7']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[5], square.file[6]), dc.squarecheck()])
    #     G7 = Button(root, image=pp.dicpic[pp.dic_chess['G7']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[6], square.file[6]), dc.squarecheck()])
    #     H7 = Button(root, image=pp.dicpic[pp.dic_chess['H7']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[7], square.file[6]), dc.squarecheck()])
    #
    #     A6 = Button(root, image=pp.dicpic[pp.dic_chess['A6']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[0], square.file[5]), dc.squarecheck()])
    #     B6 = Button(root, image=pp.dicpic[pp.dic_chess['B6']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[1], square.file[5]), dc.squarecheck()])
    #     C6 = Button(root, image=pp.dicpic[pp.dic_chess['C6']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[2], square.file[5]), dc.squarecheck()])
    #     D6 = Button(root, image=pp.dicpic[pp.dic_chess['D6']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[3], square.file[5]), dc.squarecheck()])
    #     E6 = Button(root, image=pp.dicpic[pp.dic_chess['E6']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[4], square.file[5]), dc.squarecheck()])
    #     F6 = Button(root, image=pp.dicpic[pp.dic_chess['F6']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[5], square.file[5]), dc.squarecheck()])
    #     G6 = Button(root, image=pp.dicpic[pp.dic_chess['G6']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[6], square.file[5]), dc.squarecheck()])
    #     H6 = Button(root, image=pp.dicpic[pp.dic_chess['H6']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[7], square.file[5]), dc.squarecheck()])
    #
    #     A5 = Button(root, image=pp.dicpic[pp.dic_chess['A5']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[0], square.file[4]), dc.squarecheck()])
    #     B5 = Button(root, image=pp.dicpic[pp.dic_chess['B5']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[1], square.file[4]), dc.squarecheck()])
    #     C5 = Button(root, image=pp.dicpic[pp.dic_chess['C5']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[2], square.file[4]), dc.squarecheck()])
    #     D5 = Button(root, image=pp.dicpic[pp.dic_chess['D5']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[3], square.file[4]), dc.squarecheck()])
    #     E5 = Button(root, image=pp.dicpic[pp.dic_chess['E5']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[4], square.file[4]), dc.squarecheck()])
    #     F5 = Button(root, image=pp.dicpic[pp.dic_chess['F5']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[5], square.file[4]), dc.squarecheck()])
    #     G5 = Button(root, image=pp.dicpic[pp.dic_chess['G5']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[6], square.file[4]), dc.squarecheck()])
    #     H5 = Button(root, image=pp.dicpic[pp.dic_chess['H5']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[7], square.file[4]), dc.squarecheck()])
    #
    #     A4 = Button(root, image=pp.dicpic[pp.dic_chess['A4']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[0], square.file[3]), dc.squarecheck()])
    #     B4 = Button(root, image=pp.dicpic[pp.dic_chess['B4']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[1], square.file[3]), dc.squarecheck()])
    #     C4 = Button(root, image=pp.dicpic[pp.dic_chess['C4']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[2], square.file[3]), dc.squarecheck()])
    #     D4 = Button(root, image=pp.dicpic[pp.dic_chess['D4']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[3], square.file[3]), dc.squarecheck()])
    #     E4 = Button(root, image=pp.dicpic[pp.dic_chess['E4']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[4], square.file[3]), dc.squarecheck()])
    #     F4 = Button(root, image=pp.dicpic[pp.dic_chess['F4']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[5], square.file[3]), dc.squarecheck()])
    #     G4 = Button(root, image=pp.dicpic[pp.dic_chess['G4']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[6], square.file[3]), dc.squarecheck()])
    #     H4 = Button(root, image=pp.dicpic[pp.dic_chess['H4']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[7], square.file[3]), dc.squarecheck()])
    #
    #     A3 = Button(root, image=pp.dicpic[pp.dic_chess['A3']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[0], square.file[2]), dc.squarecheck()])
    #     B3 = Button(root, image=pp.dicpic[pp.dic_chess['B3']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[1], square.file[2]), dc.squarecheck()])
    #     C3 = Button(root, image=pp.dicpic[pp.dic_chess['C3']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[2], square.file[2]), dc.squarecheck()])
    #     D3 = Button(root, image=pp.dicpic[pp.dic_chess['D3']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[3], square.file[2]), dc.squarecheck()])
    #     E3 = Button(root, image=pp.dicpic[pp.dic_chess['E3']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[4], square.file[2]), dc.squarecheck()])
    #     F3 = Button(root, image=pp.dicpic[pp.dic_chess['F3']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[5], square.file[2]), dc.squarecheck()])
    #     G3 = Button(root, image=pp.dicpic[pp.dic_chess['G3']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[6], square.file[2]), dc.squarecheck()])
    #     H3 = Button(root, image=pp.dicpic[pp.dic_chess['H3']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[7], square.file[2]), dc.squarecheck()])
    #
    #     A2 = Button(root, image=pp.dicpic[pp.dic_chess['A2']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[0], square.file[1]), dc.squarecheck()])
    #     B2 = Button(root, image=pp.dicpic[pp.dic_chess['B2']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[1], square.file[1]), dc.squarecheck()])
    #     C2 = Button(root, image=pp.dicpic[pp.dic_chess['C2']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[2], square.file[1]), dc.squarecheck()])
    #     D2 = Button(root, image=pp.dicpic[pp.dic_chess['D2']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[3], square.file[1]), dc.squarecheck()])
    #     E2 = Button(root, image=pp.dicpic[pp.dic_chess['E2']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[4], square.file[1]), dc.squarecheck()])
    #     F2 = Button(root, image=pp.dicpic[pp.dic_chess['F2']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[5], square.file[1]), dc.squarecheck()])
    #     G2 = Button(root, image=pp.dicpic[pp.dic_chess['G2']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[6], square.file[1]), dc.squarecheck()])
    #     H2 = Button(root, image=pp.dicpic[pp.dic_chess['H2']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[7], square.file[1]), dc.squarecheck()])
    #
    #     A1 = Button(root, image=pp.dicpic[pp.dic_chess['A1']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[0], square.file[0]), dc.squarecheck()])
    #     B1 = Button(root, image=pp.dicpic[pp.dic_chess['B1']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[1], square.file[0]), dc.squarecheck()])
    #     C1 = Button(root, image=pp.dicpic[pp.dic_chess['C1']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[2], square.file[0]), dc.squarecheck()])
    #     D1 = Button(root, image=pp.dicpic[pp.dic_chess['D1']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[3], square.file[0]), dc.squarecheck()])
    #     E1 = Button(root, image=pp.dicpic[pp.dic_chess['E1']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[4], square.file[0]), dc.squarecheck()])
    #     F1 = Button(root, image=pp.dicpic[pp.dic_chess['F1']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[5], square.file[0]), dc.squarecheck()])
    #     G1 = Button(root, image=pp.dicpic[pp.dic_chess['G1']], width=71, height=71, bg='darkred',
    #                 command=lambda: [square.call_cell(square, square.rank[6], square.file[0]), dc.squarecheck()])
    #     H1 = Button(root, image=pp.dicpic[pp.dic_chess['H1']], width=71, height=71, bg='brown',
    #                 command=lambda: [square.call_cell(square, square.rank[7], square.file[0]), dc.squarecheck()])
    #
    #     fix1 = Frame(root, width=327, height=612, bg='black')
    #     fix1.place(x=24 + 71 * 8, y=0)
    #     fix2 = Frame(root, height=21, width=612, bg='black')
    #     fix2.place(x=24, y=591)
    #
    #     A8.place(x = 24 + 71 * 7, y = 22 + 71 *7)
    #     B8.place(x = 24 + 71 * 6, y = 22 + 71 *7)
    #     C8.place(x = 24 + 71 * 5, y = 22 + 71 *7)
    #     D8.place(x = 24 + 71 * 4, y = 22 + 71 *7)
    #     E8.place(x = 24 + 71 * 3, y = 22 + 71 *7)
    #     F8.place(x = 24 + 71 * 2, y = 22 + 71 *7)
    #     G8.place(x = 24 + 71, y = 22 + 71 *7)
    #     H8.place(x = 24, y = 22 + 71 *7)
    #
    #     A7.place(x = 24 + 71 * 7, y = 22 + 71 * 6)
    #     B7.place(x = 24 + 71 * 6, y = 22 + 71 * 6)
    #     C7.place(x = 24 + 71 * 5, y = 22 + 71 * 6)
    #     D7.place(x = 24 + 71 * 4, y = 22 + 71 * 6)
    #     E7.place(x = 24 + 71 * 3, y = 22 + 71 * 6)
    #     F7.place(x = 24 + 71 * 2, y = 22 + 71 * 6)
    #     G7.place(x = 24 + 71, y = 22 + 71 * 6)
    #     H7.place(x = 24, y = 22 + 71 * 6)
    #
    #     A6.place(x = 24 + 71 * 7, y = 22 + 71 * 5)
    #     B6.place(x = 24 + 71 * 6, y = 22 + 71 * 5)
    #     C6.place(x = 24 + 71 * 5, y = 22 + 71 * 5)
    #     D6.place(x = 24 + 71 * 4, y = 22 + 71 * 5)
    #     E6.place(x = 24 + 71 * 3, y = 22 + 71 * 5)
    #     F6.place(x = 24 + 71 * 2, y = 22 + 71 * 5)
    #     G6.place(x = 24 + 71, y = 22 + 71 * 5)
    #     H6.place(x = 24, y = 22 + 71 * 5)
    #
    #     A5.place(x = 24 + 71 * 7, y = 22 + 71 * 4)
    #     B5.place(x = 24 + 71 * 6, y = 22 + 71 * 4)
    #     C5.place(x = 24 + 71 * 5, y = 22 + 71 * 4)
    #     D5.place(x = 24 + 71 * 4, y = 22 + 71 * 4)
    #     E5.place(x = 24 + 71 * 3, y = 22 + 71 * 4)
    #     F5.place(x = 24 + 71 * 2, y = 22 + 71 * 4)
    #     G5.place(x = 24 + 71, y = 22 + 71 * 4)
    #     H5.place(x = 24, y = 22 + 71 * 4)
    #
    #     A4.place(x = 24 + 71 * 7, y = 22 + 71 * 3)
    #     B4.place(x = 24 + 71 * 6, y = 22 + 71 * 3)
    #     C4.place(x = 24 + 71 * 5, y = 22 + 71 * 3)
    #     D4.place(x = 24 + 71 * 4, y = 22 + 71 * 3)
    #     E4.place(x = 24 + 71 * 3, y = 22 + 71 * 3)
    #     F4.place(x = 24 + 71 * 2, y = 22 + 71 * 3)
    #     G4.place(x = 24 + 71, y = 22 + 71 * 3)
    #     H4.place(x = 24, y = 22 + 71 * 3)
    #
    #     A3.place(x = 24 + 71 * 7, y = 22 + 71 * 2)
    #     B3.place(x = 24 + 71 * 6, y = 22 + 71 * 2)
    #     C3.place(x = 24 + 71 * 5, y = 22 + 71 * 2)
    #     D3.place(x = 24 + 71 * 4, y = 22 + 71 * 2)
    #     E3.place(x = 24 + 71 * 3, y = 22 + 71 * 2)
    #     F3.place(x = 24 + 71 * 2, y = 22 + 71 * 2)
    #     G3.place(x = 24 + 71, y = 22 + 71 * 2)
    #     H3.place(x = 24, y = 22 + 71 * 2)
    #
    #     A2.place(x = 24 + 71 * 7, y = 22 + 71)
    #     B2.place(x = 24 + 71 * 6, y = 22 + 71)
    #     C2.place(x = 24 + 71 * 5, y = 22 + 71)
    #     D2.place(x = 24 + 71 * 4, y = 22 + 71)
    #     E2.place(x = 24 + 71 * 3, y = 22 + 71)
    #     F2.place(x = 24 + 71 * 2, y = 22 + 71)
    #     G2.place(x = 24 + 71, y = 22 + 71)
    #     H2.place(x = 24, y = 22 + 71)
    #
    #     A1.place(x = 24 + 71 * 7, y = 22)
    #     B1.place(x = 24 + 71 * 6, y = 22)
    #     C1.place(x = 24 + 71 * 5, y = 22)
    #     D1.place(x = 24 + 71 * 4, y = 22)
    #     E1.place(x = 24 + 71 * 3, y = 22)
    #     F1.place(x = 24 + 71 * 2, y = 22)
    #     G1.place(x = 24 + 71, y = 22)
    #     H1.place(x = 24, y = 22)



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
                 'A4': '', 'B4': '', 'C4': '', 'D4': '', 'E4': '', 'F4': '', 'G4': '', 'H4': '',
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
              'wqueen': wqueenpic, 'bqueen': bqueenpic, 'wking': wkingpic, 'bking': bkingpic, '': nopic}

    def capture():
        # todo PiecePosition.dic_chess[f'{movecell}'] = sidebar
        PiecePosition.dic_chess[f'{movecell}'] = PiecePosition.dic_chess[f'{pickcell}']
        PiecePosition.dic_chess[f'{pickcell}'] = ''

    def movepiece():
        PiecePosition.dic_chess[f'{movecell}'] = PiecePosition.dic_chess[f'{pickcell}']
        PiecePosition.dic_chess[f'{pickcell}'] = ''



class PieceRules(PiecePosition):


    def whiterook():
        rm.whiterookright()
        rm.whiterookleft()
        rm.whiterookdown()
        rm.whiterookup()

    def whitebishop():
        bm.whitebishopupleft()
        bm.whitebishopupright()
        bm.whitebishopdownleft()
        bm.whitebishopdownright()

    def whiteknight():
        nm.whiteknightrightup()
        nm.whiteknightrightdown()
        nm.whiteknightleftup()
        nm.whiteknightleftdown()
        nm.whiteknightupright()
        nm.whiteknightupleft()
        nm.whiteknightdownright()
        nm.whiteknightdownleft()

    def whitequeen():
        qm.whitequeenright()
        qm.whitequeenleft()
        qm.whitequeenupright()
        qm.whitequeendownright()
        qm.whitequeendownleft()
        qm.whitequeenupleft()
        qm.whitequeenup()
        qm.whitequeendown()

    def whiteking():
        km.whitekingright()
        km.whitekingleft()
        km.whitekingupright()
        km.whitekingdownright()
        km.whitekingdownleft()
        km.whitekingupleft()
        km.whitekingup()
        km.whitekingdown()

    def whitepawn():
        pm.whitepawnup()
        pm.whitepawnup2()
        pm.whitepawnrightcapture()
        pm.whitepawnleftcapture()


    def blackrook():
        rm.blackrookdown()
        rm.blackrookleft()
        rm.blackrookright()
        rm.blackrookup()

    def blackbishop():
        bm.blackbishopupleft()
        bm.blackbishopupright()
        bm.blackbishopdownleft()
        bm.blackbishopdownright()

    def blackknight():
        nm.blackknightdownleft()
        nm.blackknightdownright()
        nm.blackknightleftdown()
        nm.blackknightleftup()
        nm.blackknightrightdown()
        nm.blackknightrightup()
        nm.blackknightupleft()
        nm.blackknightupright()

    def blackqueen():
        qm.blackqueendown()
        qm.blackqueendownleft()
        qm.blackqueendownright()
        qm.blackqueenleft()
        qm.blackqueenright()
        qm.blackqueenupleft()
        qm.blackqueenup()
        qm.blackqueenright()

    def blackking():
        km.blackkingdownleft()
        km.blackkingdown()
        km.blackkingdownright()
        km.blackkingleft()
        km.blackkingright()
        km.blackkingupleft()
        km.blackkingup()
        km.blackkingupright()

    def blackpawn():
        pm.blackpawnleftcapture()
        pm.blackpawnrightcapture()
        pm.blackpawnup()
        pm.blackpawnup2()


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

    def blackrookright():

        x = pickfile
        y = pickrank

        while ord(x) <= 71:

            x = str(chr(ord(x) + 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')
                break
            else:
                break

    def blackrookleft():

        x = pickfile
        y = pickrank

        while ord(x) >= 66:
            x = str(chr(ord(x) - 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')
                break
            else:
                break

    def blackrookup():

        x = pickfile
        y = pickrank

        while int(y) <= 7:
            y = int(y) + 1

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')
                break
            else:
                break

    def blackrookdown():

        x = pickfile
        y = pickrank

        while int(y) >= 2:
            y = int(y) - 1

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
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
            y = int(y) + 1
            x = str(chr(ord(x) + 1))

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
            y = int(y) + 1
            x = str(chr(ord(x) - 1))

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
            y = int(y) - 1
            x = str(chr(ord(x) + 1))

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
            y = int(y) - 1
            x = str(chr(ord(x) - 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidBishopMovement.possible_bishop_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidBishopMovement.possible_bishop_capture.append(f'{x}{y}')
                break
            else:
                break


class ValidKnightMovement(PiecePosition):
    possible_knight_move = []
    possible_knight_capture = []

    def whiteknightrightup():

        x = pickfile
        y = pickrank

        if ord(x) <= 70 and int(y) < 8:
            x = str(chr(ord(x)+2))
            y = int(y) + 1

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')

            else:
                pass

    def whiteknightrightdown():

        x = pickfile
        y = pickrank

        if ord(x) <= 70 and int(y) > 1:
            x = str(chr(ord(x)+2))
            y = int(y) - 1

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')

            else:
                pass
    def whiteknightleftup():

        x = pickfile
        y = pickrank

        if ord(x) >= 67 and int(y) < 8:
            x = str(chr(ord(x)-2))
            y = int(y) + 1

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')

            else:
                pass
    def whiteknightleftdown():

        x = pickfile
        y = pickrank

        if ord(x) >= 67 and int(y) > 1:
            x = str(chr(ord(x)-2))
            y = int(y) - 1

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')

            else:
                pass
    def whiteknightupright():

        x = pickfile
        y = pickrank

        if ord(x) <= 71 and int(y) < 7:
            x = str(chr(ord(x) + 1))
            y = int(y) + 2

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')

            else:
                pass

    def whiteknightupleft():

        x = pickfile
        y = pickrank

        if ord(x) >= 66 and int(y) < 7:
            x = str(chr(ord(x)-1))
            y = int(y) + 2

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')

            else:
                pass

    def whiteknightdownright():

        x = pickfile
        y = pickrank

        if ord(x) <= 71 and int(y) > 2:
            x = str(chr(ord(x)+1))
            y = int(y) - 2

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')

            else:
                pass

    def whiteknightdownleft():

        x = pickfile
        y = pickrank

        if ord(x) >= 66 and int(y) > 2:
            x = str(chr(ord(x) - 1))
            y = int(y) - 2

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')

            else:
                pass

    def blackknightrightup():

        x = pickfile
        y = pickrank

        if ord(x) <= 70 and int(y) < 8:
            x = str(chr(ord(x)+2))
            y = int(y) + 1

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')

            else:
                pass

    def blackknightrightdown():

        x = pickfile
        y = pickrank

        if ord(x) <= 70 and int(y) > 1:
            x = str(chr(ord(x)+2))
            y = int(y) - 1

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')

            else:
                pass
    def blackknightleftup():

        x = pickfile
        y = pickrank

        if ord(x) >= 67 and int(y) < 8:
            x = str(chr(ord(x)-2))
            y = int(y) + 1

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')

            else:
                pass
    def blackknightleftdown():

        x = pickfile
        y = pickrank

        if ord(x) >= 67 and int(y) > 1:
            x = str(chr(ord(x)-2))
            y = int(y) - 1

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')

            else:
                pass
    def blackknightupright():

        x = pickfile
        y = pickrank

        if ord(x) <= 71 and int(y) < 7:
            x = str(chr(ord(x) + 1))
            y = int(y) + 2

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')

            else:
                pass

    def blackknightupleft():

        x = pickfile
        y = pickrank

        if ord(x) >= 66 and int(y) < 7:
            x = str(chr(ord(x)-1))
            y = int(y) + 2

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')

            else:
                pass

    def blackknightdownright():

        x = pickfile
        y = pickrank

        if ord(x) <= 71 and int(y) > 2:
            x = str(chr(ord(x)+1))
            y = int(y) - 2

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')

            else:
                pass

    def blackknightdownleft():

        x = pickfile
        y = pickrank

        if ord(x) >= 66 and int(y) > 2:
            x = str(chr(ord(x) - 1))
            y = int(y) - 2

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidRookMovement.possible_rook_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidRookMovement.possible_rook_capture.append(f'{x}{y}')

            else:
                pass


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

    def blackqueenupright():
        x = pickfile
        y = pickrank
        while int(y) <= 7 and ord(x) <= 71:
            y = int(y) + 1
            x = str(chr(ord(x) + 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidQueenMovement.possible_queen_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidQueenMovement.possible_queen_capture.append(f'{x}{y}')
                break
            else:
                break
    def blackqueendownleft():
        x = pickfile
        y = pickrank
        while int(y) >= 2 and ord(x) >= 66:
            y = int(y) - 1
            x = str(chr(ord(x) - 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidQueenMovement.possible_queen_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidQueenMovement.possible_queen_capture.append(f'{x}{y}')
                break
            else:
                break

    def blackqueendownright():
        x = pickfile
        y = pickrank
        while int(y) >= 2 and ord(x) <= 71:
            y = int(y) - 1
            x = str(chr(ord(x) + 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidQueenMovement.possible_queen_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidQueenMovement.possible_queen_capture.append(f'{x}{y}')
                break
            else:
                break

    def blackqueenupleft():
        x = pickfile
        y = pickrank
        while int(y) <= 7 and ord(x) >= 66:
            y = int(y) + 1
            x = str(chr(ord(x) - 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidQueenMovement.possible_queen_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidQueenMovement.possible_queen_capture.append(f'{x}{y}')
                break
            else:
                break

    def blackqueendown():

        x = pickfile
        y = pickrank

        while int(y) >= 2:
            y = int(y) - 1

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidQueenMovement.possible_queen_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidQueenMovement.possible_queen_capture.append(f'{x}{y}')
                break
            else:
                break

    def blackqueenup():

        x = pickfile
        y = pickrank

        while int(y) <= 7:
            y = int(y) + 1

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidQueenMovement.possible_queen_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidQueenMovement.possible_queen_capture.append(f'{x}{y}')
                break
            else:
                break

    def blackqueenleft():

        x = pickfile
        y = pickrank

        while ord(x) >= 66:
            x = str(chr(ord(x) - 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidQueenMovement.possible_queen_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidQueenMovement.possible_queen_capture.append(f'{x}{y}')
                break
            else:
                break
    def blackqueenright():

        x = pickfile
        y = pickrank

        while ord(x) <= 71:
            x = str(chr(ord(x) + 1))

            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidQueenMovement.possible_queen_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidQueenMovement.possible_queen_capture.append(f'{x}{y}')
                break
            else:
                break


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

    def blackkingright():

        x = pickfile
        y = pickrank

        if ord(x) <= 71:
            x = str(chr(ord(x) + 1))
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidKingMovement.possible_king_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidKingMovement.possible_king_capture.append(f'{x}{y}')

            else:
                pass
    def blackkingleft():

        x = pickfile
        y = pickrank

        if ord(x) >= 66:
            x = str(chr(ord(x) - 1))
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidKingMovement.possible_king_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidKingMovement.possible_king_capture.append(f'{x}{y}')

            else:
                pass
    def blackkingup():

        x = pickfile
        y = pickrank

        if int(y) <= 7:
            y = int(y) + 1
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidKingMovement.possible_king_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidKingMovement.possible_king_capture.append(f'{x}{y}')

            else:
                pass
    def blackkingdown():

        x = pickfile
        y = pickrank

        if int(y) >= 2:
            y = int(y) - 1
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidKingMovement.possible_king_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidKingMovement.possible_king_capture.append(f'{x}{y}')

            else:
                pass
    def blackkingupright():
        x = pickfile
        y = pickrank
        if int(y) <= 7 and ord(x) <= 71:
            y = int(y) + 1
            x = str(chr(ord(x) + 1))
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidKingMovement.possible_king_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidKingMovement.possible_king_capture.append(f'{x}{y}')

            else:
                pass
    def blackkingupleft():
        x = pickfile
        y = pickrank
        if int(y) <= 7 and ord(x) >= 66:
            y = int(y) + 1
            x = str(chr(ord(x) -1))
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidKingMovement.possible_king_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidKingMovement.possible_king_capture.append(f'{x}{y}')

            else:
                pass
    def blackkingdownright():
        x = pickfile
        y = pickrank
        if int(y) >= 2 and ord(x) <= 71:
            y = int(y) - 1
            x = str(chr(ord(x) + 1))
        if PiecePosition.dic_chess[f"{x}{y}"] == '':
            ValidKingMovement.possible_king_move.append(f'{x}{y}')

        elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
            ValidKingMovement.possible_king_capture.append(f'{x}{y}')

        else:
            pass
    def blackkingdownleft():
        x = pickfile
        y = pickrank
        if int(y) >= 2 and ord(x) >= 66:
            y = int(y) - 1
            x = str(chr(ord(x) - 1))
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidKingMovement.possible_king_move.append(f'{x}{y}')

            elif PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                ValidKingMovement.possible_king_capture.append(f'{x}{y}')

            else:
                pass


class ValidPawnMovement(PiecePosition):
    possible_pawn_move = []
    possible_pawn_capture = []

    def whitepawnrightcapture():

        x = pickfile
        y = pickrank

        if ord(x) <= 71 and int(y) <= 7:
            y = int(y) + 1
            x = str(chr(ord(x) + 1))

            try:

                if PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                    ValidPawnMovement.possible_pawn_capture.append(f'{x}{y}')

            except IndexError:
                pass

    def whitepawnleftcapture():

        x = pickfile
        y = pickrank

        if ord(x) >= 66 and int(y) <= 7:
            y = int(y) + 1
            x = str(chr(ord(x) - 1))

            try:

                if PiecePosition.dic_chess[f"{x}{y}"][0] == 'b':
                    ValidPawnMovement.possible_pawn_capture.append(f'{x}{y}')

            except IndexError:
                pass

    def whitepawnup():

        x = pickfile
        y = pickrank

        if int(y) <= 7:
            y = int(y) + 1
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidPawnMovement.possible_pawn_move.append(f'{x}{y}')
            else:
                pass

    def whitepawnup2():

        x = pickfile
        y = pickrank

        if int(y) == 2:
            y = int(y) + 2
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidPawnMovement.possible_pawn_move.append(f'{x}{y}')
            else:
                pass

    def blackpawnrightcapture():

        x = pickfile
        y = pickrank

        if ord(x) <= 71 and int(y) <= 7:
            y = int(y) - 1
            x = str(chr(ord(x) + 1))

            try:

                if PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                    ValidPawnMovement.possible_pawn_capture.append(f'{x}{y}')

            except IndexError:
                pass

    def blackpawnleftcapture():

        x = pickfile
        y = pickrank

        if ord(x) >= 66 and int(y) <= 7:
            y = int(y) - 1
            x = str(chr(ord(x) - 1))

            try:

                if PiecePosition.dic_chess[f"{x}{y}"][0] == 'w':
                    ValidPawnMovement.possible_pawn_capture.append(f'{x}{y}')

            except IndexError:
                pass

    def blackpawnup():

        x = pickfile
        y = pickrank

        if int(y) <= 7:
            y = int(y) - 1
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidPawnMovement.possible_pawn_move.append(f'{x}{y}')
            else:
                pass

    def blackpawnup2():

        x = pickfile
        y = pickrank

        if int(y) == 7:
            y = int(y) - 2
            if PiecePosition.dic_chess[f"{x}{y}"] == '':
                ValidPawnMovement.possible_pawn_move.append(f'{x}{y}')
            else:
                pass


class DicCheck(ValidRookMovement, ValidPawnMovement, ValidKnightMovement, ValidBishopMovement, ValidKingMovement, ValidQueenMovement):

    def movecheck():


        dicmove =str(movecell[0] + movecell[1])
        global turn
        # if str(pickcell[0] + pickrank[0]) == dicmove:
        #     turn -= 1




#################################################################### ROOK

        if dicmove in ValidRookMovement.possible_rook_move:
            PiecePosition.movepiece()
            ValidRookMovement.possible_rook_move = []
            ValidRookMovement.possible_rook_capture = []

        elif dicmove in ValidRookMovement.possible_rook_capture:
            PiecePosition.capture()
            ValidRookMovement.possible_rook_capture = []
            ValidRookMovement.possible_rook_move = []

        else:


#################################################################### BISHOP

            if dicmove in ValidBishopMovement.possible_bishop_move:
                PiecePosition.movepiece()
                ValidBishopMovement.possible_bishop_move = []
                ValidBishopMovement.possible_bishop_capture = []

            elif dicmove in ValidBishopMovement.possible_bishop_capture:
                PiecePosition.capture()
                ValidBishopMovement.possible_bishop_capture = []
                ValidBishopMovement.possible_bishop_move = []

            else:

    #################################################################### KNIGHT

                if dicmove in ValidKnightMovement.possible_knight_move:
                    PiecePosition.movepiece()
                    ValidKnightMovement.possible_knight_move = []
                    ValidKnightMovement.possible_knight_capture = []

                elif dicmove in ValidKnightMovement.possible_knight_capture:
                    PiecePosition.capture()
                    ValidKnightMovement.possible_knight_capture = []
                    ValidKnightMovement.possible_knight_move = []

                else:


        #################################################################### QUEEN


                    if dicmove in ValidQueenMovement.possible_queen_move:
                        PiecePosition.movepiece()
                        ValidQueenMovement.possible_queen_move = []
                        ValidQueenMovement.possible_queen_capture = []

                    elif dicmove in ValidQueenMovement.possible_queen_capture:
                        PiecePosition.capture()
                        ValidQueenMovement.possible_queen_capture = []
                        ValidQueenMovement.possible_queen_move = []

                    else:


            #################################################################### KING

                        if dicmove in ValidKingMovement.possible_king_move:
                            PiecePosition.movepiece()
                            ValidKingMovement.possible_king_move = []
                            ValidKingMovement.possible_king_capture = []
                        elif dicmove in ValidKingMovement.possible_king_capture:
                            PiecePosition.capture()
                            ValidKingMovement.possible_king_capture = []
                            ValidKingMovement.possible_king_move = []
                        else:


                #################################################################### PAWN

                            if dicmove in ValidPawnMovement.possible_pawn_move:
                                PiecePosition.movepiece()
                                ValidPawnMovement.possible_pawn_move = []
                                ValidPawnMovement.possible_pawn_capture = []
                            elif dicmove in ValidPawnMovement.possible_pawn_capture:
                                PiecePosition.capture()
                                ValidPawnMovement.possible_pawn_capture = []
                                ValidPawnMovement.possible_pawn_move = []
                            else:
                                turn -= 1


    def squarecheck():
        pickfile = pickcell[0]
        pickrank = pickcell[1]
        dicpick = pickcell[0] + pickcell[1]

        if turn % 2 == 1:
            if PiecePosition.dic_chess[dicpick] == 'wrook1' or PiecePosition.dic_chess[dicpick] == 'wrook2':
                mp.whiterook()

            elif PiecePosition.dic_chess[dicpick] == 'wbishop1' or PiecePosition.dic_chess[dicpick] == 'wbishop2':
                mp.whitebishop()


            elif PiecePosition.dic_chess[dicpick] == 'wknight1' or PiecePosition.dic_chess[dicpick] == 'wknight2':
                mp.whiteknight()


            elif PiecePosition.dic_chess[dicpick] == 'wqueen':
                mp.whitequeen()


            elif PiecePosition.dic_chess[dicpick] == 'wking':
                mp.whiteking()


            elif PiecePosition.dic_chess[dicpick] == 'wpawn1' or PiecePosition.dic_chess[dicpick] == 'wpawn2' or \
                    PiecePosition.dic_chess[dicpick] == 'wpawn3' or PiecePosition.dic_chess[dicpick] == 'wpawn4' or \
                    PiecePosition.dic_chess[dicpick] == 'wpawn5' or PiecePosition.dic_chess[dicpick] == 'wpawn6' or \
                    PiecePosition.dic_chess[dicpick] == 'wpawn7' or PiecePosition.dic_chess[dicpick] == 'wpawn8':
                mp.whitepawn()

            else:
                pass

        elif turn % 2 == 0:
            if PiecePosition.dic_chess[dicpick] == 'brook1' or PiecePosition.dic_chess[dicpick] == 'brook2':
                mp.blackrook()


            elif PiecePosition.dic_chess[dicpick] == 'bbishop1' or PiecePosition.dic_chess[dicpick] == 'bbishop2':
                mp.blackbishop()


            elif PiecePosition.dic_chess[dicpick] == 'bknight1' or PiecePosition.dic_chess[dicpick] == 'bknight2':
                mp.blackknight()


            elif PiecePosition.dic_chess[dicpick] == 'bqueen':
                mp.blackqueen()


            elif PiecePosition.dic_chess[dicpick] == 'bking':
                mp.blackking()


            elif PiecePosition.dic_chess[dicpick] == 'bpawn1' or PiecePosition.dic_chess[dicpick] == 'bpawn2' or\
                    PiecePosition.dic_chess[dicpick] == 'bpawn3' or PiecePosition.dic_chess[dicpick] == 'bpawn4' or\
                    PiecePosition.dic_chess[dicpick] == 'bpawn5' or PiecePosition.dic_chess[dicpick] == 'bpawn6' or \
                    PiecePosition.dic_chess[dicpick] == 'bpawn7' or PiecePosition.dic_chess[dicpick] == 'bpawn8':
                mp.blackpawn()


            else:
                pass
        else:
            pass


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
    turn = 1
    def call_cell(self, r, f):
        if Cells.position is None and Cells.turn % 2 == 1:
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

            global movecell
            movecell = position2
            global movefile
            movefile = movecell[0]
            global moverank
            moverank = movecell[1]
            global turn

            self.movecheck()
            turn += 1

            if PiecePosition.dic_chess[movecell] != '':
                main.chess_board()

            Cells.position = None


bm = ValidBishopMovement
rm = ValidRookMovement
pm = ValidPawnMovement
nm = ValidKnightMovement
qm = ValidQueenMovement
km = ValidKingMovement
mp = PieceRules
pp = PiecePosition
square = Cells
dc = DicCheck
main = Chess
turn = 1
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
                                                                                                              y=375)
print(square.position)
root.mainloop()
