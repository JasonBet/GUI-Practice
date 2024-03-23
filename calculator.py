import tkinter as tk

root = tk.Tk()

e = tk.Entry(root, width=50, bg="blue", fg="white", borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name: ")


def myClick():
    hello = "Hello " + e.get()
    myLabel = tk.Label(root, text=hello)
    myLabel.pack()

myButton = tk.Button(root, text="Enter your name", command=myClick)
myButton.pack()


root.mainloop()