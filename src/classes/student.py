import numpy as np;

class Student:
    name = "";
    enrollment = "";
    grade = [None] * 3;

    g1 = 0;
    g2 = 0;
    g3 = 0;

    def __init__(self, name, enrollment):
        self.name = name;
        self.enrollment = enrollment;
        self.g1 = np.random.randint(11);
        self.g2 = np.random.randint(11);
        self.g3 = np.random.randint(11);
        self.grade = self.g1, self.g2, self.g3;

    def storeGrade(self, g1, g2, g3):
        self.g1 = g1;
        self.g2 = g2;
        self.g3 = g3;
        self.grade = g1, g2, g3;

    def averageCalculate(self):
        return "The student {}'s average {:.2f}.".format(self.name, (self.g1 + self.g2 + self.g3)/3);

    def __str__(self):
        return "Student: {}\nEnrollment: {}\nGrade: {}".format(self.name, self.enrollment, self.grade);