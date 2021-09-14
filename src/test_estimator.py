import unittest
import estimator

class testEstimator(unittest.TestCase):
    def test_data(self):
        result = estimator.CovidEstimator().estimator(28)
        self.assertEqual(result,{'currentlyInfected1': 6740, 'infectionsByRequestedTime1': 3450880, 'currentlyInfected2': 33700,
'infectionsByRequestedTime2': 17254400})
        
if __name__ == "__main__":
    unittest.main()        