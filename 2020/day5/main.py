from typing import List

CHAR_TO_BINARY_MAP = {
    'F': '0',
    'B': '1',
    'L': '0',
    'R': '1'
}

def seat_ids(data: List[str]) -> None:
    seat_ids = set()
    for boarding_pass in data:
        seat_ids.add(int(''.join([CHAR_TO_BINARY_MAP[char] for char in boarding_pass]), 2))
    highest_seat_id = max(seat_ids)
    for i in range(0, 2**10):
        if i not in seat_ids and i + 1 in seat_ids and i - 1 in seat_ids:
            print(i)
            break

    print(highest_seat_id)

def parse_input_file() -> List[int]:
   file = open('./input.txt', 'r')
   return [entry for entry in file.read().splitlines()]

def main():
    data = parse_input_file()
    seat_ids(data)

if __name__ == '__main__':
    main()
