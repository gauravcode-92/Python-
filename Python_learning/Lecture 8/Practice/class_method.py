class Student:
    def __init__(self,name,subject1,subject2,subject3):
        self.name=name
        self.subject1=subject1
        self.subject2=subject2
        self.subject3=subject3

    def avg(self):
        Total=self.subject1+self.subject2+self.subject3
        average=Total/3
        print("The average of",self.name ,"is:",average)

s1=Student("deep",38,90,68)
s1.avg()

