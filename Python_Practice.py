
import csv
import os
file_to_load = os.path.join("Election_Analysis", "election_results.csv")
file_to_save = os.path.join("Election_Analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    for row in file_reader:
        print(row)
