import csv
from analysis import Analysis

smokers = Analysis('insurance.csv')

smokers_dict = smokers.average_age_smokers_versus_non_smokers()
print("Number of non smokers {0} with an average age of : {1:.3g}".format(smokers_dict['number_of_non_smokers'], smokers_dict['age_non_smokers']))
print("Number of smokers {0} with an average age of : {1:.3g}".format(smokers_dict['number_of_smokers'], smokers_dict['age_smokers']))

region_none_smokers, region_smokers = smokers.smokers_versus_non_smokers_per_region()
print(region_smokers)
print(region_none_smokers)