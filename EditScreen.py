# Import the required libraries
from tkinter import *
import tkinter
import tkinter.font
from tkinter import ttk
import mysql.connector as mysql
from DAO import applicantDAO, programDAO, universitiesDAO

class EditApplicantScreen(tkinter.Tk):

    def __init__(self):
        # connect to database
        player_db = mysql.connect(
            host="35.245.211.180",
            user="root",
            password="EECE4520",
            database="player_db"
        )
        cursor = player_db.cursor()

        Tk.__init__(self)

        # Set the size of window
        self.geometry("650x650+100+100")
        self.title('Edit Applicants Screen')
        s = ttk.Style()
        s.theme_use('classic')

        self.read_entry = tkinter.Entry(self)
        self.read_button = tkinter.Button(self, text="READ", command=self.read_button)
        self.read_entry.pack()
        self.read_button.pack()

        self.del_entry = tkinter.Entry(self)
        self.del_button = tkinter.Button(self, text="DELETE", command=self.del_button)
        self.del_entry.pack()
        self.del_button.pack()

        l1 = Label(self, text = "First Name")
        self.firstname = tkinter.Entry(self)
        self.firstname.pack()
        l1.pack()

        l2 = Label(self, text = "Last Name")
        self.lastname = tkinter.Entry(self)
        self.lastname.pack() 
        l2.pack()

        l3 = Label(self, text = "Fill all fields for create and update")
        self.update_button = tkinter.Button(self, text="UPDATE", command=self.update_button)
        l3.pack()
        self.update_button.pack()

    def read_button(self):
        id = self.read_entry.get()
        #print(self.read_entry.get())
        applicant = applicantDAO.findById(id)
        l = Label(self, text = str(applicant))
        l.pack()
       

    def del_button(self):
        id = self.del_entry.get()
        applicantDAO.delete(id)
        l = Label(self, text = "Record Deleted")
        l.pack()

    def update_button(self):
        first_name = self.firstname.get()
        last_name = self.lastname.get()
        print(first_name)
        print(last_name)
    
         

class EditProgramScreen(tkinter.Tk):

    def __init__(self):
        # connect to database
        player_db = mysql.connect(
            host="35.245.211.180",
            user="root",
            password="EECE4520",
            database="player_db"
        )
        cursor = player_db.cursor()

        Tk.__init__(self)

        # Set the size of window
        self.geometry("650x650+100+100")
        self.title('Edit Programs Screen')
        s = ttk.Style()
        s.theme_use('classic')

class EditUniversityScreen(tkinter.Tk):

    def __init__(self):
        # connect to database
        player_db = mysql.connect(
            host="35.245.211.180",
            user="root",
            password="EECE4520",
            database="player_db"
        )
        cursor = player_db.cursor()

        Tk.__init__(self)

        # Set the size of window
        self.geometry("650x650+100+100")
        self.title('Edit Universities Screen')
        s = ttk.Style()
        s.theme_use('classic')

#window1 = EditScreen()
#window.mainloop()