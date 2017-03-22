from tkinter import *
from tkinter.messagebox import showinfo
import shelve
from person import Person

shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'pay', 'job')

def makeWidgets():
    global entries
    mainwin = Tk()
    mainwin.title('People Shelve')
    form = Frame(mainwin)
    form.pack()
    entries = {}
    for (ix, label) in enumerate(('key',)+fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row = ix, column = 0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    Button(mainwin, text="Fetch", command=fetch).pack(side=LEFT)
    Button(mainwin, text="Update", command=update).pack(side=RIGHT)
    return mainwin

def fetch():
    key = entries['key'].get()
    try:
        record = db[key]
    except:
        showinfo(title='error', message='no such key %s !' % key)
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))

def update():
    key = entries['key'].get()
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
    db[key]=record

db = shelve.open(shelvename)
mainwin = makeWidgets()
mainwin.mainloop()
db.close()
