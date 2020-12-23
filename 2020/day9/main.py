from typing import List

def part1(data: List[int], preamble_count: int) -> int:
    for i in range(preamble_count, len(data)):
        found = False
        preamble = data[i - preamble_count: i]
        for j in range(0, preamble_count - 1):
            for k in range(j + 1, preamble_count):
                if preamble[j] + preamble[k] == data[i]:
                    found = True
                    break
                if found == True:
                    break
            if found == True:
                break
        if found == True:
            continue

        return data[i]


def part2(data: List[int]) -> int:
    target = 3199139634
    p1 = 0
    p2 = 1
    while p1 < len(data) - 1:
        group = data[p1:p2]
        group_sum = sum(group)
        if group_sum == target:
            return max(group) + min(group)
        if group_sum < target:
            p2 += 1
        else:
            p1 += 1

def parse_input_file() -> List[int]:
   file = open('./input.txt', 'r')
   return [int(entry) for entry in file.read().splitlines()]

def main():
    data = parse_input_file()
    print(part1(data, 25))
    print(part2(data))

if __name__ == '__main__':
    main()
