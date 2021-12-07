def bin2dec(bin):
    '''Converts binary number to decimal number; Returns decimal'''
    result = 0
    
    for i in range(len(bin)):
        result += int(bin[-(i+1)]) * (2**i)

    return result

with open('input.txt', 'r') as data:
    report = [line.strip() for line in data]

o2 = report[:]
co2 = report[:]
n = len(o2[0])
o2_bits = ''
co2_bits = ''

for i in range(n):
    zeros = 0
    ones = 0

    for line in o2:
        if line[i] == '0':
            zeros += 1
        else:
            ones += 1
        
    if ones > zeros:
        o2_bits += '1'
    elif ones < zeros:
        o2_bits += '0'
    else:
        o2_bits += '1'

    if len(o2) > 1:
        for line in o2[:]: 
            if o2_bits[i] != line[i]: o2.remove(line)
    
    zeros = 0
    ones = 0
    for line in co2:
        if line[i] == '0':
            zeros += 1
        else:
            ones += 1

    if ones > zeros:
        co2_bits += '0'
    elif ones < zeros:
        co2_bits += '1'
    else:
        co2_bits += '0'
    
    if len(co2) > 1:
        for line in co2[:]:
            if co2_bits[i] != line[i]: co2.remove(line)

print(o2, co2)
print(bin2dec(o2[0]) * bin2dec(co2[0]))
