import unittest

#function to find the factorial of a positive integer
def factorial(num):
    fact = 1
    if num > 0 and isinstance(num, int):
        for n in range(1, num + 1):
            fact *= n
        return fact
    elif num == 0 and isinstance(num, int):
        return fact 
    else:
        return "Input error! Please enter number greater than 0"

#test answer
class is_a_factorial(unittest.TestCase):
    def testNegative(self): 
        self.assertEqual(factorial(-3), "Input error! Please enter number greater than 0")

    def testNonNumber(self):
        self.assertEqual(factorial("%"), "Input error! Please enter number greater than 0")

    def testRandomNumber(self):
        self.assertEqual(factorial(5), 120)


if __name__ == "__main__":
    unittest.main()
