import unittest
from src.quadratic_equation import QuadraticEquation


class QuadraticEquationTestCase(unittest.TestCase):
    def test_raise_error_when_a_is_zero(self):
        # arrange
        a, b, c = 0, 2, 4

        # act & assert
        self.assertRaises(ValueError, QuadraticEquation, a, b, c)

    def test_two_solutions(self):
        # arrange
        a, b, c = 1, -5, 6

        # act & assert
        equation = QuadraticEquation(a, b, c)
        result = equation.solve()

        self.assertAlmostEqual(result[0], 3.0)
        self.assertAlmostEqual(result[1], 2.0)

    def test_one_solution(self):
        # arrange
        a, b, c = 1, 4, 4

        # act & assert
        equation = QuadraticEquation(a, b, c)
        result = equation.solve()
        
        self.assertAlmostEqual(result[0], -2.0)

    def test_no_solutions(self):
        # arrange
        a, b, c = 1, 1, 1

        # act & assert
        equation = QuadraticEquation(a, b, c)
        self.assertIsNone(equation.solve())

if __name__ == '__main__':
    unittest.main()
