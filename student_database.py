class StudentDatabase:
    student_list=[]
    def add_student(self,x):
        self.student_list.append(x)

    


class Student:

    def __init__(self,student_id,name,department):
        self._student_id=student_id
        self._name=name
        self._department=department
        self._is_enrolled=False


    def enroll_student(self):
        if self._is_enrolled==False:
            self._is_enrolled=True


    def drop_student(self):
        if self._is_enrolled==True:
            self._is_enrolled=False
    
    def view_student_info(self):
        print(f" Id:{self._student_id} , Name:{self._name} , Department: {self._department} , Enrolled:{self._is_enrolled}")

    @property
    def st_id(self):
        return self._student_id
    @property
    def is_enrl(self):
        return self._is_enrolled
   
    
  


st1=Student("S101","Rakib","cse")
st2=Student("S102","Sakib","eee")
st3=Student("S103","Akib","pharmacy")

sd = StudentDatabase()

sd.add_student(st1)
sd.add_student(st2)
sd.add_student(st3)







bl=True
lt=[]
for q in sd.student_list:
    lt.append(q.st_id)

while bl:
    print("----------Student Management Menu----------")
    print("1.View all students")
    print("2.Enroll Student")
    print("3.Drop Student")
    print("4.Exit")
    x = int(input("Enter your choice(1-4):"))


    if x==1:
         for x in sd.student_list:
              x.view_student_info()


  


    elif x==2:
        y=(input("Enter student id to enroll:"))

        if y in lt:
         for a in sd.student_list:
            if a.st_id==y:
                if a.is_enrl==False:
                    a.enroll_student()
                    print(f"Student {y} has been enrolled")
                else:
                    print("Student is already enrolled")

        else:
            print("Invalid student id")

    elif x==3:
         p=(input("Enter student id to drop:"))
         if p in lt:
              for a in sd.student_list:
                    if a.st_id==p:
                        if a.is_enrl==True:
                          a.drop_student()
                          print(f"Student {y} has been dropped")
                        else:
                            print("Student is not enrolled can't be dropped")
         else:
             print("Invalid student id")

    elif x==4:
        bl=False
        
   