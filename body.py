
from collections import Counter
# Актуализировать список курсов
def up_ava_cr():
    available_courses.clear()
    for lec in list_lecturer:
            for i in range(len(lec.courses_attached)):
                if lec.courses_attached[i] not in available_courses:
                    available_courses.append(lec.courses_attached[i])
            
    print("Список курсов актуализирован: ")
    print(*available_courses, sep = "\n")
#Средняя оценка студентов в рамках курса
def score_st():
    print("функция: cредняя оценка студентов в рамках курса")
    def calc(crs_):
        #Считаем повторы    
        cnt = Counter(st.grades[crs_])
        #Средний балл
        sm_score = 0.0
        rpl_score = 0.0
        for i in cnt:
            sm_score += i*cnt[i]
            rpl_score += cnt[i]
        crs_score = sm_score/rpl_score
        #проверяем есть ли в словаре курс (ключ)
        if crs_ not in score:
            score[crs_] = []
        #Добавляем в значение(список) средний балл
        score[crs_].append(crs_score)
    up_ava_cr()
    course = input("Введите интересующий курс или all: ")
    score = {}
    #Студент
    for st in list_student:
        #курс
        if course == "all":
            for crs in st.grades.keys():
                calc(crs)
        else:
            calc(course)
    #Вывод данных
    if course == "all":
        for crs in score:
            print(f"Средний балл за курс {crs} всех студентов {sum(score[crs])}")
    else:
        print(f"Средний балл за курс {course} всех студентов {sum(score[course])}")
#Средняя оценка лекторов в рамках курса
def score_lc():
    print("функция: cредняя оценка лекторов в рамках курса")
    def calc(crs_):
        #Считаем повторы    
        cnt = Counter(lc.grades_lec[crs_])
        #Средний балл
        sm_score = 0.0
        rpl_score = 0.0
        for i in cnt:
            sm_score += i*cnt[i]
            rpl_score += cnt[i]
        crs_score = sm_score/rpl_score
        #проверяем есть ли в словаре курс (ключ)
        if crs_ not in score:
            score[crs_] = []
        #Добавляем в значение(список) средний балл
        score[crs_].append(crs_score)
    up_ava_cr()
    course = input("Введите интересующий курс или all: ")
    score = {}
    #Лектор
    for lc in list_lecturer:
        #курс
        if course == "all":
            for crs in lc.grades_lec.keys():
                calc(crs)
        else:
            calc(course)
    #Вывод данных
    if course == "all":
        for crs in score:
            print(f"Средний балл за курс {crs} всех Лекторов {sum(score[crs])}")
    else:
        print(f"Средний балл за курс {course} всех Лекторов {sum(score[course])}")

#Студенты
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        list_student.append(self)
       

    def add_courses(self, course_name):
        self.courses_in_progress.append(course_name)
        
    
    def fin_curses(self, course_name):
        self.courses_in_progress.remove(course_name)
        self.finished_courses.append(course_name)
        

    def score_lec(self, lecturer, course, grade):
        if type(grade) != int or grade > 10 or grade < 0:
            print("Внимание доступны только целые числа в диапазоне от 1 до 10!")
        else:
            if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
                if course in lecturer.grades_lec:
                    lecturer.grades_lec[course] += [grade]
                else:
                    lecturer.grades_lec[course] = [grade]
            else:
                print('Ошибка')

    def calc(self, cour):
        def cal_ (cr):
            #Считаем повторы    
            cnt = Counter(self.grades[cr])
            #Средний балл
            sm_score = 0.0
            rpl_score = 0.0
            for i in cnt:
                sm_score += i*cnt[i]
                rpl_score += cnt[i]
            crs_score = sm_score/rpl_score
            return crs_score

        sum = 0.0
        if cour == "all":
            for crs in self.courses_in_progress:
                if self.grades.get(crs) == None:
                    print("Оценки отсутствуют")
                else:
                    sum += cal_(crs)
        else:
            if self.grades.get(crs) == None:
                print("Оценки отсутствуют") 
            else:    
                sum += cal_(cour)
        return sum

    #   ==
    def __eq__(self, other):
            if not isinstance(other, type(self)):
                print("Не соответствие ТИПОВ")
            else:
                if self.calc("all") != other.calc("all"):
                    m_ax = [self.calc("all"), other.calc("all")]
                    m_in = [self.calc("all"), other.calc("all")]
                    print(f"Оценки отличаются! Разница = {max(m_ax)-min(m_in)}")
                    if self.calc("all") > other.calc("all"):
                        print(f"{self.name} > {other.name}")
                    else:
                        print(f"{self.name} < {other.name}") 
                else:
                    print(f"{self.name} = {other.name}")        
    #   != 
    def __ne__(self, other):
        if not isinstance(other, type(self)):
            print("Не соответствие ТИПОВ")
        else:
            self.__eq__(other)
    #    <
    def __lt__(self, other):
        if not isinstance(other, type(self)):
            print("Не соответствие ТИПОВ")
        else:
            self.__eq__(other)      
    #   <=
    def __le__(self, other):
        if not isinstance(other, type(self)):
            print("Не соответствие ТИПОВ")
        else:
            self.__eq__(other)          
    #      >
    def __gt__(self, other):
        if not isinstance(other, type(self)):
            print("Не соответствие ТИПОВ")
        else:
            self.__eq__(other)        
    #       >=
    def __ge__(self, other):
        if not isinstance(other, type(self)):
            print("Не соответствие ТИПОВ")
        else:
            self.__eq__(other)
            
    def __str__(self):
        return f"""
                Имя: {self.name}
                Фамилия: {self.surname}
                Средняя оценка за домашние задания: {self.calc("all")}
                Курсы в процессе изучения: {self.courses_in_progress}
                Завершенные курсы: {self.finished_courses}
                """
    __repr__ = __str__
