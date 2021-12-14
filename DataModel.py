
class Applicant:
    def __init__(self, first_name, last_name, username, password, email, date_of_birth, gpa):
       # self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.date_of_birth = date_of_birth
        self.gpa = gpa

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, x):
        self.first_name = x

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, x):
        self.last_name = x

    def get_username(self):
        return self.username

    def set_username(self, x):
        self.username = x
    
    def get_password(self):
        return self.password

    def set_password(self, x):
        self.password = x

    def get_email(self):
        return self.email

    def set_email(self, x):
        self.email = x

    def getDOB(self):
        return self.date_of_birth

    def setDOB(self, x):
        self.date_of_birth = x

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, x):
        self.gpa = x

    def get_application_list(self):
        return self.application_list

    def set_application_list(self, x):
        self.application_list = x

class Program:
    def __init__(self, program_name, national_ranking, total_cost, university_name, starting_sem):
        self.program_name = program_name
        self.national_ranking = national_ranking
        self.total_cost = total_cost
        self.university_name = university_name
        self.starting_sem = starting_sem

    def get_program_name(self):
        return self.program_name

    def set_program_name(self, x):
        self.program_name = x

    def get_national_ranking(self):
        return self.national_ranking

    def set_national_ranking(self, x):
        self.national_ranking = x

    def get_cost(self):
        return self.total_cost

    def set_cost(self, x):
        self.total_cost = x

    def get_university_name(self):
        return self.university_name

    def set_university_name(self, x):
        self.university_name = x

    def get_starting_sem(self):
        return self.starting_sem

    def set_starting_sem(self, x):
        self.starting_sem = x

class University:
    def __init__(self, name, location, student_body_size):
        self.name = name
        self.location = location
        self.student_body_size = student_body_size

    def get_university_name(self):
        return self.name

    def set_university_name(self, x):
        self.university_name = x

    def get_location(self):
        return self.location

    def set_location(self, x):
        self.location = x
    
    def get_size(self):
        return self.student_body_size

    def set_size(self, x):
        self.student_body_size = x


    

    