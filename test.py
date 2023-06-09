import unittest


class NumbersTest(unittest.TestCase):
    @unittest.expectedFailure
    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

    def test(self):
        self.assertEqual(1, 1)


unittest.main()
