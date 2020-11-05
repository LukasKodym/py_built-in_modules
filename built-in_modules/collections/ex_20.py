##

from collections import namedtuple

Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])

f = open('students.txt', 'r')

students = []
lines = [eval(line.strip()) for line in f.readlines()]
for line in lines:
    students.append(Student(**line))

f.close()

print(students)
