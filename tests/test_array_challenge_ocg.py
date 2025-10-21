import unittest
from advanced import array_challenge

class TestArrayChallenges(unittest.TestCase):
    def test_max_subarray_sum(self):
        self.assertEqual(array_challenge.max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]), 6)

    def test_remove_duplicates(self):
        nums = [1,1,2,2,3]
        length = array_challenge.remove_duplicates(nums)
        self.assertEqual(nums[:length], [1,2,3])
        self.assertEqual(length, 3)

    def test_move_zeros(self):
        nums = [0,1,0,3,12]
        self.assertEqual(array_challenge.move_zeros(nums), [1,3,12,0,0])

    def test_find_missing_number(self):
        self.assertEqual(array_challenge.find_missing_number([3,0,1]), 2)

    def test_two_sum_pairs(self):
        pairs = array_challenge.two_sum_pairs([3, 1, 5, 2, 4], 6)
        self.assertIn((2,4), pairs)
        self.assertIn((1,5), pairs)

    def test_majority_element(self):
        self.assertEqual(array_challenge.majority_element([2,2,1,1,1,2,2]), 2)

    def test_rotate_array(self):
        nums = [1,2,3,4,5,6,7]
        self.assertEqual(array_challenge.rotate_array(nums, 3), [5,6,7,1,2,3,4])

    def test_intersection(self):
        self.assertEqual(array_challenge.intersection([1,2,2,1], [2,2]), [2])

    def test_longest_consecutive(self):
        self.assertEqual(array_challenge.longest_consecutive([100,4,200,1,3,2]), 4)

    def test_product_except_self(self):
        self.assertEqual(array_challenge.product_except_self([1,2,3,4]), [24,12,8,6])

    def test_first_duplicate(self):
        self.assertEqual(array_challenge.first_duplicate([2, 1, 3, 5, 3, 2]), 3)

    def test_single_number(self):
        self.assertEqual(array_challenge.single_number([4,1,2,1,2]), 4)

    def test_three_sum(self):
        result = array_challenge.three_sum([-1,0,1,2,-1,-4])
        self.assertIn([-1, -1, 2], result)
        self.assertIn([-1, 0, 1], result)

    def test_find_min_rotated(self):
        self.assertEqual(array_challenge.find_min_rotated([4,5,6,7,0,1,2]), 0)

    def test_spiral_order(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(array_challenge.spiral_order(matrix), [1,2,3,6,9,8,7,4,5])

    def test_min_window_subarray(self):
        arr = [1,2,2,3,1,2,1,3]
        target = [1,3,2]
        self.assertEqual(array_challenge.min_window_subarray(arr, target), [2,3,1])

    def test_equilibrium_index(self):
        self.assertEqual(array_challenge.equilibrium_index([1,3,5,2,2]), 2)

    def test_max_product(self):
        self.assertEqual(array_challenge.max_product([1,10,2,6,5,3]), 60)

    def test_length_of_lis(self):
        self.assertEqual(array_challenge.length_of_lis([10,9,2,5,3,7,101,18]), 4)

    def test_min_jumps(self):
        self.assertEqual(array_challenge.min_jumps([2,3,1,1,4]), 2)


if __name__ == '__main__':
    unittest.main()
