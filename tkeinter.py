import tkinter
from board import Board

board = Board
root = tkinter.Tk()
root.title(u"オセロ")
root.geometry("1000x1000")


button = tkinter.Button(text=u'ボタンです')
button.pack()


def click():
    Static1 = tkinter.Message(text=board)
    Static1.pack()


button["command"] = click

root.mainloop()
