import __init__
from math import trunc

class CovidEstimator:
      def __init__ (self):
        self.region = {
         'name':'Africa',
         'avgAge': 19.7,
         'avgDailyIncomeInUSD': 5,
         'avgDailyIncomePopulation':0.71
         }
        self.periodType = 'days'
        self.timeToElapse = 58
        self.reportedCases = 674
        self.population = 66622705
        self.totalHospitalBeds = 1380614
        self.impact = {}
        self.severeImpact = {}

      def estimator(self):
      
        self.impact['currentlyInfected1'] = self.reportedCases * 10
        self.severeImpact['currentlyInfected2'] = self.reportedCases * 50
        self.impact['infectionsByRequestedTime1'] = trunc(self.impact['currentlyInfected1'] * (2**9))
        self.severeImpact['infectionsByRequestedTime2'] = trunc(self.severeImpact['currentlyInfected2'] * (2**9))           
        self.data = self.impact|self.severeImpact  
        return self.data
       
    
estimation1 = CovidEstimator()
print(estimation1.estimator())    
       

