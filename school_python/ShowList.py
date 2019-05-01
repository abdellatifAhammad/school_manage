from tkinter import *
from tkinter import ttk
from DbConnect import StudentsData
dbconnect=StudentsData()


class StudentList():
    def __init__(self):
        self._root=Tk()
        self._dbconnect = StudentsData()
        self.tv=ttk.Treeview(self._root)
        self.tv.pack()
        self.tv.heading('#0',text='Number')
        self.tv.configure(column=('#FirstName', '#LastName', '#Section', '#Class'))
        self.tv.heading('#FirstName', text='FirstName')
        self.tv.heading('#LastName', text='LastName')
        self.tv.heading('#Section', text='Section')
        self.tv.heading('#Class', text='Class')
        cursor=self._dbconnect.ListInfo()
        for row in cursor:
            self.tv.insert('','end','#{}'.format(row['Number']),text=row['Number'])
            self.tv.set('#{}'.format(row['Number']),'#FirstName',row['FirstName'])
            self.tv.set('#{}'.format(row['Number']),'#LastName',row['LastName'])
            self.tv.set('#{}'.format(row['Number']),'#Section',row['Section'])
            self.tv.set('#{}'.format(row['Number']),'#Class',row['Class'])

        self._root.mainloop()