from tkinter import *
from tkinter import font
import datetime

def finish(*args):
    global win
    win.destroy() # window bondho kore dibe

def clock_Time():
    cTime=datetime.datetime.now()
    cTime=cTime.strftime('%H:%M:%S')
    txt.set(cTime)

    win.after(1000,clock_Time)

def toggleFullScreen(self,event=None):
    win.state=not win.state
    win.attributes('-fullscreen',win.state)
    return 'break'

    
win=Tk()
win.geometry('850x200')
win.title('Digital Clock')
win.resizable(False,False)
win.configure(background='Black')

win.bind('<Escape>',finish)
win.bind('<F11>',toggleFullScreen)
fnt=font.Font(family='Helvetica',size=120, weight='bold')
txt=StringVar()
# txt.set('hh:mm:ss pm')

lbl=Label(win,textvariable=txt,font=fnt,foreground='White', background='Black')
lbl.place(relx=0.5,rely=0.5,anchor=CENTER)

win.after(1000,clock_Time)
win.mainloop()
