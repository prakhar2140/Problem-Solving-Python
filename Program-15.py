from tkinter import *
import time 
import sys
master =Tk()
master.title("Digital clock")
def get_time():
    timevar = time.strftime("%I:%M:%S %p")
    clock.config(text = timevar)
    clock.after(200,get_time)

clock = Label(master,font=("Calibari",90),bg="black",fg="yellow")
clock.pack()
get_time()
master.mainloop()    