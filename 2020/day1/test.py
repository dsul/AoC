import unittest
from main import two_sums_product, three_sums_product, SUM

class TestSumsProduct(unittest.TestCase):
    def test_two_sums_product(self):
        target_entry1 = 120
        target_entry2 = SUM - target_entry1
        test_input = [1303, 1000, target_entry1, 3, target_entry2]
        product = two_sums_product(test_input)
        self.assertEqual(product, target_entry1 * target_entry2)

    def test_three_sums_product(self):
        target_entry1 = 120
        target_entry2 = SUM - target_entry1 - (target_entry1 * 2)
        target_entry3 = SUM - target_entry2 - target_entry1
        test_input = [target_entry1, 1303, 1000, target_entry2, 3, target_entry3]
        product = three_sums_product(test_input)
        self.assertEqual(product, target_entry1 * target_entry2 * target_entry3)

    # Edge case test to ensure an element is not used twice when
    # finding the 3 target elements
    def test_three_sums_product_with_two_elements(self):
        target_entry1 = SUM // 4
        target_entry2 = SUM // 2
        test_input = [15, target_entry1, target_entry2, 10]
        product = three_sums_product(test_input)
        self.assertEqual(product, None)

if __name__ == '__main__':
    unittest.main()
