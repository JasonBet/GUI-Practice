import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title("Slider")
root.iconbitmap('C:/Users/jason/Documents/Python/GUI/Practice/GUI-Practice/business.ico')
root.geometry("400x400")

vertical = tk.Scale(root,from_=0,to=200)
vertical.pack()

def slide():
	my_label = tk.Label(root,text=horizontal.get()).pack()
	root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

horizontal = tk.Scale(root,from_=0,to=400,orient=tk.HORIZONTAL)
horizontal.pack()

my_btn = tk.Button(root,text="Click Me",command=slide).pack()

root.mainloop()