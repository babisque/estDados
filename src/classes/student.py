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

    def storeGrade(self, n1, n2, n3):
        self.g1 = n1;
        self.g2 = n2;
        self.g3 = n3;
        self.grade = self.g1, self.g2, self.g3;

    def averageCalculate(self):
        return "A média do {} é {:.2f}.".format(self.name, (self.g1 + self.g2 + self.g3)/3);

    def __str__(self):
        return "Estudante: {}\nMatrícula: {}\nNotas: {}".format(self.name, self.enrollment, self.grade);