#Родительский класс
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
        #   ==
    def __eq__(self, other):
            if not isinstance(other, type(self)):
                print("Не соответствие ТИПОВ")
            else:
                if self.calc("all") != other.calc("all"):
                    m_ax = [self.calc("all"), other.calc("all")]
                    m_in = [self.calc("all"), other.calc("all")]
                    print(f"Оценки отличаются! Разница = {max(m_ax)-min(m_in)}")
                    if self.calc("all") > other.calc("all"):
                        print(f"{self.name} > {other.name}")
                    else:
                        print(f"{self.name} < {other.name}") 
                else:
                    print(f"{self.name} = {other.name}")        
    #   != 
    def __ne__(self, other):
        if not isinstance(other, type(self)):
            print("Не соответствие ТИПОВ")
        else:
            self.__eq__(other)
    #    <
    def __lt__(self, other):
        if not isinstance(other, type(self)):
            print("Не соответствие ТИПОВ")
        else:
            self.__eq__(other)      
    #   <=
    def __le__(self, other):
        if not isinstance(other, type(self)):
            print("Не соответствие ТИПОВ")
        else:
            self.__eq__(other)          
    #      >
    def __gt__(self, other):
        if not isinstance(other, type(self)):
            print("Не соответствие ТИПОВ")
        else:
            self.__eq__(other)        
    #       >=
    def __ge__(self, other):
        if not isinstance(other, type(self)):
            print("Не соответствие ТИПОВ")
        else:
            self.__eq__(other)

#Ревьюеры 
class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        list_reviewer.append(self)

    def rate_hw(self, student, course, grade):
        if type(grade) != int or grade > 10 or grade < 0:
            print("Внимание доступны только целые числа в диапазоне от 1 до 10!")
        else:
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                print("Ошибка")


    def __str__(self):
        return f"""
                Имя: {self.name} 
                Фамилия: {self.surname}
                """
#Лекторы
class Lecturer(Mentor):
    #котором ключи – названия курсов, а значения – списки оценок
    #должен быть закреплен за тем курсом, на который записан студент
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lec = {}
        list_lecturer.append(self)
        
        
    def add_courses(self, course_name):
        if course_name in self.courses_attached:
            print("Данный лектор уже ведет данный курс!")
        else:
            self.courses_attached.append(course_name)
        if course_name not in self.grades_lec:
            self.grades_lec[course_name] = []
        if course_name not in available_courses:
            available_courses.append(course_name)
        

    def calc(self, cour):
        def cal_ (cr):
            #Считаем повторы    
            cnt = Counter(self.grades_lec[cr])
            #Средний балл
            sm_score = 0.0
            rpl_score = 0.0
            for i in cnt:
                sm_score += i*cnt[i]
                rpl_score += cnt[i]
            crs_score = sm_score/rpl_score
            return crs_score

        sum = 0.0
        if cour == "all":
            for crs in self.courses_attached:
                if self.grades_lec.get(crs) == None:
                    print("Оценки отсутствуют")
                else:
                    sum += cal_(crs)
        else:
            if self.grades_leces.get(crs) == None:
                print("Оценки отсутствуют")
            else:    
                sum += cal_(cour)
        return sum  


    def __str__(self):
        return f"""
                Имя: {self.name}
                Фамилия: {self.surname}
                Средняя оценка за лекции: {self.calc("all")}
                """


