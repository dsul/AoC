from typing import List, Tuple
import re

EYE_COLORS = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

FIELD_VALIDATIONS = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: (x.endswith('cm') and 150 <= int(x[:-2]) <= 193) or
                     (x.endswith('in') and 59 <= int(x[:-2]) <= 76),
    'hcl': lambda x: re.fullmatch(r'#[0-9a-f]{6}', x),
    'ecl': lambda x: x in EYE_COLORS,
    'pid': lambda x: re.fullmatch(r'\d{9}', x)
}

def parse_input_file() -> List[int]:
   file = open('./input.txt', 'r')
   return [entry for entry in file.read().split('\n\n')]

def valid_passport_count(data: List[str]) -> Tuple[int, int]:
    present_count = 0
    valid_count = 0
    for line in data:
        passport = dict(field.split(':') for field in line.split())
        if passport.keys() >= FIELD_VALIDATIONS.keys():
            present_count += 1
            valid_count += all(validation(passport[field]) for field, validation in FIELD_VALIDATIONS.items())

    return (present_count, valid_count)

def main():
    data = parse_input_file()
    print(f'valid_passport_count: {valid_passport_count(data)}')

if __name__ == '__main__':
    main()
