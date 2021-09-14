import unittest
import estimator

class testEstimator(unittest.TestCase):
    def test_data(self):
        result1 = estimator.CovidEstimator().estimator(28)
        self.assertEqual(result1,{'currentlyInfected1': 6740, 'infectionsByRequestedTime1': 3450880, 'currentlyInfected2': 33700,
       'infectionsByRequestedTime2': 17254400})
        result2 = estimator.CovidEstimator().estimator(29)
        self.assertEqual(result2,{'currentlyInfected1': 6740, 'infectionsByRequestedTime1': 3450880, 'currentlyInfected2': 33700,
'infectionsByRequestedTime2': 17254400})
        
if __name__ == "__main__":
    unittest.main()        