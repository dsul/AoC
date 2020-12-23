from typing import List

def part1(data: List[int]) -> int:
    one_volt_differences = 0
    three_volt_differences = 0
    for i in range(0, len(data) - 1):
        difference = data[i + 1] - data[i]
        one_volt_differences += difference == 1
        three_volt_differences += difference == 3

    return one_volt_differences * three_volt_differences

visited = {}
def part2(data: List[int], index = 0) -> int:
    if index == len(data) - 1:
       return 1
    if index in visited:
        return visited[index]
    result = 0
    for i in range(index + 1, len(data)):
        if i - index > 3:
            break
        if data[i] - data[index] <= 3:
            result += part2(data, i)
            visited[index] = result
    return result

def parse_input_file() -> List[int]:
   file = open('./input.txt', 'r')
   return [int(entry) for entry in file.read().splitlines()]

def main():
    data = parse_input_file()
    data.append(0)
    data.append(max(data) + 3)
    data.sort()
    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()
