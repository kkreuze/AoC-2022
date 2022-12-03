lines = open("D:\AA Projects\AoC-2022\days\day-3\input.txt", "r").read().splitlines()

# Solution 1
def split(s):
    half, rem = divmod(len(s), 2)
    return s[:half + rem], s[half + rem:]

def lettervalue(input):
    if input.isupper():
        return int(input.lower(), 36) + 17
    return int(input, 36) - 9

totalvalue = 0

for line in lines:
    Start, End = split(line)
    letter = match = set(Start) & set(End)
    lettergood = str(letter).replace('{','').replace('}','').replace('\'','').replace('\"','')
    totalvalue += lettervalue(lettergood)

print('The Answer is:', totalvalue)


#Solution 2
totalvalue2 = 0
for i in range(0, len(lines), 3):
    letter2 = match = set(lines[i]) & set(lines[i+1]) & set(lines[i+2])
    lettergood2 = str(letter2).replace('{','').replace('}','').replace('\'','').replace('\"','')
    totalvalue2 += lettervalue(lettergood2)
print('The Answer is:', totalvalue2)



#show the speed in which the code runs
import time
start = time.time()
a = 0
for i in range(1000):
    a += (i**100)
end = time.time()
print("Code executed in:",(end-start) * 10**3, "ms")