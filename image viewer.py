import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title("Simple Calculator")
root.iconbitmap('C:/Users/jason/Documents/Python/GUI/Practice/GUI-Practice/business.ico')

my_img = ImageTk.PhotoImage(Image.open("beach.jpg"))
my_label = tk.Label(image=my_img)
my_label.pack()









button_quit = tk.Button(root, text="Exit Program", command=root.quit)
button_quit.pack()





root.mainloop()