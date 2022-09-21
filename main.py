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


print("\nThe students avarage is:\n");
for student in students:
    print(student.averageCalculate());
    queue.enqueue(student.name);

print("The queue is: {}".format(queue.data));
print("Enrolled students: {}".format(queue.__len__()));