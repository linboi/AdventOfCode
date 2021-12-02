with open('input.txt', 'r') as file:
	lines = file.readlines()

incCount = 0
for x in range(3, len(lines)):
	if int(lines[x]) > int(lines[x-3]):
		incCount += 1

print(incCount)