from typing import Dict, List
from queue import Queue
import re

TARGET_COLOR = 'shiny gold'

def create_bags_dict(data: List[str]) -> Dict:
    bags = {}
    for line in data:
        line = line.replace(' contain', ',')
        l = re.split(', ', line)
        outer_bag = ' '.join(l[0].strip().split()[:2])
        bags[outer_bag] = []
        for inner_bag in l[1:]:
            if inner_bag == 'no other bags.':
                continue
            inner_bag_count = int(inner_bag[0])
            inner_bag_name = ' '.join(inner_bag.strip().split()[1:3])
            bags[outer_bag].append((inner_bag_name, inner_bag_count))

    return bags

def contains_shiny_gold_count(data: List[str], bags: Dict) -> None:
    print(bags)
    q = Queue(maxsize = 0)
    q.put(TARGET_COLOR)
    seen = set()
    while not q.empty():
        color = q.get()
        if color in seen:
            continue
        seen.add(color)
        for k in bags:
            if color in list(map(lambda x: x[0], bags[k])):
                q.put(k)

    print(len(seen) - 1)

def within_shiny_gold_count(data: List[str], bags: Dict) -> None:
    initial_multiplier = 1
    result = 0
    q = Queue(maxsize = 0)
    q.put((TARGET_COLOR, initial_multiplier))
    while not q.empty():
        color, multiplier = q.get()
        if color in bags:
            for inner in bags[color]:
                next_color, count = inner
                result += count * multiplier
                q.put((next_color, count * multiplier))

    print(result)

def parse_input_file() -> List[int]:
   file = open('./input.txt', 'r')
   return [entry for entry in file.read().splitlines()]

def main():
    data = parse_input_file()
    bags = create_bags_dict(data)
    contains_shiny_gold_count(data, bags)
    within_shiny_gold_count(data, bags)

if __name__ == '__main__':
    main()
