import unittest
from math_quiz import generate_rand_int, generate_rand_operator, generate_math_problem


class TestMathGame(unittest.TestCase):

    def test_generate_rand_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_rand_operator(self):
        # Test if the operator is eitehr '+', '-' or '*'
        valid_operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of function calls
            operator = generate_rand_operator()
            self.assertIn(operator, valid_operators)

    def test_generate_math_problem(self):
        # Define test cases in the format (num1, num2, operator, expected_problem, expected_answer)
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (7, 3, '-', '7 - 3', 4),
            (4, 6, '*', '4 * 6', 24),
            (9, 5, '+', '9 + 5', 14),
            (10, 10, '-', '10 - 10', 0),
            (8, 3, '*', '8 * 3', 24)
        ]

        for num1, num2, operator, correct_problem, correct_answer in test_cases:
            # Generate the problem and answer
            problem, answer = generate_math_problem(num1, num2, operator)
            # Check if the generated problem and answer match the correct results
            self.assertEqual(problem, correct_problem)
            self.assertEqual(answer, correct_answer)

if __name__ == "__main__":
    unittest.main()
