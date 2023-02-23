def main():
	student_A_name = "Dung" # local variable
	student_B_name = "Nguyen"
	print_student_A(student_A_name)
	print_student_B(student_B_name)

def print_student_A(name):
	print("Student A:")
	print("Name: " + name)
	print("Toan: 9")
	print("Van: 6")

def print_student_B(name):
	print("Student B:")
	print("Name: " + name)
	print("Toan: 5")
	print("Van: 7")

# student_A_name = "Dung" # global variable
main()

