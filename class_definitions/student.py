class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):

        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

        if self.last_name != "Morishita":
            raise ValueError

        if self.first_name != "Elijah":
            raise ValueError

        if self.major != "Coding":
            raise ValueError

        if self.gpa != 3.5:
            raise ValueError


    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + "with gpa: " + str(self.gpa)
