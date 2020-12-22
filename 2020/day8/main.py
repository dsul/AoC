from typing import List, Set
import re

def part1(data: List[str]) -> None:
    accumulator = 0
    current_code_index = 0
    visited = set()
    while current_code_index not in visited:
        visited.add(current_code_index)
        (code, arg) = re.match(r'^(.+) ([\+|-]\d+)$', data[current_code_index]).groups()
        if code == 'acc':
            accumulator += int(arg)
        if code == 'jmp':
            current_code_index += int(arg) - 1
        current_code_index += 1

    return accumulator

def part2(
    data: List[str],
    index: int = 0,
    accumulator: int = 0,
    visited: Set = set(),
    foundError: bool = False
 ) -> int:
    if index == len(data): return accumulator
    if index in visited: return -1

    new_visited = visited.copy()
    new_visited.add(index)
    (code, arg) = re.match(r'^(.+) ([\+|-]\d+)$', data[index]).groups()
    if code == 'acc':
        return part2(data, index + 1, accumulator + int(arg), new_visited, foundError)
    if code == 'jmp':
        return max(
            part2(data, index + int(arg), accumulator, new_visited, foundError),
            -1 if foundError else part2(data, index + 1, accumulator, new_visited, True)
        )
    if code == 'nop':
        return max(
            -1 if foundError else part2(data, index + int(arg), accumulator, new_visited, True),
            part2(data, index + 1, accumulator, new_visited, foundError)
        )

def parse_input_file() -> List[int]:
   file = open('./input.txt', 'r')
   return [entry for entry in file.read().splitlines()]

def main():
    data = parse_input_file()
    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()
