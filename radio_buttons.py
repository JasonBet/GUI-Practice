import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title("Radio Buttons")
root.iconbitmap('C:/Users/jason/Documents/Python/GUI/Practice/GUI-Practice/business.ico')

r = tk.IntVar()
r.set("1")

def clicked(value):
	myLabel = tk.Label(root,text=value)
	myLabel.pack()

tk.Radiobutton(root,text="Option 1",variable=r, value=1,
	command=lambda: clicked(r.get())).pack()
tk.Radiobutton(root,text="Option 2",variable=r, value=2, 
	command=lambda: clicked(r.get())).pack()

myLabel = tk.Label(root,text=r.get())
myLabel.pack()






root.mainloop()