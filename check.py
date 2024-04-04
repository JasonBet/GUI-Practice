import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title("Check Boxes")
root.iconbitmap('C:/Users/jason/Documents/Python/GUI/Practice/GUI-Practice/business.ico')
root.geometry("400x400")

def show():
	myLabel = tk.Label(root,text=var.get()).pack()

var = tk.StringVar()

c = tk.Checkbutton(root,text="Check this box",variable=var, onvalue="On",offvalue="Off")
c.deselect()
c.pack()

myButton = tk.Button(root,text="Show Selection",command=show)
myButton.pack()


root.mainloop()