# aoc2021007.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    return [int(num) for num in puzzle_input.split(',')]


def part1(numbers):
    """Solve part 2"""
    fuel_needed = [max(numbers)+1 for _ in range(max(numbers))]
    
    for i in range(len(fuel_needed)):
        fuel_consum = 0
        for num in numbers:
            fuel_consum += abs(num - i)
        fuel_needed[i] = fuel_consum

    least_fuel = min(fuel_needed)
    return least_fuel


def part2(numbers):
    """Solve part 1"""
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

        numbers = parse(puzzle_input)

        print('Part 1:', part1(numbers))
        print('Part 2:', part2(numbers))