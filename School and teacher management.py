class School:
    dataBase = {}
    def __init__(self, name, level, code) -> None:
        self.name = name;self.level = level;self.code = code
        pass
    @classmethod
    def registration(cls,self) -> bool:
        information = []
        information.append(self.name)
        information.append(self.level)
        cls.dataBase[self.code]=information
        return True
    @classmethod
    def login(cls, self) -> bool:
        if(cls.dataBase.__contains__(self.code)):
            return True
        else:
            return False
        pass
    def createTecahersDatabase(self) -> bool:
        self.teachers = {}#will store basic info
        self.fees = {}
        self.principal = "None till Now"
        self.duties = {}
        return True
    def teachersLog(self, other)-> bool:
        if(self.teachers.keys().__contains__(other.name)):
            return True
        else:
            self.teachers[other.name] = other.info
            return False
        pass
    def isHigherSecondary(self) -> bool:
        if self.level == "higher Secondary": return True
        else: return False
        pass
    def subjectOffered(self,obj) -> None:
        self.subjects = []
        self.subjects = obj
        pass
    pass

class Teacher:
    def __init__(self, name, qualif, subjects) -> None:
        self.name = name
        self.qualif = qualif
        self.subjects = subjects
        pass
    @classmethod
    def makeDataBase(cls, self) ->bool:
        self.info = []
        self.info.append(self.qualif)
        self.info.append(self.subjects)
        return True
    pass

if __name__=='__main__':
    school1 = School(input("Name:\t"), input("Education Level:\t"),input("School Code:\t"))
    school1.createTecahersDatabase()
    print("Command list:\n0 = terminate\n1 = Enrollment\n2 = login"
          "\n3 = Enroll Subjects"
          "\n4 = enroll as teacher")
    command = int(input("Enter Command:\t"))
    while(command!=0):
        if(command==1):
            if (School.registration(school1)):
                print("Enrollment successsful")
                command = int(input("Enter Command:\t"))
                pass
            pass
        elif(command==2):
            if School.login(school1):
                print("Successfully Logged in")
                pass
            else: 
                print("Login Failure. Enroll First")
                pass
            command = int(input("Enter Command:\t"))
            pass
        elif(command == 3):
            limit = int(input("Enter the Number of the books:\t"))
            subjects = []
            for i in range(limit):
                subjects.append(input("Enter subject name:\t"))
                pass
            school1.subjectOffered(subjects)
            print("All data are successfully stored")
            command = int(input("Enter Command: "))
            pass
        elif(command == 4):
            name = input("Name:\t")
            qualification = input("Qualification:\t")
            teachingSubjects = []
            print("Enter 3 subjects That you can teach:")
            for i in range(3):
                teachingSubjects.append(input("Enter subject:\t"))
                pass
            teacher = Teacher(name,qualification,teachingSubjects)
            Teacher.makeDataBase(teacher)
            if(school1.teachersLog(teacher)):
                print("You are Successfully logged in as a teacher")
                pass
            else:
                print("You are now a teacher of our Institution")
                pass
            command = int(input("Enter Commnad: "))
        else:
            print("Wrong Command")
            command = int(input("Enter Command: "))
            pass
        pass
    print("Programme Terminated")
    pass