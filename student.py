class Student:
  def __init__(self,__grade):
    self.__grade=grade
  def grade(self,grade):
    self.__grade+=grade
  def get_grade(self):
    return self.__grade
student=Student(80)
student.grade(20)
print(student.get_grade())
