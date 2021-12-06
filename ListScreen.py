# Import the required libraries
from tkinter import *
import tkinter
import tkinter.font
from tkinter import ttk
import mysql.connector as mysql
from DAO import applicantDAO, programDAO, universitiesDAO
from EditScreen import EditApplicantScreen, EditProgramScreen, EditUniversityScreen

class ListScreen(tkinter.Tk):

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
        self.title('List Screen')
        s = ttk.Style()
        s.theme_use('classic')

        # Add a Treeview widget for the chart
        applicantTree = ttk.Treeview(self, column=("c1", "c2", "c3", "c4", "c5","c6","c7","c8"),
                            show='headings', height=5)
        
        programTree = ttk.Treeview(self, column=("c1", "c2", "c3", "c4", "c5","c6"),
                            show='headings', height=5)
        
        universityTree = ttk.Treeview(self, column=("c1", "c2", "c3"),
                            show='headings', height=5)

        applicantTree.column("#1 ", anchor=CENTER)
        applicantTree.heading("# 1", text="Applicant Id")
        applicantTree.column("#2 ", anchor=CENTER)
        applicantTree.heading("# 2", text="First Name")
        applicantTree.column("# 3", anchor=CENTER)
        applicantTree.heading("# 3", text="Last Name")
        applicantTree.column("# 4", anchor=CENTER)
        applicantTree.heading("# 4", text="Username")
        applicantTree.column("# 5", anchor=CENTER)
        applicantTree.heading("# 5", text="Password")
        applicantTree.column("# 6", anchor=CENTER)
        applicantTree.heading("# 6", text="Email")
        applicantTree.column("# 7", anchor=CENTER)
        applicantTree.heading("# 7", text="Birthdate")
        applicantTree.column("# 8", anchor=CENTER)
        applicantTree.heading("# 8", text="GPA")

        programTree.column("#1 ", anchor=CENTER)
        programTree.heading("# 1", text="Program Id")
        programTree.column("#2 ", anchor=CENTER)
        programTree.heading("# 2", text="Program Name")
        programTree.column("# 3", anchor=CENTER)
        programTree.heading("# 3", text="National Ranking")
        programTree.column("# 4", anchor=CENTER)
        programTree.heading("# 4", text="Total Cost")
        programTree.column("# 5", anchor=CENTER)
        programTree.heading("# 5", text="University Name")
        programTree.column("# 6", anchor=CENTER)
        programTree.heading("# 6", text="Starting Semester")

        universityTree.column("#1 ", anchor=CENTER)
        universityTree.heading("# 1", text="University Name")
        universityTree.column("#2 ", anchor=CENTER)
        universityTree.heading("# 2", text="Location")
        universityTree.column("# 3", anchor=CENTER)
        universityTree.heading("# 3", text="Student Body Size")

        applicantsList = applicantDAO.findAll()
        for i in applicantsList:
            applicantTree.insert('', 'end', text="1", values=i)
        
        programsList = programDAO.findAll()
        for i in programsList:
            programTree.insert('', 'end', text="1", values=i)  

        universitiesList = universitiesDAO.findAll()
        for i in universitiesList:
            universityTree.insert('', 'end', text="1", values=i)    

        editbutton1 = Button(self, text="Edit Applicant Screen",
                             command=self.loadEditApplicantPage, bg='yellow', height=4, width=15, wraplength=80)
        editbutton1.place(x=100, y=400)  
        editbutton2 = Button(self, text="Edit Program Screen",
                             command=self.loadEditProgramPage, bg='yellow', height=4, width=15, wraplength = 80)
        editbutton2.place(x=250, y=400)  
        editbutton2 = Button(self, text="Edit University Screen",
                             command=self.loadEditUniversityPage, bg='yellow', height=4, width=15, wraplength = 80)
        editbutton2.place(x=400, y=400)


        applicantTree.pack()
        programTree.pack()
        universityTree.pack()

    def loadEditApplicantPage(self):
        window = EditApplicantScreen()
        window.mainloop()

    def loadEditProgramPage(self):
        window = EditProgramScreen()
        window.mainloop()
    
    def loadEditUniversityPage(self):
        window = EditUniversityScreen()
        window.mainloop()

window = ListScreen()
window.mainloop()
