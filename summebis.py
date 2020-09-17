import unittest

# Function summe_bis:
# Parameter: n
# Result: 1 + 2 + 3 + ... + n


def summe_bis(number):
    summe = 0
    for i in range(1, number + 1):
        summe = summe + i
    return summe


# Testcases
class TestSummeBis(unittest.TestCase):
    def test_summe_bis_1_is_1(self):
        self.assertEqual(summe_bis(1), 1)

    def test_summe_bis_2_is_3(self):
        self.assertEqual(summe_bis(2), 3)

    def test_summe_bis_10_is_55(self):
        self.assertEqual(summe_bis(10), 55)


# Run Tests
if __name__ == "__main__":
    unittest.main()
