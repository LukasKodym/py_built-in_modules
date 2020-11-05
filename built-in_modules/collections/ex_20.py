##

from collections import namedtuple

Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])

f = open('students.txt', 'r')

students = []

for line in f:
    print(f.read(), end='')

#
# for line in f:
#     students.append(Student(**line))
#
f.close()

print(students)