#Список всех курсов (актуализируется функцией)
available_courses = ["Python","SQL","Java"]
#Данный список хранит в себе экземляры класса Lecturer, добавленны тестовые данные
list_lecturer = []
#Данный список хранит в себе экземляры класса Student, добавленны тестовые данные
list_student = []
#Данный список хранит в себе экземпляры класса Reviewer, добавленны тестовые данные
list_reviewer = []

#Создаём обьект "лектор"
standart_lecturer = Lecturer("Brad", "Facker")
midle_lecturer = Lecturer("Brady", "Op's")
best_lecturer = Lecturer("Dony", "Hook")
#Создаём обьект "студент"
best_student = Student('Ruoy', 'Eman', 'your_gender')
low_student1 = Student('Noah', 'Mcbride', 'your_gender')
low_student2 = Student('Brian', 'Ryan', 'your_gender')
low_student3 = Student('Jeffry', 'Harmon', 'your_gender')
low_student4 = Student('Gwendoline', 'Oliver', 'your_gender')
low_student5 = Student('Estella', 'Holt', 'your_gender')
low_student6 = Student('Anabel', 'Mcgee', 'your_gender')
#Создаём обьект "ревьюер"
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer2 = Reviewer('Some2', 'Buddy2')
#Добавляем курсы лекторам
standart_lecturer.add_courses("Python")
midle_lecturer.add_courses("Python")
best_lecturer.add_courses("Python")
#Добавляем курсы студентам
best_student.courses_in_progress += ['Python']
low_student1.courses_in_progress += ['Python']
low_student1.finished_courses += ["C#"]
low_student2.courses_in_progress += ['Python']
low_student2.finished_courses += ["C#"]
low_student3.courses_in_progress += ['Python']
low_student3.finished_courses += ["C#"]
low_student4.courses_in_progress += ['Python']
low_student4.finished_courses += ["C#"]
low_student5.courses_in_progress += ['Python']
low_student5.finished_courses += ["C#"]
low_student6.courses_in_progress += ['Python']
low_student6.finished_courses += ["C#"]
#Добавили ревьюерам курсов
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['C#']
cool_reviewer2.courses_attached += ['Python']
cool_reviewer2.courses_attached += ['C#']
#выставляем оценки (студент - лектору)
best_student.score_lec(standart_lecturer, "Python", 7)
best_student.score_lec(midle_lecturer, "Python", 3)
best_student.score_lec(best_lecturer, "Python", 10)
low_student1.score_lec(standart_lecturer, "Python", 6)
low_student2.score_lec(midle_lecturer, "Python", 4)
low_student3.score_lec(best_lecturer, "Python", 3)
low_student4.score_lec(standart_lecturer, "Python", 6)
low_student5.score_lec(midle_lecturer, "Python", 4)
low_student6.score_lec(best_lecturer, "Python", 3)
#выставляем оценки (ревьюер - студенту)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer2.rate_hw(best_student, 'Python', 3)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(low_student1, 'Python', 5)
cool_reviewer2.rate_hw(low_student2, 'Python', 5)
cool_reviewer2.rate_hw(low_student3, 'Python', 2)
cool_reviewer.rate_hw(low_student4, 'Python', 6)
cool_reviewer.rate_hw(low_student5, 'Python', 10)
cool_reviewer2.rate_hw(low_student5, 'Python', 3)
cool_reviewer.rate_hw(low_student5, 'Python', 10)
cool_reviewer.rate_hw(low_student6, 'Python', 10)
 

print("======"*16)
print("Выводим студента")
print(best_student)
print("======"*16)
print("Выводим лектора")
print(standart_lecturer)
print("======"*16)
print("Выводим Ревюера")
print(cool_reviewer)
print("======"*16)
print("Попытка сравнения лектора и ревьюера")
best_student == cool_reviewer
print("======"*16)
print("Сравниваем лекторов")
midle_lecturer == standart_lecturer
print("======"*16)
print("Сравниваем студентов")
best_student == low_student1
best_student <= low_student3
best_student >= low_student4
best_student != low_student5
best_student > low_student6
best_student < low_student2
print("======"*16)
score_st()
print("======"*16)
score_lc()