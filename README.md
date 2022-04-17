# Election_Analysis

Using Python to compile data and generate results of an election

# Overview
  We started with a large amount of data on a CSV file that contained all election votes.
  from this we were able to have Python search through and sort the data using loops to count votes based on County and candidate.
  We can now see total votes broken down in quantity and percentage of votes for county and candidate.
  
    Results
    Please see Election_Results file in the Analysis folder as well as command line PyPoll_Challenege for results Also printed below.
    Election Results
-------------------------
Total Votes: 369,711
-------------------------

County Votes:
Jefferson: 10.509560% (38,855)/n'Denver: 82.782227% (306,055)/n'Arapahoe: 6.708213% (24,801)/n'-------------------------
Largest County Turnout: Denver
-------------------------
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------

  -We see Denver has the largest amount of votes with 82% and our winning candidate is Diana Degette with ~73% of votes totaling 272,892 votes.
  
  Summary
    
    We can use this series of functions to easily sort through lots of data and give us results.
    This would be true even if we added multiple other counties or completely different eleciton if minipulated.
    If we needed to pull from a diffferent CSV file or add another to this data we can simply add that path at the top and 
    its resepctive name throughout the file where election_results.csv was used.
    we Could add multiple types of data if for example the csv contained data we wanted in rows 3,4,5 etc.
    
