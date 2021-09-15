import unittest
import estimator

class testEstimator(unittest.TestCase):
    def test_data(self):
        result1 = estimator.CovidEstimator().estimator(0,0,28)
        self.assertEqual(result1,{'currentlyInfected1': 6740, 'infectionsByRequestedTime1': 3450880, 'currentlyInfected2': 33700,
       'infectionsByRequestedTime2': 17254400})
        result2 = estimator.CovidEstimator().estimator(1,2,60)
        self.assertEqual(result2,{'currentlyInfected1': 6740, 'infectionsByRequestedTime1': 115792318300160, 'currentlyInfected2': 33700, 'infectionsByRequestedTime2': 578961591500800})
        
if __name__ == "__main__":
    unittest.main()        