import unittest

from PowerfulNumber import cubPrim


class TestCubPrim(unittest.TestCase):
    def test_good_case(self):
        """
        Test in a good case
        """
        number = 27
        result = cubPrim(number)
        self.assertEqual(result, True)

    def test_bad_case(self):
        """
        Test in a bad case
        """
        number = 28
        result = cubPrim(number)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()