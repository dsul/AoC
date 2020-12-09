import unittest
from main import trees_encountered

class ValidPasswordCountTest(unittest.TestCase):
    def test_trees_encountered(self):
        slope = (3, 1)
        test_input = [
          '..........',
          '...#......',
          '..........',
          '.........#',
          '..#.......'
        ]
        actual_tree_count = 3

        tree_count = trees_encountered(test_input, slope)
        self.assertEqual(actual_tree_count, tree_count)

    def test_trees_encountered2(self):
        slope = (3, 2)
        test_input = [
          '..........',
          '..........',
          '...#......',
          '..........',
          '......#...'
        ]
        actual_tree_count = 2

        tree_count = trees_encountered(test_input, slope)
        self.assertEqual(actual_tree_count, tree_count)

if __name__ == '__main__':
    unittest.main()
