# aoc2021008.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    return [pattern.split(' | ')[1] for pattern in puzzle_input.split('\n')]


def part1(patterns):
    """Solve part 1"""
    count = 0
    for pattern in patterns:
        count += len([digit for digit in pattern.split(' ') if len(digit) in [2, 3, 4, 7]])
    
    return count


def part2(numbers):
    """Solve part 2"""
    fuel_needed = [max(numbers)+1 for _ in range(max(numbers))]
    
    for i in range(len(fuel_needed)):
        fuel_consum = 0
        for num in numbers:
            steps = abs(num - i)
            fuel_consum += steps * (1 + steps) / 2
            #print(num, '->', i, '|', fuel_consum)
        fuel_needed[i] = fuel_consum

    #print(fuel_needed)
    least_fuel = min(fuel_needed)
    return least_fuel


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()

        patterns = parse(puzzle_input)

        print('Part 1:', part1(patterns))
        # print('Part 2:', part2(numbers))