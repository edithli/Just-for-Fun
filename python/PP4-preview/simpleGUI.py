from tkinter import *
from tkinter.messagebox import showinfo

def tkinter000():
    Label(text='spam').pack()
    mainloop()

def tkinter001():
    def reply():
        showinfo(title='popup', message='button pressed')
    window = Tk()
    button = Button(window, text='press', command=reply)
    button.pack()
    window.mainloop()

class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='press', command=self.reply)
        button.pack()
    def reply(self):
        showinfo(title='popup', message='button pressed')

def attachFrame():
    mainwin = Tk()
    Label(mainwin, text=__name__).pack()
    popup = Toplevel()
    Label(popup, text='attached').pack(side=LEFT)
    MyGui(popup).pack(side=RIGHT)
    mainwin.mainloop()

class CustomGui(MyGui):
    def __init__(self, parent=None):
        MyGui.__init__(self, parent)
    def reply(self):
        showinfo(title='popup', message='Ouch')
    
def displayCustomGui():
    CustomGui().pack()
    mainloop()
        
#if __name__ == '__main__':
    # window = MyGui()
    # window.pack()
    # window.mainloop()

def tkinter002():
    def reply(name):
        showinfo(title='popup', message='hello %s' % name)
    mainwin = Tk()
    mainwin.title('Echo')
    # mainwin.iconbitmap('py-blue-tran-out.ico')
    Label(text='enter your name').pack(side=TOP)
    ent = Entry(mainwin)
    ent.pack(side=TOP)
    button = Button(mainwin, text='Enter', comman=(lambda: reply(ent.get())))
    button.pack(side=LEFT)
    mainwin.mainloop()
