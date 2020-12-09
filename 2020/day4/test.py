import unittest
from main import valid_passport_count

class ValidPassportsTest(unittest.TestCase):
    def test_valid_passports_count(self):
        test_input = [
          'pid:827837505 byr:1976 hgt:187cm iyr:2016 hcl:#fffffd eyr:2024',
          'hgt:189cm byr:1987 pid:572028668 iyr:2014 hcl:#623a2f eyr:2028 ecl:amb',
          'ecl:gry hgt:170mm iyr:2014 cid:285 pid:870052514 hcl:#866857 byr:1925 eyr:2025',
          'eyr:2021 byr:1960 pid:569950896 iyr:2010 hgt:179cm hcl:#888785 cid:167',
          'ecl:amb hcl:#602927 eyr:2029 pid:897535300 hgt:189cm byr:1952 iyr:2017'
        ]
        present_passports = 3
        valid_passports = 2

        present, valid = valid_passport_count(test_input)
        self.assertEqual(present, present_passports)
        self.assertEqual(valid, valid_passports)

if __name__ == '__main__':
    unittest.main()
