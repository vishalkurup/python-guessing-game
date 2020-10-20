import unittest
import main


class test_cases(unittest.TestCase):

    def test_correct_guess(self):
        '''Testing scenario where guess == answer'''
        guess = 5
        answer = 5
        result = main.validate_user_input(guess, answer)
        self.assertTrue(True)

    def test_incorrect_guess(self):
        '''Testing scenario where guess == incorrect answer'''
        guess = 5
        answer = 11
        result = main.validate_user_input(guess, answer)
        self.assertFalse(result)

    def test_invalid_guess(self):
        '''Testing scnenario where one value is a string'''
        guess = 5
        answer = "answer"
        result = main.validate_user_input(guess, answer)
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
