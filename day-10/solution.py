# aoc2021008.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split('\n')]


def part1(lines):
    """Solve part 1"""
    corrupt_count = {')': 0, ']': 0, '}': 0, '>': 0}
    
    for line in lines:
        openings = []
        for symbol in line:
            if symbol in '([{<':
                openings.append('([{<'.index(symbol))
            else:
                if ')]}>'.index(symbol) != openings.pop():
                    corrupt_count[symbol] += 1

    total = 0
    for key, val in corrupt_count.items():
        if key == ')':
            total += val * 3
        elif key == ']':
            total += val * 57
        elif key == '}':
            total += val * 1197
        else:
            total += val * 25137
    
    return total

def part2(lines):
    """Solve part 2"""
    scores = []

    for line in lines:
        corrupt = False
        openings = []

        for symbol in line:
            if symbol in '([{<':
                openings.append('([{<'.index(symbol))
            else:
                temp = openings.pop()
                if ')]}>'.index(symbol) != temp:
                    corrupt = True
                    break
        
        if corrupt:
            continue
            
        missing_symbols = ''
        for opener in openings:
            missing_symbols += ')]}>'[opener]
        missing_symbols = missing_symbols[::-1]

        score = 0
        for i in range(len(missing_symbols)):
            symbol = missing_symbols[i]
            score *= 5
            if symbol == ')':
                score += 1
            elif symbol == ']':
                score += 2
            elif symbol == '}':
                score += 3
            else:
                score += 4
        scores.append(score)
    
    scores.sort()
    
    return scores[(len(scores) - 1) // 2]

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()

        lines = parse(puzzle_input)

        print('Part 1:', part1(lines))
        print('Part 2:', part2(lines))