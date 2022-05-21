# Election_Analysis

## Project overview
A Colorado Board of Election employee has given you the following tasks to complete the election audit of a recent local congressional election

1. Calculate the total number of votes cast.
2. Get a complete list of counties.
3. Calculate the total number of votes each county received.
4. Calculate the percentage of vote for each county.
5. Determine the largest county based on number of votes cast.
6. Get a complete list of candidates who received votes.
7. Calculate the total number of votes each candidate received
8. Calculate the percentage of vote each candidate won
9. Determine the winner of the election based on popular vote

## Resources
-Data Source: election_results.csv

-Software: Python 3.7.6, Visual Studio code, 3.10.4

## Summary
The analysis of the election show that:

- There were **369,717** votes cast in the election
```
total_votes = 0
for row in reader:
  total_votes = total_votes + 1
```
- The counties and its number of votes were:
    
    -**Jefferson**: 10.5% (38,855 number of votes)
    
    -**Denver**: 82.8% (306,055 number of votes)
    
    -**Arapahoe**: 6.7% (24,801 number of votes)
```
if county_name not in counties_options: 
  counties_options.append(county_name)
  counties_votes[county_name] = 0
  counties_votes[county_name] += 1
```
    
__The largest county turnout was: *Denver*__ 
    
- The candidates results were:

    -**Charles Casper Stockham**: 23.0% (85,213 number of votes)
    
    -**Diana DeGette**: 73.8% (272,892 number of votes)
    
    -**Raymon Anthony Doane**: 3.1% (11,606 number of votes)
```
if candidate_name not in candidate_options:
  candidate_options.append(candidate_name)
  candidate_votes[candidate_name] = 0
  candidate_votes[candidate_name] += 1
```
    
__The winner of the election was: *Diana DeGette*, who received 73.8% of the vote and 272,892 number of votes.__

## Election_Audit Summary
this election_audit script could be used for other similar elections by simplily modify some attributes inside the script. For example:
1. The resources csv file to be opened has a similar format.
2. To determin which colomn represent the county and candidate name, then change the row index "row[]" respectively.
3. To change the output county and candidate summary format in order to suit for different circumstances.
