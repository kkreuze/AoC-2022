lines = open("D:\AA Projects\AoC-2022\days\day-4\input.txt", "r").read().splitlines()
lines = [x.replace(',','-') for x in lines]
lines = [x.split('-') for x in lines]
lines = [list(map(int, x)) for x in lines]

# solution 1
def containsinranges(x1,x2,y1,y2):
  return ((y1 <= x1 <= y2 and y1 <= x2 <= y2) or (x1 <= y1 <= x2 and x1 <= y2 <= x2))

print('the answer to the first question is:',(sum(containsinranges(a,b,c,d) for a,b,c,d in lines)))

#solution 2
def overlapingranges(x1,x2,y1,y2):
  return x1 <= y2 and y1 <= x2

print('the answer to the second question is:',(sum(overlapingranges(a,b,c,d) for a,b,c,d in lines)))

#show the speed in which the code runs
import time
start = time.time()
a = 0
for i in range(1000):
    a += (i**100)
end = time.time()
print("Code executed in:",(end-start) * 10**3, "ms")