class Student:
	def __init__(self,name,age,math_score,literature_score):
		self.name = name
		self.age = age
		self.math_score = math_score
		self.literature_score = literature_score
		self.teacher = "Dung Lai"

	def average_score(self):
		self.ave_score = (self.math_score + self.literature_score)/2
		return self.ave_score

	def print_info(self):
		ave_score = str(self.average_score())
		print("Student name " + self.name + " study with " + self.teacher + " have average score " + ave_score)	

students = []

s1 = Student("David", 21, 9, 7)
s2 = Student("Bob", 19, 5, 6)
s3 = Student("Jenny", 29, 10,6)

s2.teacher = "Jane"

students.append(s1)
students.append(s2)
students.append(s3)

for i in range(len(students)):
	students[i].print_info()
