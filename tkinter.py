from tkinter import *

def click_me():
	x = Label( root , text = "Welcome")
	x.pack()

root = Tk()
label = Label( root , text = "Hello Dheekshith!", font = ("courier", 40), bg = "red", fg = "blue", width = "50", height = "2")
label.pack()
button = Button( root , text = "Click Me", font = ("courier", 40), bg = "yellow", fg = "purple", activebackground = "orange", activeforeground = "green", command = click_me)
button.pack()
root.mainloop()
