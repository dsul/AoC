from typing import List
from functools import reduce

TREE = '#'

def parse_input_file() -> List[int]:
   file = open('./input.txt', 'r')
   return [entry for entry in file.read().splitlines()]

def trees_encountered(data: List[str], slope: tuple) -> int:
    (right, down) = slope
    trees = 0
    row_index = right
    column_index = down
    row_length = len(data[0])
    while column_index < len(data):
        trees += data[column_index][row_index % row_length] == TREE
        row_index += right
        column_index += down

    return trees

def main():
    data = parse_input_file()
    print(f'trees_encountered: {trees_encountered(data, (3, 1))}')
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    counts = [trees_encountered(data, slope) for slope in slopes]
    print(f'trees_encountered2: {reduce(lambda x, y: x * y, counts)}')

if __name__ == '__main__':
    main()
