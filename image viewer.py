import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title("Simple Calculator")
root.iconbitmap('C:/Users/jason/Documents/Python/GUI/Practice/GUI-Practice/business.ico')

my_img1 = ImageTk.PhotoImage(Image.open("images/beach.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/bed.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/coffee.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/jason.jpeg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/water.jpg"))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]



my_label = tk.Label(image=my_img)
my_label.grid(row=0,column=0,columnspan=3)



button_back = tk.Button(root, text="<<")
button_exit = tk.Button(root, text="EXIT PROGRAM", command = root.quit)
button_forward = tk.Button(root, text=">>")

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)





root.mainloop()