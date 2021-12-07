increases = 0

with open('p1-input.txt', 'r') as data:
    prev = None
    for line in data.readlines():
        curr = int(line)
        
        if prev is None:
            prev = curr
        elif curr > prev:
            increases += 1
        
        prev = curr

print(increases)