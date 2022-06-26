from contents import razor, diluc, barbara

from tkinter import *
from time import *

w, h = 600, 600

program = Tk()
program.resizable(width = False, height = False)
program.title("Skor Anda")

screen_width = program.winfo_screenwidth()
screen_height = program.winfo_screenheight()

pos_top = int(screen_height / 2 - h / 2)
pos_right = int(screen_width / 2 - w / 2)

program.geometry(f"{w}x{h}+{pos_right}+{pos_top-50}")

cnv = Canvas(program, width=w, height=h)
cnv.pack()

background_img = PhotoImage(file='endgame.png')
background = cnv.create_image(0,0,image=background_img,anchor=NW)

score = razor.score + diluc.score + barbara.score

def score_statement():
    if score == 30:
        cnv.create_text(w/2+2, (h-150)/2+2, text=f'Skormu adalah {score}! Skor terbaik', fill="black", font=('Impact', 30), anchor=CENTER)
        cnv.create_text(w/2, (h-150)/2, text=f'Skormu adalah {score}! Skor terbaik', fill="white", font=('Impact', 30), anchor=CENTER)
    elif 20 <= score <= 30:
        cnv.create_text(w/2+2, (h-150)/2+2, text=f'Skormu adalah {score}! Tetap semangat', fill="black", font=('Impact', 30), anchor=CENTER)
        cnv.create_text(w/2, (h-150)/2, text=f'Skormu adalah {score}! Tetap semangat', fill="white", font=('Impact', 30), anchor=CENTER)
    elif 0 <= score <= 20:
        cnv.create_text(w/2+2, (h-150)/2+2, text=f'Skormu {score}! Sulit ya? Sama aku juga kok wkwk!', fill="black", font=('Impact', 20), anchor=CENTER)
        cnv.create_text(w/2, (h-150)/2, text=f'Skormu {score}! Sulit ya? Sama aku juga kok wkwk!', fill="white", font=('Impact', 20), anchor=CENTER)           
    else:
        cnv.create_text(w/2+2, (h-150)/2+2, text=f'Skor totalmu adalah {score}!', fill="black", font=('Impact', 30), anchor=CENTER)
        cnv.create_text(w/2, (h-150)/2, text=f'Skor totalmu adalah {score}!', fill="white", font=('Impact', 30), anchor=CENTER)

score_statement()

cnv.create_text(w/2+2, (h-50)/2+2, text='Terimakasih telah bermain', fill="black", font=('Impact', 30), anchor=CENTER)
cnv.create_text(w/2, (h-50)/2, text='Terimakasih telah bermain', fill="white", font=('Impact', 30), anchor=CENTER)
cnv.create_text(w/2+2, (h+500)/2+2, text='Semua yang ada dalam game ini terinspirasi dari game', fill="black", font=('Impact', 15), anchor=CENTER)
cnv.create_text(w/2, (h+500)/2, text='Semua yang ada dalam game ini terinspirasi dari game', fill="white", font=('Impact', 15), anchor=CENTER)
cnv.create_text(w/2+2, (h+550)/2+2, text='Genshin Impact (c) Hoyoverse', fill="black", font=('Impact', 15), anchor=CENTER)
cnv.create_text(w/2, (h+550)/2, text='Genshin Impact (c) Hoyoverse', fill="white", font=('Impact', 15), anchor=CENTER)

program.mainloop()