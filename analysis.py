#
# the class Analysis hold all the functions to perform the needed analysis functions
#
import csv

class Analysis:
    def __init__(self, csv_file):
        self.csv_file = csv_file


    def average_age_smokers_versus_non_smokers(self):
        total_age_non_smokers = 0
        number_of_non_smokers = 0
        total_age_smokers = 0
        number_of_smokers = 0

        with open('insurance.csv') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                # average age smokers versus non smokers
                if row['smoker'] == 'no':
                    total_age_non_smokers += int(row['age'])
                    number_of_non_smokers += 1
                else:
                    total_age_smokers += int(row['age'])
                    number_of_smokers += 1

        return {"age_non_smokers": total_age_non_smokers / number_of_non_smokers,
                "number_of_non_smokers": number_of_non_smokers,
                "age_smokers": total_age_smokers / number_of_smokers,
                "number_of_smokers": number_of_smokers}

    def smokers_versus_non_smokers_per_region(self):
        region_none_smokers = {}
        region_smokers = {}
        with open('insurance.csv') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if row['smoker'] == 'no':
                    if row['region'] in region_none_smokers.keys():
                        region_none_smokers[row['region']] += 1
                    else:
                        region_none_smokers[row['region']] = 1
                else:
                    if row['region'] in region_smokers.keys():
                        region_smokers[row['region']] += 1
                    else:
                        region_smokers[row['region']] = 1

        return sorted(region_none_smokers.items()), sorted(region_smokers.items())