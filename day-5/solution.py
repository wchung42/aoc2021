# aoc2021005.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    return [tuple(map(int, pair.strip().split(','))) for line in puzzle_input.split('\n') for pair in line.split('->')]

def print_field(field):
    for i in range(len(field)):
        for j in range(len(field)):
            print(field[j][i], end='')
        print()

def part1(numbers):
    """Solve part 1"""
    # find max x and max y
    maxx, maxy = 0, 0
    for pair in numbers:
        if pair[0] > maxx:
            maxx = pair[0]
        if pair[1] > maxy:
            maxy = pair[1]
    
    # make board
    field = []
    for r in range(maxx+1):
        field.append([])
        for _ in range(maxy+1):
            field[r].append(0)
            
    for i in range(0, len(numbers)-1, 2):
        p1 = numbers[i]
        p2 = numbers[i+1]
        if p1[0] == p2[0] or p1[1] == p2[1]:
            print(p1, '->', p2)
            distx = abs(p2[0] - p1[0])
            disty = abs(p2[1] - p1[1])
            print(distx, disty)
            
            if distx != 0:
                startx = min(p1[0], p2[0])
                for x in range(startx, startx + distx+1):
                    field[x][p1[1]] += 1

            if disty != 0:
                starty = min(p1[1], p2[1])
                for y in range(starty, starty + disty+1):
                    field[p1[0]][y] += 1

    print_field(field) 

    total = 0
    for row in field:
        for col in row:
            if col >= 2:
                total += 1

    return total

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()

        numbers = parse(puzzle_input)

        print(part1(numbers))