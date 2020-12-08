import unittest
from main import valid_password_count, valid_password_count2

class ValidPasswordCountTest(unittest.TestCase):
    def test_valid_password_count(self):
        valid_passwords = [
          '14-20 b: bbbbbbbbbbbbzwbbbbbb',
          '5-6 t: tttttt',
          '2-6 s: sjsssss'
        ]
        test_input = [
          '4-13 b: mdbctbzgcpdjbhsdctrd',
          '7-9 h: zbhhfmwhhpx',
        ]
        test_input.extend(valid_passwords)

        valid_count = valid_password_count(test_input)
        self.assertEqual(len(valid_passwords), valid_count)

    def test_valid_password_count2(self):
        valid_passwords = [
          '4-13 b: mdbctbzgcpdjbhsdctrd',
          '6-8 h: zbhhfmwhhpx'
        ]
        test_input = [
          '14-20 b: bbbbbbbbbbbbzbbbbbbb',
          '2-6 s: sssjsss',
          '4-13 b: mdbbtbzgcpdjbhsdctrd',
          '5-6 t: ttttrs'
        ]
        test_input.extend(valid_passwords)

        valid_count = valid_password_count2(test_input)
        self.assertEqual(len(valid_passwords), valid_count)

if __name__ == '__main__':
    unittest.main()
