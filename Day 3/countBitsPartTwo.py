def main():
	with open('input.txt', 'r') as file:
		lines = file.readlines()

	for idx, line in enumerate(lines):
		if line[-1] == '\n':
			lines[idx] = line[:-1:]
	oxygenPossibilities = lines.copy()
	CO2Possibilities = lines.copy()

	bitPos = 0
	while(len(oxygenPossibilities) > 1):
		count = 0
		for inputLine in oxygenPossibilities:
			if inputLine[bitPos] == '1':
				count += 1
		if count >= len(oxygenPossibilities)/2:
			leastCommon = '0'
		else: 
			leastCommon = '1'
		x = 0
		while x != len(oxygenPossibilities):
			if oxygenPossibilities[x][bitPos] == leastCommon:
				oxygenPossibilities.remove(oxygenPossibilities[x])
				x -= 1
			x += 1
		bitPos += 1
	bitPos = 0
	while(len(CO2Possibilities) > 1):
		count = 0
		for inputLine in CO2Possibilities:
			if inputLine[bitPos] == '1':
				count += 1
		if count >= len(CO2Possibilities)/2:
			mostCommon = '1'
		else: 
			mostCommon = '0'
		x = 0
		while x != len(CO2Possibilities):
			if CO2Possibilities[x][bitPos] == mostCommon:
				CO2Possibilities.remove(CO2Possibilities[x])
				x -= 1
			x += 1
		bitPos += 1
	result = stringToInt(CO2Possibilities[0])*stringToInt(oxygenPossibilities[0])
	print(result)

def stringToInt(s):
	s = s[::-1]
	exponent = 0
	result = 0
	for c in s:
		if c == '1':
			result += 2**exponent
		exponent += 1
	return result

if __name__ == '__main__':
	main()