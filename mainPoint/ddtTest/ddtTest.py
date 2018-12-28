#coding=utf-8
import unittest
from ddt import ddt, data, file_data, unpack

@ddt
class DDTTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
    @classmethod
    def tearDownClass(self):
        pass
    def setUp(self):
        pass
    def tearDown(self):
        pass

    @data(3)
    def test_one(self, value):
        self.assertEqual(value, 3)

    @data('ascii', 'string')
    def test_two(self, value):
        self.assertIn(value, ['ascii', 'string'])

    @data([3, 2], [4, 3], [5, 3])
    @unpack
    def test_three(self, first, second):
        self.assertTrue(first > second)

    @data({'first': 1, 'second': 3, 'third': 2}, {'first': 4, 'second': 6, 'third': 5})
    @unpack
    def test_four(self, first, second, third):
        self.assertTrue(first < third < second)

    @file_data('test_data_list.json')
    def test_five(self, value):
        self.assertTrue(isinstance(value, str))

    @file_data('test_data_dict.json')
    def test_six(self, value):
        self.assertEqual(len(value), 3)

    @file_data('test_data_list.yaml')
    def test_seven(self, value):
        self.assertTrue(isinstance(value, str))

    @file_data('test_data_dict.yaml')
    def test_six(self, value):
        self.assertEqual(len(value), 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)


