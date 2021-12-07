'''Day 3: Binary Diagnostic'''

# Binary to Decimal
def bin2dec(bin):
    '''Converts binary number to decimal number; Returns decimal'''
    result = 0
    
    for i in range(len(bin)):
        result += int(bin[-(i+1)]) * (2**i)

    return result

# Calculate gamma rate (most common bits)

# Calculate epsilon rate (least common bits)

with open('input.txt', 'r') as data:
    report = data.readlines()

gamma = ''
epsilon = ''

for i in range(len(report[0])-1):
    ones = 0
    zeros = 0

    for line in report:
        if line[i] == '1':
            ones += 1
        else:
            zeros += 1

    if ones > zeros:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(gamma, epsilon)
print(bin2dec(gamma) * bin2dec(epsilon))