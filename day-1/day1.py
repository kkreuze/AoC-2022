with open("D:\AA Projects\AoC-2022\day-1\input.txt") as file:
    total_calories = sorted(sum(int(food) for food in calories.split("\n")) for calories in (elf for elf in file.read().strip().split("\n\n")))
    print('the solution to the first problem is:',total_calories[-1])
    print('the solution to the second problem is:',sum(total_calories[-3:]))



#show the speed in which the code runs
import time
start = time.time()
a = 0
for i in range(1000):
    a += (i**100)
end = time.time()
print("Code executed in :",(end-start) * 10**3, "ms")