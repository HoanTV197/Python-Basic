# Write mode - write to a new file
file = open("data.txt", "w")
file.write("dunglai\n")
file.write("dunglailaptrinh")
file.close()

# Write mode - write to a new file
file = open("data.txt", "w")
file.write("a\n")
file.write("b\n")
file.close()

# Append mode - write to an existing file
file = open("data.txt", "a")
file.write("c\n")
file.write("d\n")
file.write("e")
file.close()

# Reading mode - read a file
file = open("data.txt", "r")
data = file.read()
print(data)
file.close()
