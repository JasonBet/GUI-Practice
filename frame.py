import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title("Image Viewer")
root.iconbitmap('C:/Users/jason/Documents/Python/GUI/Practice/GUI-Practice/business.ico')

frame = tk.LabelFrame(root, text="This is my Frame...",padx=50,pady=50)
frame.pack(padx=10,pady=10)

b = tk.Button(frame,text="Don't click here")
b2 = tk.Button(frame,text="Click here")
b.grid(row=0,column=0)
b2.grid(row=1,column=1)






root.mainloop()
