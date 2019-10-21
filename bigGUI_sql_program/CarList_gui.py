import tkinter as tk
import CarList_backend

def command_view():
    list1.delete(0, 500)
    for row in CarList_backend.view():
        list1.insert(0,row)

def command_serach():
        list1.delete(0, 500)
        for row in CarList_backend.search(e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get()):
             list1.insert(0,row)
def command_add():
        CarList_backend.add_row(e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get())
        command_view()
        
def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    print(selected_tuple)

def command_delete():
    CarList_backend.delete(selected_tuple[0])
    command_view()

window=tk.Tk()

l1=tk.Label(window,text="Brand:")
l1.grid(row=0,column=0)

l2=tk.Label(window,text="Model:")
l2.grid(row=0,column=2)

l3=tk.Label(window,text="Year:")
l3.grid(row=1,column=0)

l4=tk.Label(window,text="Number:")
l4.grid(row=1,column=2)

###

e1_val=tk.StringVar()
e1=tk.Entry(window,textvariable=e1_val)
e1.grid(row=0,column=1)

e2_val=tk.StringVar()
e2=tk.Entry(window,textvariable=e2_val)
e2.grid(row=0,column=3)

e3_val=tk.IntVar()
e3=tk.Entry(window,textvariable=e3_val)
e3.grid(row=1,column=1)

e4_val=tk.StringVar()
e4=tk.Entry(window,textvariable=e4_val)
e4.grid(row=1,column=3)

###list



list1=tk.Listbox(window, height=10 ,width=30)
list1.grid(row=2, column=0 ,rowspan=6,columnspan=2)

sb1=tk.Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)#used in delete

b1=tk.Button(window,text="View all",width=12, command=command_view)
b1.grid(row=2,column=3)

b2=tk.Button(window,text="Search entry",width=12,command=command_serach)
b2.grid(row=3,column=3)

b3=tk.Button(window,text="Add entry",width=12,command=command_add)
b3.grid(row=4,column=3)

b4=tk.Button(window,text="Update selected",width=12)
b4.grid(row=5,column=3)

b5=tk.Button(window,text="Delete selected",width=12,command=command_delete)
b5.grid(row=6,column=3)

b6=tk.Button(window,text="Close",width=12)
b6.grid(row=7,column=3)

window.mainloop()