s_denominator = 0

for i in range(100):
	if i == 1:
		continue

	if i % 2 == 0:
		continue

	s_denominator += 1/i

s = 1/s_denominator
s = round(s,2)
print("S = " + str(s))