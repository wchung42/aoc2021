
increases = 0

with open('day1-input.txt', 'r') as data:
    measurements = data.readlines()

windows = []

for i in range(0, len(measurements) - 2):    
    windows.append((int(measurements[i]), int(measurements[i+1]), int(measurements[i+2])))

print(windows[-1])

prev = None
for window in  windows:
    curr = sum(window)

    if prev is None:
        prev = curr
    elif prev < curr:
        increases += 1
    
    prev = curr

print(increases)
