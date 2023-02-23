CURRENT_YEAR = 2021

print("Your firstname: ")
firstname = input()

print("Your lastname: ")
lastname = input()

print("Your name is " + firstname + " " + lastname)

print("When you were born: ")
year_born = input()
year_born = int(year_born)

age = CURRENT_YEAR - year_born

print("You are " + str(age) + " years old in " + str(CURRENT_YEAR))