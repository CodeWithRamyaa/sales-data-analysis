import unittest

def classify_profit(profit):
    if profit >= 100000:
        return "High Profit"
    elif profit >= 50000:
        return "Medium Profit"
    else:
        return "Low Profit"


class TestSalesAnalysis(unittest.TestCase):

    def test_high_profit(self):
        self.assertEqual(classify_profit(150000), "High Profit")

    def test_medium_profit(self):
        self.assertEqual(classify_profit(75000), "Medium Profit")

    def test_low_profit(self):
        self.assertEqual(classify_profit(24000), "Low Profit")

    def test_profit_boundary_high(self):
        self.assertEqual(classify_profit(100000), "High Profit")

    def test_profit_boundary_medium(self):
        self.assertEqual(classify_profit(50000), "Medium Profit")

    def test_zero_profit(self):
        self.assertEqual(classify_profit(0), "Low Profit")

    def test_negative_profit(self):
        self.assertEqual(classify_profit(-1000), "Low Profit")


suite = unittest.TestLoader().loadTestsFromTestCase(TestSalesAnalysis)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
