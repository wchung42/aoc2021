def main():
    depth = 0
    horizontal_pos = 0

    with open('input.txt', 'r') as data:
        
        lines = [line.strip('\n') for line in data.readlines()]
        for line in lines:
            if line.startswith('forward'):
                horizontal_pos += int(line[-1])
            elif line.startswith('down'):
                depth += int(line[-1])
            elif line.startswith('up'):
                depth -= int(line[-1])

    print(f'Depth: {depth}')
    print(f'Horizontal Position: {horizontal_pos}')
    print(depth*horizontal_pos)

if __name__ == '__main__':
    main()