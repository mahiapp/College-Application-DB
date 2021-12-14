# Import the required libraries
from tkinter import *
import tkinter
import tkinter.font
from tkinter import ttk
import mysql.connector
from DAO import applicantDAO, programDAO, universitiesDAO
from EditScreen import EditApplicantScreen, EditProgramScreen, EditUniversityScreen

class ListScreen(tkinter.Tk):

    def __init__(self):
        # connect to database
        player_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="P@ssw0rd",
        database="final_project",
        )
        cursor = player_db.cursor()

        Tk.__init__(self)

        # Set the size of window
        self.geometry("650x650+100+100")
        self.title('List Screen')
        s = ttk.Style()
        s.theme_use('classic')

        # Add a Treeview widget for the chart
        self.applicantTree = ttk.Treeview(self, column=("c1", "c2", "c3", "c4", "c5","c6","c7","c8"),
                            show='headings', height=5)
        
        self.programTree = ttk.Treeview(self, column=("c1", "c2", "c3", "c4", "c5","c6"),
                            show='headings', height=5)
        
        self.universityTree = ttk.Treeview(self, column=("c1", "c2", "c3"),
                            show='headings', height=5)     
                     

        self.applicantTree.column("#1 ", anchor=CENTER)
        self.applicantTree.heading("# 1", text="Applicant Id")
        self.applicantTree.column("#2 ", anchor=CENTER)
        self.applicantTree.heading("# 2", text="First Name")
        self.applicantTree.column("# 3", anchor=CENTER)
        self.applicantTree.heading("# 3", text="Last Name")
        self.applicantTree.column("# 4", anchor=CENTER)
        self.applicantTree.heading("# 4", text="Username")
        self.applicantTree.column("# 5", anchor=CENTER)
        self.applicantTree.heading("# 5", text="Password")
        self.applicantTree.column("# 6", anchor=CENTER)
        self.applicantTree.heading("# 6", text="Email")
        self.applicantTree.column("# 7", anchor=CENTER)
        self.applicantTree.heading("# 7", text="Birthdate")
        self.applicantTree.column("# 8", anchor=CENTER)
        self.applicantTree.heading("# 8", text="GPA")

        self.programTree.column("#1 ", anchor=CENTER)
        self.programTree.heading("# 1", text="Program Id")
        self.programTree.column("#2 ", anchor=CENTER)
        self.programTree.heading("# 2", text="Program Name")
        self.programTree.column("# 3", anchor=CENTER)
        self.programTree.heading("# 3", text="National Ranking")
        self.programTree.column("# 4", anchor=CENTER)
        self.programTree.heading("# 4", text="Total Cost")
        self.programTree.column("# 5", anchor=CENTER)
        self.programTree.heading("# 5", text="University Name")
        self.programTree.column("# 6", anchor=CENTER)
        self.programTree.heading("# 6", text="Starting Semester")

        self.universityTree.column("#1 ", anchor=CENTER)
        self.universityTree.heading("# 1", text="University Name")
        self.universityTree.column("#2 ", anchor=CENTER)
        self.universityTree.heading("# 2", text="Location")
        self.universityTree.column("# 3", anchor=CENTER)
        self.universityTree.heading("# 3", text="Student Body Size")

        applicantsList = applicantDAO.findAll()
        for i in applicantsList:
            self.applicantTree.insert('', 'end', text="1", values=i)
        
        programsList = programDAO.findAll()
        for i in programsList:
            self.programTree.insert('', 'end', text="1", values=i)  

        universitiesList = universitiesDAO.findAll()
        for i in universitiesList:
            self.universityTree.insert('', 'end', text="1", values=i)    

        editbutton1 = Button(self, text="Edit Applicant Screen",
                             command=self.loadEditApplicantPage, bg='yellow', height=4, width=15, wraplength=80)
        editbutton1.place(x=100, y=400)  
        editbutton2 = Button(self, text="Edit Program Screen",
                             command=self.loadEditProgramPage, bg='yellow', height=4, width=15, wraplength = 80)
        editbutton2.place(x=250, y=400)  
        editbutton2 = Button(self, text="Edit University Screen",
                             command=self.loadEditUniversityPage, bg='yellow', height=4, width=15, wraplength = 80)
        editbutton2.place(x=400, y=400)


        self.applicantTree.pack()
        self.programTree.pack()
        self.universityTree.pack()

        self.applicantTree.bind("<Double-1>", self.OnDoubleClickApplicant)
        self.programTree.bind("<Double-1>", self.OnDoubleClickProgram)
        self.universityTree.bind("<Double-1>", self.OnDoubleClickUniversity)

    def loadEditApplicantPage(self):

        window = EditApplicantScreen()
        window.mainloop()

    def loadEditProgramPage(self):
        window = EditProgramScreen()
        window.mainloop()
    
    def loadEditUniversityPage(self):
        window = EditUniversityScreen()
        window.mainloop()

    def OnDoubleClickApplicant(self, event):
        item = self.applicantTree.selection()
        contents = self.applicantTree.item(item)
        values = contents.get('values')
        EditApplicantScreen(values)

    def OnDoubleClickUniversity(self, event):
        item = self.universityTree.selection()
        contents = self.universityTree.item(item)
        values = contents.get('values')
        EditUniversityScreen(values)

    def OnDoubleClickProgram(self, event):
        item = self.programTree.selection()
        contents = self.programTree.item(item)
        values = contents.get('values')
        EditProgramScreen(values)

window = ListScreen()
window.mainloop()
