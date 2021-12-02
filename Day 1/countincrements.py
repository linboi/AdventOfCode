with open('input.txt', 'r') as file:
	lines = file.readlines()

incCount = 0
prev = lines[0]
lines = lines[1::]
for line in lines:
	if int(line) > int(prev):
		incCount += 1
	prev = line
print(incCount)