# while loop

i=0
while i<5:
	print(i)

	i += 1

print("\n ---- \n")

i=0
while i<10:
	i+=1
	if i==5:
		continue
	print(i)

print("\n ---- \n")

i=0
while True:
	print(i)
	i += 1
	if i==5:
		break

print("\n ---- \n")

i=11
while i>1:
	i -= 2
	if i == 5:
		continue
	print(i)