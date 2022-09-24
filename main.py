import numpy as np;
from src.classes.student import Student;
from src.classes.circularQueue import CircularQueue;

queue = CircularQueue();
students = [];

students.append(Student("Lucas", "20220920ES"));
students.append(Student("Kawan", "20220940ES"));
students.append(Student("Rodrigo", "20220930ES"));
students.append(Student("Caio", "20220220ES"));
students.append(Student("Rafael", "20223120ES"));
students.append(Student("David", "20223134ES"));
students.append(Student("Samuel", "19020920ES"));
students.append(Student("Tiago", "14535920ES"));
students.append(Student("José", "4246720ES"));
students.append(Student("Antonio", "8197429ES"));
students.append(Student("Carlos", "8932745ES"));
students.append(Student("Michael", "2167463ES"));
students.append(Student("João", "2164738ES"));

for student in students:
    n1 = np.random.randint(11);
    n2 = np.random.randint(11);
    n3 = np.random.randint(11);
    student.storeGrade(n1, n2, n3);

i = 0;
print("Alunos matriculados:\n");
while i < 10:
    queue.enqueue(students[i].name);
    print("{}\n".format(students[i]));
    i += 1;

print("Adicionando {} na fila.".format(students[10].name));
queue.enqueue(students[10].name);

k = 0;
while k < 3:
    queue.dequeue();
    k += 1;

j = 10;
print("\n\n");
while j < 13:
    print("Adicionando {} na fila.".format(students[j].name));
    queue.enqueue(students[j].name);
    print("\n");
    j += 1;