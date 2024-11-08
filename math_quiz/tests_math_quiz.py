import unittest
from math_quiz import generate_number, generate_operator, problem_answer


class TestMathGame(unittest.TestCase):

    def test_generate_number(self):
        # Test if random numbers generated are within the specified range.
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_operator(self):
        # Test if the operator is one of the allowed operators ('+', '-', '*').
        allowed_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of selections to ensure randomization
            operator = generate_operator()
            self.assertIn(operator, allowed_operators)

    def test_problem_answer(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (1, 1, '-', '1 - 1', 0),
                (9, 2, '-', '9 - 2', 7),
                (10, 6, '+', '10 + 6', 16),
                (10, 5, '*', '10 * 5', 50),
                #''' TODO add more test cases here '''
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                problem, answer = problem_answer(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
                pass

if __name__ == "__main__":
    unittest.main()
