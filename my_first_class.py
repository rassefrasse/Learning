class Students:
    students = []

    def __init__(self, student_name, student_grade):
        self.student_name = student_name
        self.student_grade = student_grade #1-100

    def add_student(self, student):
        if len(self.students) < 2:
            self.students.append(student)

    def grade(self):
        return self.student_grade
        


z = Students("Rasmus", 95)

for student in Students.students:
    print("Name: ", student.student_name, "Grade: ", student.student_grade)
    