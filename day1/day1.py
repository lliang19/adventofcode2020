inputFile = open('input', 'r')
entries = inputFile.read().split('\n')
for entry1 in entries:
  entry1Num = int(entry1)
  complement1 = 2020 - entry1Num
  for entry2 in entries:
    entry2Num = int(entry2)
    complement2 = complement1 - entry2Num
    if (str(complement2) in entries):
      print(entry1Num * entry2Num * complement2)