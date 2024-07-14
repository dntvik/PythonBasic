class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}, Record Book: {self.record_book}'


class GroupIsFull(Exception):
    def __init__(self, message="Group is full."):
        self.message = message
        super().__init__(self.message)


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupIsFull()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 22, 'John', 'Doe', 'AN143')
st4 = Student('Female', 23, 'Jane', 'Doe', 'AN144')
st5 = Student('Male', 21, 'Mike', 'Smith', 'AN146')
st6 = Student('Female', 24, 'Anna', 'Brown', 'AN147')
st7 = Student('Male', 26, 'Chris', 'Johnson', 'AN148')
st8 = Student('Female', 22, 'Emma', 'Wilson', 'AN149')
st9 = Student('Male', 27, 'James', 'Williams', 'AN150')
st10 = Student('Female', 25, 'Olivia', 'Jones', 'AN151')
st11 = Student('Male', 28, 'Liam', 'Garcia', 'AN152')

gr = Group('PD1')
students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]

for st in students:
    try:
        gr.add_student(st)
    except GroupIsFull as err:
        print(err)
print(gr)
