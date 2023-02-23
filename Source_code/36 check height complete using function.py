import datetime

def ask_yes_no(prompt):
	while True:
		answer = input(prompt)
		if answer == "yes":
			return True
		elif answer == "no":
			return False
		else:
			continue

def calculate_age(year_born):
	now = datetime.datetime.now()
	CURRENT_YEAR = now.year
	return CURRENT_YEAR - year_born

def convert_meter_to_feet(meter):
	METER_TO_FEET = 3.281
	feet = meter * METER_TO_FEET
	feet = round(feet,1)
	return feet

def print_height_info(height_feet, is_male):
	if is_male == True:
		if height_feet > 6.5:
			print("You are", end=" ")
			for i in range(10):
				print("very", end=" ")
			print("tall as a man")
		elif height_feet > 6.0:
			print("You are tall as a man")
		else:
			print("You are short as a man")
	else:
		if height_feet > 5.7:
			print("You are tall as a girl")
		elif height_feet < 5.0:
			print("You are", end=" ")
			i=0
			while i<10:
				print("very ", end = "")
				i+=1
			print("short as a girl")
		else:
			print("You are short as a girl")	

def print_person_info(firstname, lastname, age, height_feet, is_vietnamese, is_male):
	now = datetime.datetime.now()
	CURRENT_YEAR = now.year
	print("\n---")
	print("Your name is " + firstname + " " + lastname)
	print("{2} is {0} years old in {1}".format(age,CURRENT_YEAR,firstname))
	print("You are " + str(height_feet) + " feet tall")
	if is_vietnamese:
		print("You are from Vietnam")
	else:
		print("You are not from Vietnam")
	print_height_info(height_feet, is_male)

def ask_person_info():
	firstname = input("Your firstname: ")
	lastname = input("Your lastname: ")
	year_born = int(input("When you were born: "))
	height_meter = float(input("Your height (meter): "))
	is_male = ask_yes_no("Are you male (yes/no): ")
	is_vietnamese = ask_yes_no("Are you Vietnamese (yes/no): ")
	return firstname, lastname, year_born, height_meter, is_male, is_vietnamese

def main():
	firstname, lastname, year_born, height_meter, is_male, is_vietnamese = ask_person_info()
	age = calculate_age(year_born)
	height_feet = convert_meter_to_feet(height_meter)
	print_person_info(firstname, lastname, age, height_feet, is_vietnamese, is_male)

main()