with open('input.txt', 'r') as file:
	lines = file.readlines()

forward = 0
depth = 0
aim = 0
for line in lines:
	if line.startswith("forward"):
		forward += int(line[7::])
		depth += aim*int(line[7::])
	elif line.startswith("down"):
		aim += int(line[4::])
	elif line.startswith("up"):
		aim -= int(line[2::])
print(forward*depth)