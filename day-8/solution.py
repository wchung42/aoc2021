# aoc2021008.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    return [pattern for pattern in puzzle_input.split('\n')]


def part1(patterns):
    """Solve part 1"""
    patterns = [pattern.split(' | ')[1] for pattern in patterns]
    count = 0
    for pattern in patterns:
        count += len([digit for digit in pattern.split(' ') if len(digit) in [2, 3, 4, 7]])
    
    return count


def part2(patterns):
    """Solve part 2"""
    total = 0

    for line in patterns:
        signal_patterns = [chunk for chunk in line.split(' | ')[0].split(' ')]
        outputs = [chunk for chunk in line.split(' | ')[1].split(' ')]

        combos = [None for _ in range(10)]
        while None in combos:
            for i in range(len(signal_patterns)):
                if len(signal_patterns[i]) == 2:
                    combos[1] = set(signal_patterns[i])
                elif len(signal_patterns[i]) == 3:
                    combos[7] = set(signal_patterns[i])
                elif len(signal_patterns[i]) == 4:
                    combos[4] = set(signal_patterns[i])
                elif len(signal_patterns[i]) == 7:
                    combos[8] = set(signal_patterns[i])
                elif len(signal_patterns[i]) == 6:
                    if combos[4] is not None and combos[4].issubset(signal_patterns[i]): # 9
                        combos[9] = set(signal_patterns[i])
                    elif combos[7] is not None and combos[7].issubset(signal_patterns[i]):
                        combos[0] = set(signal_patterns[i])
                    elif combos[4] is not None and combos[7] is not None:
                        combos[6] = set(signal_patterns[i]) # 6
                elif len(signal_patterns[i]) == 5:
                    if combos[7] is not None and combos[7].issubset(signal_patterns[i]):
                        combos[3] = set(signal_patterns[i]) # 3
                    elif combos[6] is not None and set(signal_patterns[i]).issubset(combos[6]):
                        combos[5] = set(signal_patterns[i])
                    else:
                        combos[2] = set(signal_patterns[i])
        
        result = ''
        for output in outputs:
            for chunk in output.split(' '):
                result += str(combos.index(set(chunk)))
            
        total += int(result)
    
    return total

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()

        patterns = parse(puzzle_input)

        print('Part 1:', part1(patterns))
        print('Part 2:', part2(patterns))