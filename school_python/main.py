from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DbConnect import StudentsData

dbconnect=StudentsData()
root=Tk()
root.title("students information ")
#Style
style=ttk.Style()
style.configure('TButton', background="#ffcc55")
style.configure('TLabel', background="#44ddd9")
style.configure('TCombobox', background="#44ddd9")
style.configure('TRadiobutton',background="#44ddd9",forground="#cfc458")
root.configure( background="#44ddd9")


# the saving data functions:
def saveData():
 
    try:
        msg=dbconnect.Add(StudentfName.get(),StudentlName.get(),spanSection.get(),combotext.get())
        messagebox.showinfo(title='students information', message=msg)
    except :
        msg1="Plese try again!"
        messagebox.showerror(title='students information', message=msg1)


    StudentfName.delete(0,'end')
    StudentlName.delete(0,'end')
    StudentNumber.delete(0,'end')
# show the information from database
def ShowList():
    from  ShowList import StudentList
    StudentList()

#the first name
ttk.Label(root,text="Student first name :").grid(row=0,column=0,padx=1,pady=1)
StudentfName=ttk.Entry(root,width=30,font=('Arial',16))
StudentfName.grid(column=1,row=0,columnspan=2,pady=1)




#the second name
ttk.Label(root,text="Student second name :").grid(row=1,column=0,padx=1,pady=1)
StudentlName=ttk.Entry(root,width=30,font=('Arial',16))
StudentlName.grid(column=1,row=1,columnspan=2,pady=1)



#the groupe cette classification par les groupes de TP
combotext = StringVar()
combotext.set('Select')
box = ttk.Combobox(root, textvariable=combotext, state='readonly')
box['values'] = ("TP1",
                 "TP2",
                 "TP3",
                 "TD1",
                 "TD2",
                 "TD3")
box.grid(row=4,column=0,padx=30,pady=1)




#the Section (GI:genie informatique TM:tecnique de managment)
ttk.Label(root,text="Student Studying section :").grid(row=3,column=0,padx=1,pady=1)
spanSection=StringVar()
ttk.Radiobutton(root,text="GI",variable=spanSection,value="GI").grid(row=4,column=1)
ttk.Radiobutton(root,text="TM",variable=spanSection,value="TM").grid(row=4,column=2)
#the submit and showList
submit=ttk.Button(root,text="Submit",command=saveData).grid(row=5,column=2)
showlist=ttk.Button(root,text="Show the list",command=ShowList).grid(row=5,column=4)






root.mainloop()
