lines = open("D:\AA Projects\AoC-2022\days\day-3\input.txt", "r").read().splitlines()

# Solution 1
def split(s):
    half, rem = divmod(len(s), 2)
    return s[:half + rem], s[half + rem:]

#alvast sorry dat je dit moet zien :)
def lettervalue(input):
    if input == 'a': return(1) 
    if input == 'b': return(2) 
    if input == 'c': return(3)
    if input == 'd': return(4) 
    if input == 'e': return(5) 
    if input == 'f': return(6)
    if input == 'g': return(7)
    if input == 'h': return(8) 
    if input == 'i': return(9)
    if input == 'j': return(10) 
    if input == 'k': return(11) 
    if input == 'l': return(12)
    if input == 'm': return(13) 
    if input == 'n': return(14)
    if input == 'o': return(15)
    if input == 'p': return(16)
    if input == 'q': return(17)
    if input == 'r': return(18)
    if input == 's': return(19) 
    if input == 't': return(20) 
    if input == 'u': return(21)
    if input == 'v': return(22) 
    if input == 'w': return(23) 
    if input == 'x': return(24)
    if input == 'y': return(25)
    if input == 'z': return(26) 
    if input == 'A': return(27)
    if input == 'B': return(28) 
    if input == 'C': return(29) 
    if input == 'D': return(30)
    if input == 'E': return(31) 
    if input == 'F': return(32) 
    if input == 'G': return(33)
    if input == 'H': return(34)
    if input == 'I': return(35) 
    if input == 'J': return(36)
    if input == 'K': return(37)
    if input == 'L': return(38) 
    if input == 'M': return(39) 
    if input == 'N': return(40)
    if input == 'O': return(41)
    if input == 'P': return(42) 
    if input == 'Q': return(43)
    if input == 'R': return(44) 
    if input == 'S': return(45) 
    if input == 'T': return(46)
    if input == 'U': return(47) 
    if input == 'V': return(48) 
    if input == 'W': return(49)
    if input == 'X': return(50)
    if input == 'Y': return(51) 
    if input == 'Z': return(52)

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