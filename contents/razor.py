from tkinter import *
from time import *

w, h = 1280, 720

bgsrc = 'contents/wolvendom.png'
mrsrc = 'contents/mora.png'
chsrc = 'contents/razor.png'
hisrc = 'contents/hilichurl.png'

program = Tk()
program.resizable(width = False, height = False)
program.title("Razor Berburu Di Wolvendom")

screen_width = program.winfo_screenwidth()
screen_height = program.winfo_screenheight()

pos_top = int(screen_height / 2 - h / 2)
pos_right = int(screen_width / 2 - w / 2)

program.geometry(f"{w}x{h}+{pos_right}+{pos_top-50}")

cnv = Canvas(program, width=w, height=h)
cnv.pack()

background_img = PhotoImage(file=bgsrc)
background = cnv.create_image(0,0,image=background_img,anchor=NW)

class Props:
    def __init__(self, imgname, xpos, ypos, anchor):
        self.imgname = PhotoImage(file=imgname)
        self.xpos = xpos
        self.ypos = ypos
        self.anchor = anchor
        self.prop = cnv.create_image(xpos, ypos, image=self.imgname, anchor=anchor)

    def xbrake(self):
        xbrake = self.imgname.width()
        return xbrake

    def ybrake(self):
        ybrake = self.imgname.width()
        return ybrake

    def walk(self, xspeed, yspeed):
        cnv.move(self.prop, xspeed, yspeed)

    def hide(self):
        cnv.itemconfigure(self.prop, state=HIDDEN)

    def show(self):
        cnv.itemconfigure(self.prop, state=NORMAL)

    def coords(self):
        return cnv.coords(self.prop)

charx_pos = 0
chary_pos = 550
charx_speed = 0
chary_speed = 0

hili1y_speed = 1
hili2x_speed = 1
hili3y_speed = 1
hili4x_speed = -1
hili5x_speed = 1

def goup(args):
    global chary_speed
    global charx_speed
    chary_speed += -3
    charx_speed = 0

def godown(args):
    global chary_speed
    global charx_speed
    chary_speed += 3
    charx_speed = 0

def goright(args):
    global charx_speed
    global chary_speed
    charx_speed += 3
    chary_speed = 0

def goleft(args):
    global charx_speed
    global chary_speed
    charx_speed += -3
    chary_speed = 0

def stop(args):
    global charx_speed
    global chary_speed
    charx_speed = 0
    chary_speed = 0

mora1 = Props(mrsrc, 1000, 625, NW)
mora2 = Props(mrsrc, 1000, 250, NW)
mora3 = Props(mrsrc, 825, 225, NW)
mora4 = Props(mrsrc, 500, 50, NW)
mora5 = Props(mrsrc, 50, 100, NW)
mora6 = Props(mrsrc, 450, 500, NW)
mora7 = Props(mrsrc, 100, 400, NW)
mora8 = Props(mrsrc, 1100, 500, NW)
mora9 = Props(mrsrc, 1150, 350, NW)
mora10 = Props(mrsrc, 1100, -10, NW)
hilichurl1 = Props(hisrc, 1200, 100, NW)
hilichurl2 = Props(hisrc, 850, 10, NW)
hilichurl3 = Props(hisrc, 500, 300, NW)
hilichurl4 = Props(hisrc, 200, -50, NW)
hilichurl5 = Props(hisrc, 800, 600, NW)

char = Props(chsrc, charx_pos, chary_pos, NW)

score = 0
score_text_bg = cnv.create_text(7, 2, text=f'Skor: {score}', fill="black", font=('Impact', 30), anchor=NW)
score_text_fg = cnv.create_text(5, 0, text=f'Skor: {score}', fill="white", font=('Impact', 30), anchor=NW)

def addscore():
    global score
    global score_text
    score += 1
    cnv.itemconfigure(score_text_bg, text=f'Skor: {score}')
    cnv.itemconfigure(score_text_fg, text=f'Skor: {score}')

def showscore():
    global score
    global score_text
    cnv.itemconfigure(score_text_bg, state=HIDDEN)
    cnv.itemconfigure(score_text_fg, state=HIDDEN)
    if score == 10:
        cnv.create_text(w/2+2, h/2+2, text=f'Kamu menang dengan skor {score}!', fill="black", font=('Impact', 30), anchor=CENTER)
        cnv.create_text(w/2, h/2, text=f'Kamu menang dengan skor {score}!', fill="white", font=('Impact', 30), anchor=CENTER)
    else:
        cnv.create_text(w/2+2, h/2+2, text=f'Kamu digebuk Hilichurl, Skormu {score}', fill="black", font=('Impact', 30), anchor=CENTER)
        cnv.create_text(w/2, h/2, text=f'Kamu digebuk Hilichurl, Skormu {score}', fill="white", font=('Impact', 30), anchor=CENTER)

def hideall():
    char.hide()
    for i in range(1, 5+1):
        eval(f'hilichurl{i}.hide()')
    for j in range(1, 10+1):
        eval(f'mora{j}.hide()')

def start():
    global charx_speed
    global chary_speed
    global hili1y_speed
    global hili2x_speed
    global hili3y_speed
    global hili4x_speed
    global hili5x_speed
    try:
        while True:
            p = cnv.bbox(char.prop)
            coll = cnv.find_overlapping(p[0], p[1], p[2], p[3])
            print(coll)
            if char.coords()[0] >= w-char.xbrake() or char.coords()[0] < 0:
                charx_speed = -charx_speed
            if char.coords()[1] >= h-char.ybrake()-25 or char.coords()[1] < 0:
                chary_speed = -chary_speed

            if hilichurl1.coords()[1] > 250 or hilichurl1.coords()[1] < 5:
                hili1y_speed = -hili1y_speed
            if hilichurl2.coords()[0] > 1000 or hilichurl2.coords()[0] < 825:
                hili2x_speed = -hili2x_speed
            if hilichurl3.coords()[1] > 400 or hilichurl3.coords()[1] < 90:
                hili3y_speed = -hili3y_speed
            if hilichurl4.coords()[0] > 201 or hilichurl4.coords()[0] < 25:
                hili4x_speed = -hili4x_speed
            if hilichurl5.coords()[0] > 1000 or hilichurl5.coords()[0] < 425:
                hili5x_speed = -hili5x_speed
            
            # Mendeteksi Collision / Overlapping Berdasarkan Checking Array dan Pemanggilan Method dengan Eval
            for i in range(2, 12):
                if coll[1] == i:
                    eval(f'mora{i-1}.hide()')
                    addscore()
            for j in range(12, 16+1):
                if coll[1] == j:
                    hideall()
                    showscore()
            if score == 10:
                showscore()
                char.walk(0, 0)
                char.hide()
                break
            
            char.walk(charx_speed, chary_speed)
            hilichurl1.walk(0, hili1y_speed)
            hilichurl2.walk(hili2x_speed, 0)
            hilichurl3.walk(0, hili3y_speed)
            hilichurl4.walk(hili4x_speed, 0)
            hilichurl5.walk(hili5x_speed, 0)
            program.bind('<Up>', goup)
            program.bind('<Down>', godown)
            program.bind('<Right>', goright)
            program.bind('<Left>', goleft)
            program.bind('<space>', stop)
            program.update()
            sleep(0.01)
    except TclError:
        pass
    except TypeError:
        pass

start()
program.mainloop()