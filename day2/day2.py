inputFile = open('input', 'r')
count = 0

# PART 1
#
# for line in inputFile.read().split('\n'):
#   parts = line.split(': ')
#   policy = parts[0].split(' ')
#   minmax = policy[0].split('-')
#   minimum = int(minmax[0])
#   maximum = int(minmax[1])
#   letter = policy[1]
#   letterCount = parts[1].count(letter)
#   if letterCount >= minimum and letterCount <= maximum:
#     count += 1
# 

# PART 2
#
for line in inputFile.read().split('\n'):
  parts = line.split(': ')
  policy = parts[0].split(' ')
  positions = policy[0].split('-')
  pos1 = int(positions[0]) - 1
  pos2 = int(positions[1]) - 1
  
  if pos1 >= len(parts[1]) or pos2 >= len(parts[1]):
    continue

  letter = policy[1]
  inPos1 = parts[1][pos1] == letter
  inPos2 = parts[1][pos2] == letter
  if (inPos1 and not inPos2) or (not inPos1 and inPos2):
    count += 1

print(count)
