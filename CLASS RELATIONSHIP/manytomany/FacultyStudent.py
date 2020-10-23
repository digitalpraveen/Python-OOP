class FacultyStudent:
    def __init__(self,faculty,student):
        self.faculty=faculty
        self.student=student

    def __str__(self):

        return str(self.faculty)+str(self.student)