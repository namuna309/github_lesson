import unittest
import hex_dig
class averageTestCase(unittest.TestCase):
 def test_average(self):
    answer = hex_dig(123456)
    self.assertEqual(answer, 3.0)
 
 def test_empty_input_average(self):
    answer = hex_dig([])
    self.assertEqual(answer, None)
    if __name__ == "__main__":
        unittest.main()