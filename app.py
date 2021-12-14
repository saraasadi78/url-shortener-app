import pyshorteners
from tkinter import *
from tkinter import messagebox
import webbrowser

window=Tk()
window.geometry('700x200')
window.title("URL SHORTNER")
window.config(bg='lightgreen')
t=Label(window, text='Enter url : ',bg="green",borderwidth=6)
t.pack()
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

def shorting_func():
    if 'http' in entered_url.get() or 'https' in entered_url.get():
        key = pyshorteners.Shortener()
        short_link = key.chilpit.short(entered_url.get())
        #print(short_link)

        o = Label(window, text='Here is your shorted URL : ', bg="green", borderwidth=2)
        o.pack()

        result = Entry(window ,width=55,borderwidth=6)
        result.insert(0, short_link)
        result.place(relx=0.5, rely=0.7)

    else:
        print('url is not valid enter again')


entered_url = Entry(window, width=80)
entered_url.place(relx=0.5, rely=0.2)

apply_button = Button(window,
                      text='apply',
                      width=10,
                      bg='#121212',
                      fg='yellow',
                      borderwidth=6,
                      command=shorting_func)

apply_button.place(relx=0.5, rely=0.4)

entered_url.pack()
apply_button.pack()

window.mainloop()
