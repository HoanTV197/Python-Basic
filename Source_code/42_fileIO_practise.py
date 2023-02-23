# Create a program that asks an user to enter an integer
# Write to a file named "data.txt" all integers from the previous integer to 0 on each line
# Read the file "data.txt" and print to the terminal all lines and its corresponding integer

user_input = int(input("Enter an integer: "))

with open("data.txt", "w") as file:
	for i in range(user_input):
		file.write(str(user_input - i) + "\n")

numbers = []

with open("data.txt", "r") as file:
	numbers = file.read().split("\n")
	numbers.pop()

for i in range(numbers):
	print("Line " + str(i+1) + ": " + numbers[i])