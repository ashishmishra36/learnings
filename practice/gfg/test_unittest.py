import unittest
import lambda_utility

# it inherits the base class
class TestUnitTest(unittest.TestCase):

    def test_positive(self):
        length = lambda_utility.count_vowel('ashish')
        assert length== 2, f'correct number of vowels is {length}!'

    def test_negative(self):
        length = lambda_utility.count_vowel('mishra')
        assert length==2 ,'Error ! '


if __name__ == '__main__':
    unittest.main()

