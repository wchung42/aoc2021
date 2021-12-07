def main():
    depth = 0
    horizontal_pos = 0
    aim = 0

    with open('input.txt', 'r') as data:
        
        lines = [line.strip('\n') for line in data.readlines()]
        for line in lines:
            units = int(line[-1])
            if line.startswith('forward'):
                horizontal_pos += units # add to horizontal_pos
                depth += aim * units
            elif line.startswith('down'):
                aim += units
            elif line.startswith('up'):
                aim -= units

    print(f'Depth: {depth}')
    print(f'Horizontal Position: {horizontal_pos}')
    print(depth*horizontal_pos)

if __name__ == '__main__':
    main()