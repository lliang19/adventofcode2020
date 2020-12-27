inputFile = open('input', 'r')
count = 0
validMap = {
  'byr': False,
  'iyr': False,
  'eyr': False,
  'hgt': False,
  'hcl': False,
  'ecl': False,
  'pid': False
}
validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
for line in inputFile.read().split('\n'):
  if len(line) == 0:
    valid = True
    for key, value in validMap.items():
      valid = valid and value
      validMap[key] = False
    if valid:
      count += 1
  
  else:
    for passKey in line.split(' '):
      key = passKey.split(':')
      if key[0] in validMap.keys():
        if key[0] == 'byr':
          year = int(key[1])
          if len(key[1]) == 4 and year >= 1920 and year <= 2002:
            validMap[key[0]] = True
        elif key[0] == 'iyr':
          issueYear = int(key[1])
          if len(key[1]) == 4 and issueYear >= 2010 and issueYear <= 2020:
            validMap[key[0]] = True
        elif key[0] == 'eyr':
          expYear = int(key[1])
          if len(key[1]) == 4 and expYear >= 2020 and expYear <= 2030:
            validMap[key[0]] = True
        elif key[0] == 'hgt':
          if 'in' in key[1]:
            height = int(key[1][0:key[1].find('in')])
            if height >= 59 and height <= 76:
              validMap[key[0]] = True
          elif 'cm' in key[1]:
            height = int(key[1][0:key[1].find('cm')])
            if height >= 150 and height <= 193:
              validMap[key[0]] = True
        elif key[0] == 'hcl':
          if len(key[1]) == 7:
            validMap[key[0]] = True
            if key[1][0] != '#':
              validMap[key[0]] = False
            for char in key[1][1:]:
              asciiValue = ord(char)
              if not ((asciiValue >= 48 and asciiValue <= 57) or (asciiValue >= 97 and asciiValue <= 102)):
                validMap[key[0]] = False
        elif key[0] == 'ecl':
          if key[1] in validEyeColors:
            validMap[key[0]] = True
        elif key[0] == 'pid':
          if key[1].isdigit() and len(key[1]) == 9:
            validMap[key[0]] = True

valid = True
for key, value in validMap.items():
  valid = valid and value
  validMap[key] = False
if valid:
  count += 1

print(count)