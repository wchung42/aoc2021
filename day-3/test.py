with open('input.txt', 'r') as data:
    prompt = [line.strip() for line in data]
    
o2 = prompt
co2 = prompt
n = len(o2[0])
for i in range(n):
    gama = ''
    for index in range(n):
        ones = 0
        zeros = 0
        for line in o2:
            if line[index] == '1':
                ones += 1
            else:
                zeros += 1
        if ones >= zeros:
            gama += '1'
        else:
            gama += '0'
    if len(o2) > 1:
        o2 = [l for l in o2 if l[i] == gama[i]]
    epsilon = ''
    for index in range(n):
        ones = 0
        zeros = 0
        for line in co2:
            if line[index] == '1':
                ones += 1
            else:
                zeros += 1
        if ones < zeros:
            epsilon += '1'
        else:
            epsilon += '0'
    if len(co2) > 1:
        co2 = [l for l in co2 if l[i] == epsilon[i]]
        
print(int(o2[0],2) * int(co2[0],2))