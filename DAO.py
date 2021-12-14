import mysql.connector as mysql
from DataModel import Applicant
from DataModel import Program
from DataModel import University

# connect to database
universities_db = mysql.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd",
    database="final_project")

class applicantDAO:
    def findAll():
        applicantList = []
        mycursor = universities_db.cursor()
        mycursor.execute("SELECT * FROM applicants")
        myresult = mycursor.fetchall()
        for x in myresult:
            applicantList.append(x)
        return applicantList
    
    def findById(id):
        mycursor = universities_db.cursor()
        mycursor.execute("SELECT * FROM final_project.applicants WHERE id=%(id)s", {'id': id})
        myresult = mycursor.fetchall()
        for x in myresult:
            return x

    def getIDList():
        idList = []
        mycursor = universities_db.cursor()
        mycursor.execute("SELECT id FROM final_project.applicants")
        myresult = mycursor.fetchall()
        for x in myresult:
            idList.append(x[0])
        return idList

    def create(Applicant):
        first_name = Applicant.get_first_name()
        last_name = Applicant.get_last_name()
        username = Applicant.get_username()
        password = Applicant.get_password()
        email = Applicant.get_email()
        DOB = Applicant.getDOB()
        gpa = Applicant.get_gpa()
        mycursor = universities_db.cursor()
        insert_stmt = ("INSERT INTO final_project.applicants(first_name,last_name,username,password,email,birthdate,gpa) "
                        "VALUES(%s, %s, %s, %s, %s, %s, %s)")
        data = (first_name,last_name,username,password,email,DOB,gpa)
        mycursor.execute(insert_stmt,data)
        universities_db.commit()

    def update(id, Applicant):
        first_name = Applicant.get_first_name()
        last_name = Applicant.get_last_name()
        username = Applicant.get_username()
        password = Applicant.get_password()
        email = Applicant.get_email()
        DOB = Applicant.getDOB()
        gpa = Applicant.get_gpa()
        mycursor = universities_db.cursor()
        update_query = """UPDATE final_project.applicants SET first_name="%s",last_name="%s",username="%s",password="%s",email="%s",birthdate="%s",gpa="%s"
                        WHERE id = "%s";""" % (first_name,last_name,username,password,email,DOB,gpa,id)
        mycursor.execute(update_query)
        universities_db.commit()
        
    def delete(id):
        mycursor = universities_db.cursor()
        mycursor.execute("DELETE FROM final_project.applicants WHERE id=%(id)s", {'id': id})
        universities_db.commit()

class programDAO:
    def findAll():
        programList = []
        mycursor = universities_db.cursor()
        mycursor.execute("SELECT * FROM final_project.programs")
        myresult = mycursor.fetchall()
        for x in myresult:
            programList.append(x)
        return programList
    
    def findById(id):
        mycursor = universities_db.cursor()
        mycursor.execute("SELECT * FROM final_project.programs WHERE id_program=%(id)s", {'id': id})
        myresult = mycursor.fetchall()
        for x in myresult:
            return x

    def getIDList():
        idList = []
        mycursor = universities_db.cursor()
        mycursor.execute("SELECT id_program FROM final_project.programs")
        myresult = mycursor.fetchall()
        for x in myresult:
            idList.append(x[0])
        return idList

    def create(Program):
        program_name = Program.get_program_name()
        national_ranking = Program.get_national_ranking()
        total_cost = Program.get_cost()
        university_name = Program.get_university_name()
        starting_sem = Program.get_starting_sem()
        mycursor = universities_db.cursor()
        insert_stmt = ("INSERT INTO final_project.programs(program_name,national_ranking,total_cost,university_name,starting_semester)"
                        "VALUES(%s, %s, %s, %s, %s)")
        data = (program_name,national_ranking,total_cost,university_name,starting_sem)
        mycursor.execute(insert_stmt,data)
        universities_db.commit()

    def update(id, Program):
        program_name = Program.get_program_name()
        national_ranking = Program.get_national_ranking()
        total_cost = Program.get_cost()
        university_name = Program.get_university_name()
        starting_sem = Program.get_starting_sem()
        mycursor = universities_db.cursor()
        update_query = """UPDATE final_project.programs SET program_name="%s",national_ranking="%s",total_cost="%s",university_name="%s",starting_semester="%s"
                        WHERE id_program = "%s";""" % (program_name,national_ranking,total_cost,university_name,starting_sem,id)
        mycursor.execute(update_query)
        universities_db.commit()
        
    def delete(id):
        mycursor = universities_db.cursor()
        mycursor.execute("DELETE FROM final_project.programs WHERE id_program=%(id)s", {'id': id})
        universities_db.commit()

class universitiesDAO:
    def findAll():
        universityList = []
        mycursor = universities_db.cursor()
        mycursor.execute("SELECT * FROM final_project.universities")
        myresult = mycursor.fetchall()
        for x in myresult:
            universityList.append(x)
        return universityList
    
    def findById(id):
        mycursor = universities_db.cursor()
        mycursor.execute("SELECT * FROM final_project.universities WHERE university_name=%(id)s", {'id': id})
        myresult = mycursor.fetchall()
        for x in myresult:
            return x

    def getIDList():
        idList = []
        mycursor = universities_db.cursor()
        mycursor.execute("SELECT university_name FROM final_project.universities")
        myresult = mycursor.fetchall()
        for x in myresult:
            idList.append(x[0])
        return idList
        
    def create(University):
        university_name = University.get_university_name()
        location = University.get_location()
        student_body_size = University.get_size()
        mycursor = universities_db.cursor()
        insert_stmt = ("INSERT INTO final_project.universities(university_name,location,studentbody_size)"
                        "VALUES(%s, %s, %s)")
        data = (university_name,location,student_body_size)
        mycursor.execute(insert_stmt,data)
        universities_db.commit()

    def update(id, University):
        location = University.get_location()
        student_body_size = University.get_size()
        mycursor = universities_db.cursor()
        update_query = """UPDATE final_project.universities SET location="%s",studentbody_size="%s"
                        WHERE university_name = "%s";""" % (location,student_body_size, id)
        mycursor.execute(update_query)
        universities_db.commit()
        
    def delete(id):
        mycursor = universities_db.cursor()
        mycursor.execute("DELETE FROM final_project.universities WHERE university_name=%(id)s", {'id': id})
        universities_db.commit()




