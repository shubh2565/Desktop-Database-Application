# this code is for making a GUI for front end of the book store applications

from tkinter import *
import backend_code  # for using the database manipulation functions defined in backend_code file


# this function is used to store the selected entry in a variable and also to display the values of that entry in their respective places
def get_selected_row(event):
	try:
		global selected_tuple  # so that other functions can also use the value of selected entry
		index=list1.curselection()[0]  # to get the index of the selected entry
		selected_tuple=list1.get(index)
		e1.delete(0,END)
		e1.insert(END,selected_tuple[1])
		e2.delete(0,END)
		e2.insert(END,selected_tuple[2])
		e3.delete(0,END)
		e3.insert(END,selected_tuple[3])
		e4.delete(0,END)
		e4.insert(END,selected_tuple[4])
	except IndexError:
		pass


	

def view_command():
	list1.delete(0,END)
	for row in backend_code.view_all():
		list1.insert(END, row)


def search_command():
	list1.delete(0,END)
	for row in backend_code.search(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()):
		list1.insert(END, row)


def add_command():
	backend_code.add_entry(title_value.get(),author_value.get(),year_value.get(),isbn_value.get())
	list1.delete(0,END)
	list1.insert(END,(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()))


def delete_command():
	backend_code.delete(selected_tuple[0]) # to pass the id of the row which we want to delete


def update_command():
	backend_code.update(selected_tuple[0],title_value.get(),author_value.get(),year_value.get(),isbn_value.get())




window=Tk()

window.wm_title('Booklist')  # for assigning a title to our GUI app

l1=Label(window,text='Title')
l1.grid(row=0,column=0)  # pack method can also be used, but grid provides more control

l2=Label(window,text='Author')
l2.grid(row=0,column=2)

l3=Label(window,text='Year')
l3.grid(row=1,column=0)

l4=Label(window,text='ISBN')
l4.grid(row=1,column=2)

title_value=StringVar()
e1=Entry(window,textvariable=title_value)
e1.grid(row=0,column=1)

author_value=StringVar()
e2=Entry(window,textvariable=author_value)
e2.grid(row=0,column=3)

year_value=StringVar()
e3=Entry(window,textvariable=year_value)
e3.grid(row=1,column=1)

isbn_value=StringVar()
e4=Entry(window,textvariable=isbn_value)
e4.grid(row=1,column=3)

list1=Listbox(window,height=8,width=24)
list1.grid(row=2,column=0,rowspan=8,columnspan=2)

sb1=Scrollbar(window)     # for adding a scroll bar 
sb1.grid(row=2,column=2,rowspan=8)

list1.configure(yscrollcommand=sb1.set)  # for connecting the list box and scroll bar together so that they can work in sync
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)   

b1=Button(window,text='View All',width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text='Search entry',width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text='Add entry',width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text='Update',width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text='Delete',width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text='Close',width=12,command=window.destroy)  # for closing our GUI app
b6.grid(row=7,column=3)

window.mainloop()
