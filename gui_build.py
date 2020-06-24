from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
window = Tk()
frame=Frame(window)
frame.pack()
window.title("My Accounts - Welcome!")
label=Label(window,text="Welcome, Lets Begin!!",font=("Calibri",50))
#label.grid(column=0,row=0)
#window.geometry('700x620')

def buttonClick():
    res=" Action: Button Clicked, " + txtBox.get() +"!!!!";
    label.configure(text=res)


button=Button(frame,text="Add",font=("Calibri",25),bg="green",fg="white",command=buttonClick)
#button.grid(column=1,row=200)
button.pack(side=LEFT)


txtBox=Entry(frame,width=10);
#txtBox.grid(column=0,row=10);
txtBox.pack(side=LEFT)
txtBox.focus();

def comboSel(*args):
    selection=comboBox.get();
    messagebox.showinfo("Item from comboBox", selection);


comboBox = Combobox(frame)
comboBox['values']=("Rent", "Gas", "Grocery", "Others")
comboBox.current(0)
#comboBox.grid(column=0, row=8000)
comboBox.pack(side=LEFT)
comboBox.bind("<<ComboboxSelected>>", comboSel)
#comboBox.get();
#messagebox.showinfo("Item from comboBox",comboBox.get());



window.mainloop()