import tkinter as tk
from PIL import ImageTk,Image
import sqlite3

root = tk.Tk()
root.title("Data Base")
root.iconbitmap('C:/Users/jason/Documents/Python/GUI/Practice/GUI-Practice/business.ico')
root.geometry("400x400")


# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

'''
# Create table
c.execute("""CREATE TABLE addresses (
		first_name text,
		last_name text,
		address text,
		city text,
		state text,
		zipcode integer
		)""")
'''

# Create submit function
def submit():
	# Create a database or connect to one
	conn = sqlite3.connect('address_book.db')
	# Create cursor
	c = conn.cursor()

	# Insert into table
	c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
		{
			'f_name': f_name.get(),
			'l_name': l_name.get(),
			'address': address.get(),
			'city': city.get(),
			'state': state.get(),
			'zipcode': zipcode.get()
		})

	# Commit changes
	conn.commit()

	# Close connection
	conn.close()

	# clear text boxes
	f_name.delete(0,tk.END)
	l_name.delete(0,tk.END)
	address.delete(0,tk.END)
	city.delete(0,tk.END)
	state.delete(0,tk.END)
	zipcode.delete(0,tk.END)

# Create query function
def query():
	return

# Create text boxes
f_name = tk.Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)

l_name = tk.Entry(root,width=30)
l_name.grid(row=1,column=1)

address = tk.Entry(root,width=30)
address.grid(row=2,column=1)

city = tk.Entry(root,width=30)
city.grid(row=3,column=1)

state = tk.Entry(root,width=30)
state.grid(row=4,column=1)

zipcode = tk.Entry(root,width=30)
zipcode.grid(row=5,column=1)

# Create text box labels
f_name_label = tk.Label(root, text="First Name")
f_name_label.grid(row=0,column=0)

l_name_label = tk.Label(root, text="Last Name")
l_name_label.grid(row=1,column=0)

address_label = tk.Label(root, text="Address")
address_label.grid(row=2,column=0)

city_label = tk.Label(root, text="City")
city_label.grid(row=3,column=0)

state_label = tk.Label(root, text="State")
state_label.grid(row=4,column=0)

zipcode_label = tk.Label(root, text="Zipcode")
zipcode_label.grid(row=5,column=0)

# Create submit button
submit_btn = tk.Button(root,text="Add Record To Database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

# Create query button
query_btn = tk.Button(root,text="Show Records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()