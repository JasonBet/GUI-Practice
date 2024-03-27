import tkinter as tk
from PIL import ImageTk,Image
from tkinter import filedialog

root = tk.Tk()
root.title("Windows")
root.iconbitmap('C:/Users/jason/Documents/Python/GUI/Practice/GUI-Practice/business.ico')

def open():
	global my_image
	root.filename = filedialog.askopenfilename(initialdir=
	"C:/Users/jason/Documents/Python/GUI/Practice/GUI-Practice/images",
	title="Select A File",filetypes=(("jpg files","*jpg"),("all files", "*.*")))
	my_label = tk.Label(root,text=root.filename).pack()
	my_image = ImageTk.PhotoImage(Image.open(root.filename))
	my_image_label = tk.Label(image=my_image).pack()

my_btn = tk.Button(root,text="Open File",command=open).pack()











root.mainloop()