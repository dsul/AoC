from typing import List
import re

degree_map = {
    90: 1,
    180: 2,
    270: 3
}

directions = ['N', 'E', 'S', 'W']

def get_new_direction(current_direction, action, degrees):
    index = directions.index(current_direction)
    increment_by = 0
    if action == 'R':
        increment_by += degree_map[degrees]
    else:
        increment_by += degree_map[abs(degrees - 360)]

    return directions[(index + increment_by) % len(directions)]


def part1(data: List[str]) -> int:
    direction_totals = {
        'N': 0,
        'E': 0,
        'S': 0,
        'W': 0
    }
    direction = 'E'
    for instruction in data:
        (action, value) = re.match(r'(^[\D])(\d+)', instruction).groups()
        if action == 'F':
            direction_totals[direction] += int(value)
        if action in ['N', 'E', 'S', 'W']:
            direction_totals[action] += int(value)
        if action in ['R', 'L']:
            direction = get_new_direction(direction, action, int(value))

    return abs(direction_totals['N'] - direction_totals['S']) + abs(direction_totals['E'] - direction_totals['W'])


def rotate_by_degrees(action, degrees, waypoint_position):
    clockwise_90_mapping = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'
    }

    clockwise_iterations = degree_map[degrees] if action == 'R' else degree_map[abs(degrees - 360) % 360]
    new_waypoint_position = waypoint_position.copy()
    for _ in range(clockwise_iterations):
        changed = False
        for direction, position in waypoint_position.items():
            if position != 0:
                temp_val = waypoint_position[direction]
                if not changed:
                    new_waypoint_position[direction] = 0
                    changed = True
                new_waypoint_position[clockwise_90_mapping[direction]] = temp_val
        waypoint_position = new_waypoint_position.copy()

    return new_waypoint_position


def part2(data: List[str]) -> int:
    direction_totals = {
        'N': 0,
        'E': 0,
        'S': 0,
        'W': 0
    }
    waypoint_position = {
        'N': 1,
        'E': 10,
        'S': 0,
        'W': 0
    }
    for instruction in data:
        (action, value) = re.match(r'(^[\D])(\d+)', instruction).groups()
        if action == 'F':
            for direction, position in waypoint_position.items():
                direction_totals[direction] += int(value) * position
        if action in ['N', 'E', 'S', 'W']:
            waypoint_position[action] += int(value)
        if action in ['R', 'L']:
            waypoint_position = rotate_by_degrees(action, int(value), waypoint_position)

    return abs(direction_totals['N'] - direction_totals['S']) + abs(direction_totals['E'] - direction_totals['W'])

def parse_input_file() -> List[str]:
   file = open('./input.txt', 'r')
   return [entry for entry in file.read().splitlines()]

def main():
    data = parse_input_file()
    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()
