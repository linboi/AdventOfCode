with open('input.txt', 'r') as file:
	lines = file.readlines()

counts = [0]*(len(lines[0])-1)
for line in lines:
	for i, c in enumerate(line):
		if c == '1':
			counts[i] += 1

gamma = 0
epsilon = 0
counts.reverse()
exponent = 0
for count in counts:
	if count > len(lines)/2:
		gamma = gamma + 2**exponent
	else:
		epsilon = epsilon + 2**exponent
	exponent += 1
print(epsilon*gamma)