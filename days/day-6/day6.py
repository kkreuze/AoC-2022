lines = open("D:\AA Projects\AoC-2022\days\day-6\input.txt", "r").read()

# solution 1
pairsize = 4

for a, b in enumerate(lines):
    possiblepairs = lines[a:a+pairsize]
    if len(set(possiblepairs)) == pairsize and possiblepairs[0] != '':
        print('The Aswer to the first problem is:',a + pairsize)
        break

#solution 2
pairsize2 = 14

for a, b in enumerate(lines):
    possiblepairs2 = lines[a:a+pairsize2]
    if len(set(possiblepairs2)) == pairsize2 and possiblepairs2[0] != '':
        print('The Aswer to the second problem is:',a + pairsize2)
        break
