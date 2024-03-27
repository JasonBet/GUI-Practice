import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title("Windows")
root.iconbitmap('C:/Users/jason/Documents/Python/GUI/Practice/GUI-Practice/business.ico')

def open():
	global my_img
	top = tk.Toplevel()
	top.title("My Second Window")
	top.iconbitmap('C:/Users/jason/Documents/Python/GUI/Practice/GUI-Practice/business.ico')
	my_img = ImageTk.PhotoImage(Image.open("images/friend.jpg"))
	my_label = tk.Label(top,image=my_img).pack()
	btn2 = tk.Button(top,text="close window",command=top.destroy).pack()

btn = tk.Button(root,text="Open Second Window",command=open).pack()


root.mainloop()