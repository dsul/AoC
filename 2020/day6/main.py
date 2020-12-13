from typing import List

def yes_count(data: List[str]) -> None:
    # Part 1
    print(sum(len(set.union(*map(set, group.split('\n')))) for group in data))

    # Part 2
    print(sum(len(set.intersection(*map(set, group.split('\n')))) for group in data))


def parse_input_file() -> List[int]:
   file = open('./input.txt', 'r')
   return [entry.rstrip() for entry in file.read().split('\n\n')]

def main():
    data = parse_input_file()
    yes_count(data)

if __name__ == '__main__':
    main()
