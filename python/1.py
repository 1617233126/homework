class student:
    '����ѧ���Ļ���'
    stu_count = 0




    def __init__(self,name,stu_number,stu_class,gender):
        self.name = name
        self.stu_number =  stu_number
        self.stu_class = stu_class
        self.gender = gender
        student.stu_count += 1

    def displaycount(self):
        print"Total student %d" %student.stu_count
    def displayStu(self):
        print"Name : ",self.name, ", stu_number: ",self.stu_number,"stu_class:"
