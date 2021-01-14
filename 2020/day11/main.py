from typing import List

def part1(data: List[int]) -> int:
    arr_length = len(data)
    row_length = len(data[0])
    new_data = []
    for i, entry in enumerate(data):
        new_data_entry = []
        for j, c in enumerate(entry):
            adjacent_count = 0
            if c == 'L' or c == '#':
                # Check above
                if i > 0:
                    adjacent_count += data[i-1][max(j-1, 0): min(j+2, row_length)].count('#')
                # Check below
                if i < arr_length - 1:
                    adjacent_count += data[i+1][max(j-1, 0): min(j+2, row_length)].count('#')
                # Check left
                if j > 0:
                    adjacent_count += data[i][j-1] == '#'
                # Check right
                if j < row_length - 1:
                    adjacent_count += data[i][j+1] == '#'


                if adjacent_count == 0:
                    new_data_entry.append('#')
                elif adjacent_count >= 4:
                    new_data_entry.append('L')
                else:
                    new_data_entry.append(data[i][j])

            else:
                new_data_entry.append('.')

        new_data.append(new_data_entry)

    if new_data == data:
        return sum([c.count('#') for c in new_data])

    return part1(new_data)

def part2(data: List[int], index = 0) -> int:
    arr_length = len(data)
    row_length = len(data[0])
    new_data = []
    for i, entry in enumerate(data):
        new_data_entry = []
        for j, char in enumerate(entry):
            adjacent_count = 0
            if char == 'L' or char == '#':
                # Check north
                if i > 0:
                    k = i
                    while k > 0 and data[k-1][j] != 'L':
                        if data[k-1][j] == '#':
                            adjacent_count += 1
                            break
                        k -= 1

                # Check south
                if i < arr_length - 1:
                    k = i
                    while k < arr_length - 1 and data[k+1][j] != 'L':
                        if data[k+1][j] == '#':
                            adjacent_count += 1
                            break
                        k += 1

                # Check east
                if j < row_length - 1:
                    k = j
                    while k < row_length - 1 and data[i][k+1] != 'L':
                        if data[i][k+1] == '#':
                            adjacent_count += 1
                            break
                        k += 1

                # Check west
                if j > 0:
                    k = j
                    while k > 0 and data[i][k-1] != 'L':
                        if data[i][k-1] == '#':
                            adjacent_count += 1
                            break
                        k -= 1

                # Check north-west
                if j > 0 and i > 0:
                    k = j
                    l = i
                    while k > 0 and l > 0 and data[l-1][k-1] != 'L':
                        if data[l-1][k-1] == '#':
                            adjacent_count += 1
                            break
                        k -= 1
                        l -= 1

                # Check north-east
                if j < row_length - 1 and i > 0:
                    k = j
                    l = i
                    while k < row_length - 1 and l > 0 and data[l-1][k+1] != 'L':
                        if data[l-1][k+1] == '#':
                            adjacent_count += 1
                            break
                        k += 1
                        l -= 1

                # Check south-west
                if j > 0 and i < arr_length - 1:
                    k = j
                    l = i
                    while k > 0 and l < arr_length - 1 and data[l+1][k-1] != 'L':
                        if data[l+1][k-1] == '#':
                            adjacent_count += 1
                            break
                        k -= 1
                        l += 1

                # Check south-east
                if j < row_length - 1 and i < arr_length - 1:
                    k = j
                    l = i
                    while k < row_length - 1 and l < arr_length - 1 and data[l+1][k+1] != 'L':
                        if data[l+1][k+1] == '#':
                            adjacent_count += 1
                            break
                        k += 1
                        l += 1

                if adjacent_count == 0:
                    new_data_entry.append('#')
                elif adjacent_count >= 5:
                    new_data_entry.append('L')
                else:
                    new_data_entry.append(data[i][j])

            if char == '.':
                new_data_entry.append('.')
        new_data.append(new_data_entry)

    if new_data == data:
        return sum([c.count('#') for c in new_data])

    return part2(new_data)

def parse_input_file() -> List[int]:
   file = open('./input.txt', 'r')
   return [[c for c in entry] for entry in file.read().splitlines()]

def main():
    data = parse_input_file()
    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()
