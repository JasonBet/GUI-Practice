import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title("Image Viewer")
root.iconbitmap('C:/Users/jason/Documents/Python/GUI/Practice/GUI-Practice/business.ico')

my_img1 = ImageTk.PhotoImage(Image.open("images/beach.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/bed.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/coffee.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/friend.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/water.jpg"))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]



my_label = tk.Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = tk.Label(image=image_list[image_number-1])
	button_forward = tk.Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = tk.Button(root, text="<<", command=lambda: back(image_number-1))

	if image_number == 5:
		button_forward = tk.Button(root, text=">>", state=tk.DISABLED)

	my_label.grid(row=0,column=0,columnspan=3)
	button_back.grid(row=1,column=0)
	button_forward.grid(row=1,column=2)

def back(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = tk.Label(image=image_list[image_number-1])
	button_forward = tk.Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = tk.Button(root, text="<<", command=lambda: back(image_number-1))

	if image_number == 1:
		button_back = tk.Button(root, text="<<", state=tk.DISABLED)

	my_label.grid(row=0,column=0,columnspan=3)
	button_back.grid(row=1,column=0)
	button_forward.grid(row=1,column=2)

button_back = tk.Button(root, text="<<", command=back, state=tk.DISABLED)
button_exit = tk.Button(root, text="Exit Program", command = root.quit)
button_forward = tk.Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)





root.mainloop()