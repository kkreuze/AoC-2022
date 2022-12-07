lines = open("D:\AA Projects\AoC-2022\days\day-6\input.txt", "r").read()

# solution 1 + 2
def findSolution(pairsize):
  for a, b in enumerate(lines):
    possiblepairs = lines[a:a+pairsize]
    if len(set(possiblepairs)) == pairsize and possiblepairs[0] != '':
        return(a + pairsize)

print(findSolution(4))
print(findSolution(14))
