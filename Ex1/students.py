
class student:

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def reportGPA(self):
        return(f'{self.name} has a GPA of {self.gpa}')
