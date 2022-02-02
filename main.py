class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _mean(self):
        add = 0
        index = 0
        for val in self.grades.values():
            add += sum(val)
            index += len(val)
        result = add / index
        return result

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {self._mean()} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
        else:
            return self._mean() < other._mean()

    def rate_lectors(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] = [grade]
            else:
                lector.grades[course] = [grade]
        else:
            print('Ошибка добавления оценки!')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _mean(self):
        add = 0
        index = 0
        for val in self.grades.values():
            add += sum(val)
            index += len(val)
        result = add / index
        return result

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._mean()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lector')
        else:
            return self._mean() < other._mean()


class Reviewer(Mentor):

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


lector_one = Lecturer("Ivan", "Potapov")
lector_two = Lecturer("Gennadiy", "Pavlov")
student_one = Student("Pavel", "Ivanov", "man")
student_two = Student("Sidor", "Sidorikov", "man")
reviewer_one = Reviewer('Petr', 'Sidorov')
reviewer_two = Reviewer("Simon", "Born")
reviewer_one.courses_attached += ['Python']
reviewer_two.courses_attached += ['Python']
lector_one.courses_attached += ['Python']
lector_two.courses_attached += ['Python']
student_one.courses_in_progress += ['Python']
student_two.courses_in_progress += ['Python']
reviewer_one.rate_hw(student_one, 'Python', 10)
reviewer_one.rate_hw(student_two, 'Python', 8)
student_one.rate_lectors(lector_one, 'Python', 10)
student_two.rate_lectors(lector_two, 'Python', 9)
print(lector_one)
print(lector_two)
print(student_one)
print(student_two)
print(reviewer_one)
print(reviewer_two)
print(student_two > student_one)
print(lector_one > lector_two)

student_list = [student_one, student_two]


def calculation_of_the_avarage_grade_student(list_student, name_course):
    avarage_grade = 0
    student_count = 0
    for student in list_student:
        if isinstance(student, Student) and name_course in student.courses_in_progress:
            student_count += 1
            for key, val in student.grades.items():
                if key == name_course:
                    avarage_grade += sum(val)
        else:
            print(f'Object {student.name} {student.surname} is not class Student or not enrolled in this course')
    return avarage_grade/len(list_student)


print(calculation_of_the_avarage_grade_student(student_list, 'Python'))
lector_list = [lector_one, student_one, lector_two]


def calculation_of_the_avarage_grade_lectors(list_lectors, name_course):
    avarage_grade = 0
    count_lector = 0
    for lector in list_lectors:
        if isinstance(lector, Lecturer) and name_course in lector.courses_attached:
            count_lector += 1
            for key, val in lector.grades.items():
                if key == name_course:
                    avarage_grade += sum(val)
        else:
            print(f'Object {lector.name} {lector.surname} is not class Lecturer or not enrolled in this course')
    return avarage_grade/count_lector


print(calculation_of_the_avarage_grade_lectors(lector_list, 'Python'))