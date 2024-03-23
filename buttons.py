import tkinter as tk

root = tk.Tk()

def myClick():
    myLabel = tk.Label(root, text="Look! I clicked a Button!!")
    myLabel.pack()

myButton = tk.Button(root, text="Click Me!", command=myClick)
myButton.pack()


root.mainloop()