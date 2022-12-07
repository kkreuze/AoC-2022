#solution 1
with open("D:\AA Projects\AoC-2022\days\day-5\input.txt") as f:
    contents1, sentinel, contents2 = f.read().partition("\n\n")
with open("D:\AA Projects\AoC-2022\days\day-5\order", "w") as f:
    f.write(contents1)
with open("D:\AA Projects\AoC-2022\days\day-5\commands", "w") as f:
    f.write(contents2)

orderarr = open("D:\AA Projects\AoC-2022\days\day-5\order", "r").read()



commands = open("D:\AA Projects\AoC-2022\days\day-5\commands", "r").read()
numbercommands = [int(i) for i in commands.split() if i.isdigit()]
for i in range(0, len(numbercommands), 3):
    amount = numbercommands[i]
    start = numbercommands[i+1]
    end = numbercommands[i+2]
    print(amount, start, end)

#gave up on this one
