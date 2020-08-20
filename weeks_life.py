from tkinter import Tk, Canvas
import datetime
from datetime import date
import math

mybirth = datetime.date(1996, 2, 5)
mydeath = datetime.date(2056, 2, 5)
today = date.today()
wlived = (today - mybirth).days // 7
tolive = (mydeath - today).days // 7
print('Total weeks to live:', wlived + tolive)
print('Weeks already lived:', wlived)
print('Weeks to live:', tolive)
x_side = int(math.sqrt((wlived + tolive)//12))
nrows = 3*x_side + 1
ncolumns = (wlived + tolive)//nrows + 1
print('squares in 1 row, no. of rows:', nrows, ncolumns)
master = Tk()
space = 4
side = 10
week = Canvas(master, width=nrows * (side + space) + side, height=ncolumns * (side + space) + side)
rowlive = wlived // nrows
pos = wlived - (rowlive * nrows)
print('position:', pos)
week.pack()


def rsquare(x, y):
    week.create_rectangle(x, y, x + side, y + side, fill="red", outline='black')


def bsquare(x, y):
    week.create_rectangle(x, y, x + side, y + side, fill="green", outline='black')


def row(x, y, j):
    for i in range(nrows):
        if j < rowlive + 1:
            rsquare(x, y)
            x = x + side + space
        elif j == rowlive + 1:
            for k in range(pos):
                rsquare(x, y)
                x = x + side + space
            for m in range(nrows - pos):
                bsquare(x, y)
                x = x + side + space
            break
        elif j > rowlive:
            bsquare(x, y)
            x = x + side + space


def column():
    x = 10
    y = 10
    j = 0
    for i in range(ncolumns):
        j = j + 1
        row(x, y, j)
        y = y + side + space


column()
week.postscript(file="tmp.eps")
master.mainloop()
