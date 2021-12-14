# Import the required libraries
from tkinter import *
import tkinter
import tkinter.font
from tkinter import ttk
import mysql.connector as mysql
from DAO import applicantDAO, programDAO, universitiesDAO
from DataModel import Applicant, Program, University

class EditApplicantScreen(tkinter.Tk):

    def __init__(self,  fill_values = ['']*7):
        # connect to database
        player_db = mysql.connect(
            host="localhost",
            user="root",
            password="P@ssw0rd",
            database="final_project",
        )
        cursor = player_db.cursor()

        Tk.__init__(self)

        # Set the size of window
        self.geometry("650x650+100+100")
        self.title('Edit Applicants Screen')
        s = ttk.Style()
        s.theme_use('classic')

        id_list = str(applicantDAO.getIDList())
        l1 = Label(self, text = "Choose from following ID's:" + id_list)
        l1.pack()


        self.read_entry = tkinter.Entry(self)
        self.read_button = tkinter.Button(self, text="READ", command=self.read_button)
        self.read_entry.pack()
        self.read_button.pack()

        self.del_entry = tkinter.Entry(self)
        self.del_button = tkinter.Button(self, text="DELETE", command=self.del_button)
        self.del_entry.pack()
        self.del_button.pack()

        l1 = Label(self, text = "id")
        self.id = tkinter.Entry(self)
        self.id.insert(0, str(fill_values[0]))
        self.id.pack()
        l1.pack()

        l2 = Label(self, text = "First Name")
        self.firstname = tkinter.Entry(self)
        self.firstname.insert(0, str(fill_values[1]))
        self.firstname.pack()
        l2.pack()

        l3 = Label(self, text = "Last Name")
        self.lastname = tkinter.Entry(self)
        self.lastname.insert(0, str(fill_values[2]))
        self.lastname.pack() 
        l3.pack()

        l4 = Label(self, text = "username")
        self.username = tkinter.Entry(self)
        self.username.insert(0, str(fill_values[3]))
        self.username.pack() 
        l4.pack()

        l5 = Label(self, text = "password")
        self.password = tkinter.Entry(self)
        self.password.insert(0, str(fill_values[4]))
        self.password.pack() 
        l5.pack()

        l6 = Label(self, text = "email")
        self.email = tkinter.Entry(self)
        self.email.insert(0, str(fill_values[5]))
        self.email.pack() 
        l6.pack()

        l7 = Label(self, text = "date_of_birth")
        self.date_of_birth = tkinter.Entry(self)
        self.date_of_birth.insert(0, str(fill_values[6]))
        self.date_of_birth.pack() 
        l7.pack()

        l8 = Label(self, text = "gpa")
        self.gpa = tkinter.Entry(self)
        self.gpa.insert(0, str(fill_values[7]))
        self.gpa.pack() 
        l8.pack()

        l9 = Label(self, text = "Fill all fields for update (ID must match)")
        self.update_button = tkinter.Button(self, text="UPDATE", command=self.update_button)
        l9.pack()
        self.update_button.pack()

        l10 = Label(self, text = "Leave ID field blank for create")
        self.create_button = tkinter.Button(self, text="CREATE", command=self.create_button)
        l10.pack()
        self.create_button.pack()


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
        id = self.id.get()
        first_name = self.firstname.get()
        last_name = self.lastname.get()
        username = self.username.get()
        password = self.password.get()
        email = self.email.get()
        date_of_birth = self.date_of_birth.get()
        gpa = self.gpa.get()
        #code to update applicant
        #applicantDAO1 = applicantDAO()
        newInfo = Applicant(first_name, last_name, username, password, email, date_of_birth, gpa)
        applicantDAO.update(id, newInfo)
        l = Label(self, text = "Record Updated")
        l.pack()

    def create_button(self):
        first_name = self.firstname.get()
        last_name = self.lastname.get()
        username = self.username.get()
        password = self.password.get()
        email = self.email.get()
        date_of_birth = self.date_of_birth.get()
        gpa = self.gpa.get()
        #code to add applicant
        my_applicant = Applicant(first_name, last_name, username, password, email, date_of_birth, gpa)
        applicantDAO.create(my_applicant)
        l = Label(self, text = "Record Created")
        l.pack()
    
         

