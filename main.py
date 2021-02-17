import csv
from decimal import Decimal

total_age_smokers = 0
number_of_smokers = 0
total_age_non_smokers = 0
number_of_non_smokers = 0
region_none_smokers = {}
region_smokers = {}

with open('insurance.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        # average age smokers versus non smokers
        if row['smoker'] == 'no':
            total_age_non_smokers += int(row['age'])
            number_of_non_smokers += 1
            if row['region'] in region_none_smokers.keys():
                region_none_smokers[row['region']] += 1
            else:
                region_none_smokers[row['region']] = 1
        else:
            total_age_smokers += int(row['age'])
            number_of_smokers += 1
            if row['region'] in region_smokers.keys():
                region_smokers[row['region']] += 1
            else:
                region_smokers[row['region']] = 1

n_smoker = "Average age of non-smokers: {0:.3g}".format(total_age_non_smokers / number_of_non_smokers)
smoker = "Average age of smokers: {0:.3g}".format(total_age_smokers / number_of_smokers)
print("Number of none-smokers: {0}, {1}". format(number_of_non_smokers, n_smoker))
print("Number of smokers: {0}, {1}". format(number_of_smokers, smoker))

print(region_smokers)
print(region_none_smokers)