lines = open("D:\AA Projects\AoC-2022\days\day-2\input.txt", "r").read().splitlines()

#Solution 1
def games (input):
    if input == 'A X': return(1 + 3) 
    if input == 'A Y': return(2 + 6) 
    if input == 'A Z': return(3 + 0)
    if input == 'B X': return(1 + 0) 
    if input == 'B Y': return(2 + 3) 
    if input == 'B Z': return(3 + 6)
    if input == 'C X': return(1 + 6)
    if input == 'C Y': return(2 + 0) 
    if input == 'C Z': return(3 + 3)

totalpoints = 0
for line in lines:
    totalpoints += games(line)

print('You have:', totalpoints,'points')


#Solution 2


#show the speed in which the code runs
import time
start = time.time()
a = 0
for i in range(1000):
    a += (i**100)
end = time.time()
print("Code executed in :",(end-start) * 10**3, "ms")