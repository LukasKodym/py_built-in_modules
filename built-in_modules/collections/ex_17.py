##

from collections import namedtuple

Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])

st1 = Student('Mike', 21, 'physics')
st2 = Student('Kate', 20, 'mathematics')
st3 = Student('Bob', 21, 'information technology')

students = [st1, st2, st3]

for student in students:
    print(f'{student.name:5}: {student.age}: {student.specialization}')
