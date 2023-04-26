import sum_fraction as sf
import unittest

class MyTestCase(unittest.TestCase):
    def test_1(self):
        answer = sf.sum_fraction(1,2,1,2)
        self.assertEqual(answer, [1,1])
    
    def test_2(self):
        answer = sf.sum_fraction(9,2,1,3)
        self.assertEqual(answer, [29,6])

    def test_3(self):
        answer = sf.sum_fraction(2,6,1,6)
        self.assertEqual(answer, [1,2])

if __name__ == "__main__":
    unittest.main()