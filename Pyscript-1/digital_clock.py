from tkinter import *
from tkinter import ttk
from time import strftime

digital_clock = Tk()
digital_clock.title("Digital Clock")

def time():
    string = strftime('%d %b %Y \n %A \n %H:%M:%S %p')
    label.config(text = string)
    label.after(1000,time)

label = Label(digital_clock,font=("ds-digital",100),background="black",foreground = "cyan")
label.pack(anchor= 'center')

time()

mainloop()
