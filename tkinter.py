from tkinter import *

def click_me():
	x = Label( root , text = "HAPPY BIRTHDAY SELVA")
	x.pack()

root = Tk()
label = Label( root , text = "HELLO SELVA SURPRICE!", font = ("courier", 30), bg = "red", fg = "blue", width = "50", height = "4")
label.pack()
button = Button( root , text = "Click Me", font = ("courier", 40), bg = "yellow", fg = "purple", activebackground = "orange", activeforeground = "green", command = click_me)
button.pack()
root.mainloop()
