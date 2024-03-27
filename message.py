import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox

root = tk.Tk()
root.title("Message Boxes")
root.iconbitmap('C:/Users/jason/Documents/Python/GUI/Practice/GUI-Practice/business.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
	response = messagebox.askyesno("This is my popup!", "Hello World")
	tk.Label(root,text=response).pack()
	if response ==1:
		tk.Label(root,text="You clicked yes").pack()
	else:
		tk.Label(root,text="You clicked no").pack()

tk.Button(root,text="Popup",command=popup).pack()









root.mainloop()