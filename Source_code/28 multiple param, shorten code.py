def main():
	student_A_name = "Dung"
	student_A_math_score = 9
	student_A_literature_score = 6

	student_B_name = "Nguyen"
	student_B_math_score = 6
	student_B_literature_score = 8

	print_student(student_A_name, student_A_math_score, student_A_literature_score)
	print_student(student_B_name, student_B_math_score, student_B_literature_score)

def print_student(name, math_score, literature_score):
	print("Student name: " + name)
	print("Math: " + str(math_score))
	print("Literature: " + str(literature_score))

main()

