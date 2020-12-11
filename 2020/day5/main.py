from typing import List

CHAR_TO_BINARY_MAP = {
    'F': '0',
    'B': '1',
    'L': '0',
    'R': '1'
}

def seat_ids(data: List[str]) -> None:
    seat_ids = []
    for boarding_pass in data:
        seat_ids.append(int(''.join([CHAR_TO_BINARY_MAP[char] for char in boarding_pass]), 2))
    seat_ids.sort()
    highest_seat_id = seat_ids[-1]
    missing_seat_id = None
    for sid in range(seat_ids[0], seat_ids[-1] - 1):
        if (
                sid not in seat_ids
                and sid + 1 in seat_ids
                and sid - 1 in seat_ids
            ):
            missing_seat_id = sid

    print(highest_seat_id)
    print(missing_seat_id)

def parse_input_file() -> List[int]:
   file = open('./input.txt', 'r')
   return [entry for entry in file.read().splitlines()]

def main():
    data = parse_input_file()
    seat_ids(data)

if __name__ == '__main__':
    main()
