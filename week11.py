import unittest

class SimpleTests(unittest.TestCase):

    def test_case_one(self):
        print("✅ Test Case One: Hello from unittest!")
        self.assertTrue(True)

    def test_case_two(self):
        a = 5
        b = 7
        sum_result = a + b
        print("✅ Test Case Two: Sum = ", sum_result)
        self.assertEqual(sum_result, 12)

# ✅ Run test suite
if __name__ == '__main__':
    unittest.main()
    input("\n✅ Press Enter to exit...")
