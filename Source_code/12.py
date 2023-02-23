# CURRENT_YEAR = 2021
# METER_TO_FEET = 3.281

# firstname = input("Your firstname: ")
# lastname = input("Your lastname: ")
# year_born = input("When you were born: ")
# height_meter = input("Your height (meter): ")

# year_born = int(year_born)
# age = CURRENT_YEAR - year_born

# height_meter = float(height_meter)
# height_feet = height_meter * METER_TO_FEET
# height_feet = round(height_feet,1)

# print("\n---")
# print("Your name is " + firstname + " " + lastname)
# print("{2} is {0} years old in {1}".format(age,CURRENT_YEAR,firstname))
# print("You are " + str(height_feet) + " feet tall")

gender_input = input("Are you male (yes/no): ")
is_male = None

if gender_input == "yes":
	is_male = True
elif gender_input == "no":
	is_male = False
else:
	is_male = None 