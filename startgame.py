from tkinter import *
from tkinter.font import *
from time import *

w, h = 600, 600

program = Tk()
program.resizable(width = False, height = False)
program.title("Mulai Game")

screen_width = program.winfo_screenwidth()
screen_height = program.winfo_screenheight()

pos_top = int(screen_height / 2 - h / 2)
pos_right = int(screen_width / 2 - w / 2)

program.geometry(f"{w}x{h}+{pos_right}+{pos_top-50}")

cnv = Canvas(program, width=w, height=h)
cnv.pack()

buttonFont = Font(family='Impact', size=20)
btn = Button(program, text='Mulai Game!', font=buttonFont, width=15, height=1, bd='5', command=program.destroy, anchor=CENTER, fg="black")

btn.place(x=(w/2)-100, y=h/2)

background_img = PhotoImage(file='startgame.png')
background = cnv.create_image(0,0,image=background_img,anchor=NW)

class Props:
    def __init__(self, imgname, xpos, ypos, anchor):
        self.imgname = PhotoImage(file=imgname)
        self.xpos = xpos
        self.ypos = ypos
        self.anchor = anchor
        self.prop = cnv.create_image(xpos, ypos, image=self.imgname, anchor=anchor)

diluc = Props("contents/diluc.png", 450, 350, NW)
razor = Props("contents/razor.png", 0, 350, NW)
barbara = Props("contents/barbara.png", 225, 350, NW)

cnv.create_text(w/2+2, (h-550)/2+2, text='Selamat Datang Di Game', fill="black", font=('Impact', 30), anchor=CENTER)
cnv.create_text(w/2, (h-550)/2, text='Selamat Datang Di Game', fill="white", font=('Impact', 30), anchor=CENTER)
cnv.create_text(w/2+2, (h-450)/2+2, text='Razor, Diluc, Barbara Berburu Mora', fill="black", font=('Impact', 30), anchor=CENTER)
cnv.create_text(w/2, (h-450)/2, text='Razor, Diluc, Barbara Berburu Mora', fill="white", font=('Impact', 30), anchor=CENTER)
cnv.create_text(w/2+2, (h+500)/2+2, text='Semua yang ada dalam game ini terinspirasi dari game', fill="black", font=('Impact', 15), anchor=CENTER)
cnv.create_text(w/2, (h+500)/2, text='Semua yang ada dalam game ini terinspirasi dari game', fill="white", font=('Impact', 15), anchor=CENTER)
cnv.create_text(w/2+2, (h+550)/2+2, text='Genshin Impact (c) Hoyoverse', fill="black", font=('Impact', 15), anchor=CENTER)
cnv.create_text(w/2, (h+550)/2, text='Genshin Impact (c) Hoyoverse', fill="white", font=('Impact', 15), anchor=CENTER)

program.mainloop()

import endgame