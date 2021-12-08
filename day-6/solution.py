# aoc2021006.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    return [int(num) for num in puzzle_input.split(',')]

def part1(numbers):
    """Solve part 1"""
    school = [num for num in numbers]
    for i in range(80):
        for j in range(len(school)):
            if school[j] == 0:
                school[j] = 6
                school.append(8)
            else:
                school[j] -= 1
        # print(f'After {i} days: {school}')
    return len(school)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()

        numbers = parse(puzzle_input)

        print(part1(numbers))