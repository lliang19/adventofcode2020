inputFile = open('input', 'r')
mapBoard = inputFile.read().split('\n')

def countTrees(right, down):
  xPos = 0
  yPos = 0
  treeCount = 0
  while yPos < len(mapBoard):
    xPos = (xPos + right) % len(mapBoard[0])
    yPos += down
    if (yPos >= len(mapBoard)):
      break
    if mapBoard[yPos][xPos] == '#':
      treeCount += 1
  return treeCount

print(countTrees(1, 1) * countTrees(3, 1) * countTrees(5, 1) * countTrees(7, 1) * countTrees(1, 2))