class EditProgramScreen(tkinter.Tk):

    def __init__(self, fill_values = ['']*7):
        # connect to database
        player_db = mysql.connect(
            host="localhost",
            user="root",
            password="P@ssw0rd",
            database="final_project",
        )
        cursor = player_db.cursor()

        Tk.__init__(self)

        # Set the size of window
        self.geometry("650x650+100+100")
        self.title('Edit Programs Screen')
        s = ttk.Style()
        s.theme_use('classic')

        id_list = str(programDAO.getIDList())
        l1 = Label(self, text = "Choose from following ID's:" + id_list)
        l1.pack()

        self.read_entry = tkinter.Entry(self)
        self.read_button = tkinter.Button(self, text="READ", command=self.read_button)
        self.read_entry.pack()
        self.read_button.pack()

        self.del_entry = tkinter.Entry(self)
        self.del_button = tkinter.Button(self, text="DELETE", command=self.del_button)
        self.del_entry.pack()
        self.del_button.pack()

        l1 = Label(self, text = "id")
        self.id = tkinter.Entry(self)
        self.id.insert(0, str(fill_values[0]))
        self.id.pack()
        l1.pack()

        l2 = Label(self, text = "program name")
        self.program_name = tkinter.Entry(self)
        self.program_name.insert(0, str(fill_values[2]))
        self.program_name.pack()
        l2.pack()

        l3 = Label(self, text = "national_ranking")
        self.national_ranking = tkinter.Entry(self)
        self.national_ranking.insert(0, str(fill_values[3]))
        self.national_ranking.pack() 
        l3.pack()

        l4 = Label(self, text = "total cost")
        self.total_cost = tkinter.Entry(self)
        self.total_cost.insert(0, str(fill_values[4]))
        self.total_cost.pack() 
        l4.pack()

        l5 = Label(self, text = "university_name")
        self.university_name = tkinter.Entry(self)
        self.university_name.insert(0, str(fill_values[5]))
        self.university_name.pack() 
        l5.pack()

        l6 = Label(self, text = "starting_sem")
        self.starting_sem = tkinter.Entry(self)
        self.starting_sem.insert(0, str(fill_values[6]))
        self.starting_sem.pack() 
        l6.pack()

        l9 = Label(self, text = "Fill all fields for update (ID must match)")
        self.update_button = tkinter.Button(self, text="UPDATE", command=self.update_button)
        l9.pack()
        self.update_button.pack()

        l10 = Label(self, text = "Leave ID field blank for create")
        self.create_button = tkinter.Button(self, text="CREATE", command=self.create_button)
        l10.pack()
        self.create_button.pack()


    def read_button(self):
        id = self.read_entry.get()
        #print(self.read_entry.get())
        program = programDAO.findById(id)
        l = Label(self, text = str(program))
        l.pack()
       

    def del_button(self):
        id = self.del_entry.get()
        programDAO.delete(id)
        l = Label(self, text = "Record Deleted")
        l.pack()

    def update_button(self):
        id = self.id.get()
        program_name = self.program_name.get()
        national_ranking = self.national_ranking.get()
        total_cost = self.total_cost.get()
        university_name = self.university_name.get()
        starting_sem = self.starting_sem.get()
        #code to update program
        newInfo = Program(program_name, national_ranking, total_cost, university_name, starting_sem)
        programDAO.update(id, newInfo)
        l = Label(self, text = "Record Updated")
        l.pack()


    def create_button(self):
        program_name = self.program_name.get()
        national_ranking = self.national_ranking.get()
        total_cost = self.total_cost.get()
        university_name = self.university_name.get()
        starting_sem = self.starting_sem.get()
        #code to add program
        program = Program(program_name, national_ranking, total_cost, university_name, starting_sem)
        programDAO.create(program)
        l = Label(self, text = "Record Created")
        l.pack()

