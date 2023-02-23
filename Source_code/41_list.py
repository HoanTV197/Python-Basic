colors = ["red", "green", "blue", "yellow"]

print(colors)

# remove from list
try:
	colors.remove("green")
except:
	print("not exist")

print(colors)

# remove last element
colors.pop()
print(colors)

# add to list at specific index
colors.insert(0, "black")
print(colors)
colors.insert(1, "purple")
print(colors)

# find index of the first "red"
colors = ['black', 'purple', 'red', 'blue', 'red']
print(colors)
try:
	print("The first index of 'red': ", end="")
	print(colors.index("red"))
except:
	print("not exist")

# find index of "red" in list
red_index = []
for i in range(len(colors)):
	if colors[i] == "red":
		red_index.append(i)
print("The word 'red' occurs at the following index: ", end="")
print(red_index)

# find number of occurance of "red"
print("How many times 'red' occurs: "+ str(colors.count("red")))

print("Sort Example: ")
a = [1,2,10,4,5,0,6]
a.sort()
print(a)

# change the first element to 'dunglai'
a[0] = "dunglai"
print(a)