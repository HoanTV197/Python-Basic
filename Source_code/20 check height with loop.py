CURRENT_YEAR = 2021
METER_TO_FEET = 3.281

firstname = input("Your firstname: ")
lastname = input("Your lastname: ")
year_born = input("When you were born: ")
height_meter = input("Your height (meter): ")
gender_input = input("Are you male (yes/no): ")

year_born = int(year_born)
age = CURRENT_YEAR - year_born

height_meter = float(height_meter)
height_feet = height_meter * METER_TO_FEET
height_feet = round(height_feet,1)

print("\n---")
print("Your name is " + firstname + " " + lastname)
print("{2} is {0} years old in {1}".format(age,CURRENT_YEAR,firstname))
print("You are " + str(height_feet) + " feet tall")

is_male = None

if (gender_input == "yes") or (gender_input == "y") or (gender_input == "Yes"):
	is_male = True
elif (gender_input == "no") or (gender_input == "n") or (gender_input == "No"):
	is_male = False
else:
	is_male = None 

if is_male == None:
	print("Invalid Answer")
elif is_male == True:
	if height_feet > 6.5:
		print("You are", end=" ")

		# print "very" 10 times using for
		for i in range(10):
			print("very", end=" ")

		print("tall as a man")
	elif height_feet > 6.0:
		print("You are tall as a man")
	else:
		print("You are short as a man")
elif is_male == False:
	if height_feet > 5.7:
		print("You are tall as a girl")
	elif height_feet < 5.0:
		print("You are", end=" ")

		# print "very" 10 times using while
		i=0
		while i<10:
			print("very ", end = "")
			i+=1

		print("short as a girl")
	else:
		print("You are short as a girl")
else:
	print("System error: Variable 'is_male' is not correct")


