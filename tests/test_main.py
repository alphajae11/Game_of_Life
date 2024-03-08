import unittest

from game_of_life.main import read_input, get_next_generation, count_neighbors, print_generation

class TestMain(unittest.TestCase):
    def test_read_input1(self):
        input_analysed = read_input("input/seed1.txt")
        expected_output = [[1]]
        self.assertEquals(input_analysed, expected_output)

    def test_read_input2(self):
        input_analysed = read_input("input/seed2.txt")
        expected_output = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 0, 0], [0, 1, 0, 0]]
        self.assertEquals(input_analysed, expected_output)

    # def

    def test_count_neighbors1(self):
        grid = [[1]]
        self.assertEqual(count_neighbors(grid, 0, 0), 0)

    def test_count_neighbors2(self):
        grid = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 0, 0], [0, 1, 0, 0]]
        self.assertEqual(count_neighbors(grid, 1, 1), 3)
        self.assertEqual(count_neighbors(grid, 0, 2), 2)
        self.assertEqual(count_neighbors(grid, 2, 1), 3)
        self.assertEqual(count_neighbors(grid, 3, 1), 2)

    def test_get_next_generation1(self):
        current_generation = [[1]]
        expected_next_generation = [[0]]
        actual_next_generation = get_next_generation(current_generation)
        self.assertEquals(actual_next_generation, expected_next_generation)

    def test_get_next_generation2(self):
        current_generation = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 0, 0], [0, 1, 0, 0]]
        expected_next_generation = [[0, 0, 1, 0], [1, 1, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0]]
        actual_next_generation = get_next_generation(current_generation)
        self.assertEquals(actual_next_generation, expected_next_generation)