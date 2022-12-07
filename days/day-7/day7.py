lines = open("D:\AA Projects\AoC-2022\days\day-7\input.txt", "r").read()

res = [int(i) for i in lines.split() if i.isdigit()]

total = 0
for i in res:
    if i < 100000:
        total += i
        print(total)
    else:
        print("too big")
print(total)

#kost me teveel moeite.