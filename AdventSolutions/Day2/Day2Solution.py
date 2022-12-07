location = 'AdventSolutions/Day2/AdventData.txt'

def Day2Star1():
    with open(location) as data_file:
        lines = [{'dir': line.split()[0],'dist': int(line.split()[1])} for line in data_file]
        horizontal = depth = 0
        for i in range(len(lines)):
            if(lines[i]['dir'] == 'forward'): horizontal += lines[i]['dist']
            if(lines[i]['dir'] == 'up'): depth -= lines[i]['dist']
            if(lines[i]['dir'] == 'down'): depth += lines[i]['dist']
        print(f"Day 2 Star 1 Answer: {depth*horizontal}")

def Day2Star2():
    with open(location) as data_file:
        lines = [{'dir': line.split()[0],'dist': int(line.split()[1])} for line in data_file]
        horizontal = depth = aim = 0
        for i in range(len(lines)):
            if(lines[i]['dir'] == 'forward'): horizontal += lines[i]['dist']; depth += aim * lines[i]['dist']
            if(lines[i]['dir'] == 'up'): aim -= lines[i]['dist']
            if(lines[i]['dir'] == 'down'): aim += lines[i]['dist']
        print(f"Day 2 Star 2 Answer: {depth*horizontal}\n")