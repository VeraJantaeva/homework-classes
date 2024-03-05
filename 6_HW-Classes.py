# Класс студентов
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade(self.grades)}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return output

    def rate_lecturer(self, specific_lecturer, course, grade):
        if isinstance(specific_lecturer, Lecturer) \
                and course in specific_lecturer.courses_attached \
                and course in self.courses_in_progress \
                and 0 < grade <= 10:

            specific_lecturer.grades.append(grade)

        else:
            return 'Ошибка'

    def __lt__(self, other_student):
        if isinstance(other_student, Student):
            return average_grade(self.grades) < average_grade(other_student.grades)
        else:
            return None


# Класс преподавателей
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


# Класс лекторов
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        self.courses_attached = []

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade(self.grades)}'
        return output

    def __lt__(self, other_lecturer):
        if isinstance(other_lecturer, Lecturer):
            return average_grade(self.grades) < average_grade(other_lecturer.grades)
        else:
            return None


# Класс экспертов
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}'
        return output

    # Метод класса оценки студентов
    def rate_hw(self, specific_student, course, grade):
        if isinstance(specific_student, Student) \
                and course in self.courses_attached \
                and course in specific_student.courses_in_progress:

            if course in specific_student.grades:
                specific_student.grades[course] += [grade]
            else:
                specific_student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Функция расчета среднего значения оценок:
def average_grade(all_grades):
    if type(all_grades) is dict:
        amount_grades = []
        for grades in all_grades.values():
            for grade in grades:
                amount_grades.append(grade)
        return average_grade(amount_grades)
    elif type(all_grades) is list and all_grades[0] != None:
        average = round(sum(all_grades) / len(all_grades), 2)
        return average
    else:
        return "Ошибка! Оценки храняться не в словаре и не в списке, или список состоит из вложенных списков"


# Функция расчета среднего значения оценок:
def average_course_grade(all_students, current_course):
    all_course_grades = []
    for current_student in all_students:
        if current_course in current_student.grades.keys():
            for every_grade in current_student.grades.get(current_course):
                all_course_grades.append(every_grade)
        else:
            print(f'Курс {current_course} отсутствует у студента {current_student.name} {current_student.surname}')
    return average_grade(all_course_grades)


# Функция расчета среднего значения оценок:
def average_lecturers_grade(all_lecturers, current_course):
    all_lecturers_grades = []
    for current_lecturer in all_lecturers:
        for every_grade in current_lecturer.grades:
            all_lecturers_grades.append(every_grade)
    return average_grade(all_lecturers_grades)


# Создание экземпляра класса студент1:
student_no_1 = Student('Roy', 'Eman', '25')
student_no_1.courses_in_progress += ['Python']
student_no_1.courses_in_progress += ['English for IT']
student_no_1.finished_courses += ['Git']
student_no_1.add_courses('Math')
student_no_1.grades['Git'] = [7, 2, 6]
student_no_1.grades['Python'] = [10, 10, 8, 10, 10, 10]
student_no_1.grades['English for IT'] = [10, 10]
# Создание экземпляра класса студент2:
student_no_2 = Student('Mike', 'Red', '45')
student_no_2.courses_in_progress += ['Python']
student_no_2.finished_courses += ['Git']
student_no_2.grades['Git'] = [9, 5, 2]
student_no_2.grades['Python'] = [8, 10]
# Допустим мы их храним в списке (для функции average_course_grade):
student_list = [student_no_1, student_no_2]

# Создание экземпляра класса лектор1:
lecturer_1 = Lecturer('Bill', 'Boops')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['English for IT']
lecturer_1.courses_attached += ['Git']

# Создание экземпляра класса лектор2:
lecturer_2 = Lecturer('Ray', 'Bitts')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['English for IT']
lecturer_2.courses_attached += ['Git']

# Допустим мы их храним в списке (для функции average_lecturers_grade):
lecturer_list = [lecturer_1, lecturer_2]

# Создание экземпляра класса Эксперт:
cool_reviewer = Reviewer('Anton', 'Green')
cool_reviewer.courses_attached += ['Python']

# Создание экземпляра класса Эксперт2:
cool_reviewer_2 = Reviewer('Eddy', 'Grey')
cool_reviewer_2.courses_attached += ['Git']

# Проверяем

print('печать классов')
print(lecturer_2)
print()
print(cool_reviewer)
print()
print(student_no_1)
print()
print(student_no_2)
print()

print('Средний балл студентов по определенному курсу')
print(average_course_grade(student_list, 'Python'))

print('Cредний балл лекторов по всем курсам')
print(average_lecturers_grade(lecturer_list))

# print("сравнение")
# print(student_no_1 < student_no_2)
# print(student_no_2 < student_no_1)
# print(student_no_1 > student_no_2)
# print(student_no_2 > lecturer_1)

# print(lecturer_1 < lecturer_2)
# print(lecturer_1 < lecturer_2)
# print(lecturer_1 > lecturer_2)
# print(lecturer_1 > student_no_1)

