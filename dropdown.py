import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title("Drop Boxes")
root.iconbitmap('C:/Users/jason/Documents/Python/GUI/Practice/GUI-Practice/business.ico')
root.geometry("400x400")


# Dropdown Boxes

def show():
	myLabel = tk.Label(root,text=clicked.get()).pack()

options = [
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday"
]

clicked = tk.StringVar()
clicked.set(options[0])

drop = tk.OptionMenu(root,clicked,*options)
drop.pack()

myButton = tk.Button(root,text="Show Selection",command=show).pack()





root.mainloop()