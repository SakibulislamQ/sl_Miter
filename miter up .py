# main miter >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
''' 1 miter = 39.37007874 inchi
    1 foot = 12 inchi
    1 cm = 0.03280839895 inchi
    1 inchi = 1 inchi
'''
def conv(num, froms, tos): # conv 'fron' to 'to'
    if froms == 'Meter':
        main_num = num / 39.37007874

    if froms == 'Feet':
        main_num = num / 12

    if froms == 'Centimetre':
        main_num = num / 0.03280839895

    if froms == 'Inch':
        main_num = num / 1

    if tos == 'Meter':
        oupts = main_num * 39.37007874
        return oupts
    if tos == 'Feet':
        oupts = main_num * 12
        return oupts
    if tos == 'Centimetre':
        oupts = main_num * 0.03280839895
        return oupts
    if tos == 'Inch':
        oupts = main_num * 1
        return oupts
# main miter <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  

# making main window >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

from tkinter import * # importing module
from tkinter.ttk import Combobox

win = Tk() # making window 
# designimg window >>>>>
win.title('Meter')
win.geometry('700x300')
win.attributes('-topmost',1)
win.configure(bg='SkyBlue')
win.resizable(0,0)
# designing window <<<<
# making From text
from_label = Label(win, text='From', font=('Arial',20),bg='SkyBlue', fg='red')
from_label.place(x=120,y=40)
# making To text
to_label = Label(win, text='To', font=('Arial',20),bg='SkyBlue', fg='red')# From text 
to_label.place(x=400,y=40)
# making from combobox >>>>
from_combo = Combobox(win,width=30)
from_combo['values']=('Meter','Feet','Centimetre','Inch')
from_combo.current(0)# set the selected items
from_combo['state']='readonly'
from_combo.place(x=120,y=80)

# making to combobox >>>>
to_combo = Combobox(win, width=30)
to_combo['values']=('Meter','Feet','Centimetre','Inch')
to_combo.current(1)# set the selected items
to_combo['state']='readonly'
to_combo.place(x=400,y=80)

# input num >>>>
inp_num = Entry(win, bd=0)
inp_num.place(x=300, y=120)

# making button click
def btn_cl():
    _from = from_combo.get()
    _to = from_combo.get()
    _imp = float(inp_num.get())
    result = conv(_imp, _from, _to)
    outp.configure(text=result)
# making oupt
outp = Label(win, text='', font=('Calibri Light bold',20), bg='SkyBlue', fg='red3')
outp.place(x=320,y=210)
# Go button
go_button = Button(win, text='Go', font=('Arial bold', 12),bg='red', bd=0, command=btn_cl)
go_button.place(x=350,y=150)

win.mainloop() # window mainloop
# making main window <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<







