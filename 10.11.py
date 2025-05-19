#10.11

class Student:
    def __init__(self, name, student_id, korean_quiz=0, math_quiz=0, science_quiz=0):
        self.__name = name 
        self.__student_id = student_id 
        self.__korean_quiz = korean_quiz
        self.__math_quiz = math_quiz
        self.__science_quiz = science_quiz
        self.__total_score = korean_quiz + math_quiz + science_quiz

    def __str__(self):
        return f"이름 : {self.__name}, 학번 : {self.__student_id}\n" \
               f"국어성적 : {self.__korean_quiz}, 수학성적 : {self.__math_quiz} 과학성적 : {self.__science_quiz}" \
               f"합계 : {self.__total_score}, 평균 : {self.get_avg_score()}"                                                                   

    def get_name(self):
        return self.__name

    def get_korean_quiz(self):
        return self.__korean_quiz

    def get_math_quiz(self):
        return self.__math_quiz

    def get_science_quiz(self):
        return self.__science_quiz

    def set_korean_quiz(self, score):
        self.__korean_quiz = score
        self.__total_score = self.__korean_quiz + self.__math_quiz + self.__science_quiz

    def set_math_quiz(self, score):
        self.__math_quiz = score
        self.__total_score = self.__korean_quiz + self.__math_quiz + self.__science_quiz

    def set_science_quiz(self, score):
        self.__science_quiz = score
        self.__total_score = self.__korean_quiz + self.__math_quiz + self.__science_quiz

    def set_total_score(self):
        return self.__total_score

    def get_avg_score(self):
        return self.__total_score / 3

name = input('학생의 이름을 입력하세요 : ')
student_id = input('학생의 학번을 입력하세요.')
student = Student(name, student_id) #student 객체를 생성

korean_quiz = int(input('학생의 국어 성적을 입력하세요 : '))
math_quiz = int(input('학생의 수학 성적을 입력하세요 : '))
science_quiz = int(input('학생의 과학 성적을 입력하세요 : '))
student.set_korean_quiz(korean_quiz)
student.set_math_quiz(math_quiz)
student.set_science_quiz(science_quiz)
print(student)