class EditUniversityScreen(tkinter.Tk):

    def __init__(self, fill_values = ['']*4):
        # connect to database
        player_db = mysql.connect(
            host="localhost",
            user="root",
            password="P@ssw0rd",
            database="final_project",
        )
        cursor = player_db.cursor()

        Tk.__init__(self)

        # Set the size of window
        self.geometry("650x650+100+100")
        self.title('Edit Universities Screen')
        s = ttk.Style()
        s.theme_use('classic')

        l = Label(self, text = "ID is university name")
        l.pack()

        id_list = str(universitiesDAO.getIDList())
        l1 = Label(self, text = "Choose from following ID's:" + id_list)
        l1.pack()

        self.read_entry = tkinter.Entry(self)
        self.read_button = tkinter.Button(self, text="READ", command=self.read_button)
        self.read_entry.pack()
        self.read_button.pack()

        self.del_entry = tkinter.Entry(self)
        self.del_button = tkinter.Button(self, text="DELETE", command=self.del_button)
        self.del_entry.pack()
        self.del_button.pack()

        l1 = Label(self, text = "name")
        self.name = tkinter.Entry(self)
        self.name.insert(0, str(fill_values[0]))
        self.name.pack()
        l1.pack()

        l3 = Label(self, text = "location")
        self.location = tkinter.Entry(self)
        self.location.insert(0, str(fill_values[1]))
        self.location.pack() 
        l3.pack()

        l4 = Label(self, text = "student_body_size")
        self.student_body_size = tkinter.Entry(self)
        self.student_body_size.insert(0, str(fill_values[2]))
        self.student_body_size.pack() 
        l4.pack()

        l5 = Label(self, text = "Fill all fields for update (ID must match)")
        self.update_button = tkinter.Button(self, text="UPDATE", command=self.update_button)
        l5.pack()
        self.update_button.pack()

        l6 = Label(self, text = "Do not leave ID field blank for create")
        self.create_button = tkinter.Button(self, text="CREATE", command=self.create_button)
        l6.pack()
        self.create_button.pack()

        self.search_programs_button = tkinter.Button(self, text="find university programs", command=self.search_programs_button)
        self.search_programs_button.pack()

    def read_button(self):
        name = self.read_entry.get()
        #print(self.read_entry.get())
        program = universitiesDAO.findById(name)
        l = Label(self, text = str(program))
        l.pack()
       

    def del_button(self):
        name = self.del_entry.get()
        universitiesDAO.delete(name)
        l = Label(self, text = "Record Deleted")
        l.pack()

    def update_button(self):
        name = self.name.get()
        location = self.location.get()
        student_body_size = self.student_body_size.get()
        newInfo = University(name, location, student_body_size)
        universitiesDAO.update(name, newInfo)
        l = Label(self, text = "Record Updated")
        l.pack()

    def search_programs_button(self):
        university = self.name.get()
        allPrograms = programDAO.findAll()
        filtered_universities = [i for i in allPrograms if i[4]==university]
        #create treeview below
        self.universityTree = ttk.Treeview(self, column=("c1", "c2", "c3"),
                    show='headings', height=5) 

        self.universityTree.column("#1 ", anchor=CENTER)
        self.universityTree.heading("# 1", text="University Name")
        self.universityTree.column("#2 ", anchor=CENTER)
        self.universityTree.heading("# 2", text="Location")
        self.universityTree.column("# 3", anchor=CENTER)
        self.universityTree.heading("# 3", text="Student Body Size") 

        for i in filtered_universities:
            self.universityTree.insert('', 'end', text="1", values=i)  
        self.universityTree.pack()

        self.universityTree.bind("<Double-1>", self.OnDoubleClickUniversity)

    def OnDoubleClickUniversity(self, event):
        item = self.universityTree.selection()
        contents = self.universityTree.item(item)
        values = contents.get('values')
        EditUniversityScreen(values)
        

    def create_button(self):
        name = self.name.get()
        location = self.location.get()
        student_body_size = self.student_body_size.get()
        uni = University(name, location, student_body_size)
        universitiesDAO.create(uni)
        l = Label(self, text = "Record Created")
        l.pack()

#window1 = EditScreen()
#window.mainloop()