from typing import List

SUM = 2020

def parse_input_file() -> List[int]:
   file = open('./input.txt', 'r')
   return [int(entry) for entry in file.read().split()]

def two_sums_product(entries: List[int]) -> int:
    visited = set()
    for entry in entries:
        visited.add(entry)
        complement = SUM - entry
        if complement in visited:
            return complement * entry

def three_sums_product(entries: List[int]) -> int:
    arr_length = len(entries)
    for i in range(0, arr_length):
        visited = set()
        current_sum = SUM - entries[i]
        for j in range(i + 1, arr_length):
            if (current_sum - entries[j]) in visited:
                return entries[i] * entries[j] * (current_sum - entries[j])
            visited.add(entries[j])

def main():
    entries = parse_input_file()
    print(f'two_sums_product {two_sums_product(entries)}')
    print(f'three_sums_product {three_sums_product(entries)}')

if __name__ == '__main__':
    main()
