import re
from typing import List

PASSWORD_LIST_REGEX = r"\A(\d+)-(\d+)\s(.):\s(.+$)"

def parse_input_file() -> List[int]:
   file = open('./input.txt', 'r')
   return [entry for entry in file.read().splitlines()]

def valid_password_count(data: List[str]) -> int:
    valid_count = 0
    for line in data:
        (min, max, letter, password) = re.search(PASSWORD_LIST_REGEX, line).groups()
        if int(min) <= password.count(letter) <= int(max):
            valid_count += 1

    return valid_count

def valid_password_count2(data: List[str]) -> int:
    valid_count = 0
    for line in data:
        (pos1, pos2, letter, password) = re.search(PASSWORD_LIST_REGEX, line).groups()
        first_position_match = password[int(pos1) - 1] == letter
        second_position_match = password[int(pos2) - 1] == letter
        if first_position_match ^ second_position_match:
            valid_count += 1

    return valid_count

def main():
    data = parse_input_file()
    print(f'valid_password_count: {valid_password_count(data)}')
    print(f'valid_password_count2: {valid_password_count2(data)}')

if __name__ == '__main__':
    main()
