location = 'AdventSolutions/Day1/AdventData.txt'

def Day1Star1():
    with open(location) as data_file:
        lines = [int(line.strip()) for line in data_file]
        num = 0
        for i in range(1,len(lines)):
            if lines[i-1] < lines[i]:
                num += 1;
        print (f"Day 1 Star 1 Answer: {num}")

def Day1Star2():
    with open(location) as data_file:
        lines = [int(line.strip()) for line in data_file]
        num = 0
        for i in range(len(lines)):
            if(sum(lines[i:i+3]) < sum(lines[i+1:i+4])):
                num += 1
        print (f"Day 1 Star 2 Answer: {num}\n")