# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Initialize a county list and county votes dictionary.
county_list = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Initialize empty string that tracks the largest county and county voter turnout.
largest_county = ""
county_voter = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Get the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 1

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write if statement that checks that county does not match any existing county in county list.
        if county_name not in county_list:

            # 4b: Add existing county to list of counties.
            county_list.append(county_name)

            # 4c: Start tracking the county's vote count.
            county_votes[county_name] = 1
            
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] +=1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = ( f"\nElection Results\n"
                         f"-------------------------\n"
                         f"Total Votes: {total_votes:,}\n"
                         f"-------------------------\n\n"
                         f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)
    county_results = ""
    # 6a: Write for loop to get county from county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve county vote count.
        county_vote = county_votes[county_name]
        # 6c: Calculate percentage of votes for county.
        county_percentage = county_vote/total_votes * 100
        county_results = (f"{county_name}: {county_percentage:.1f}% ({county_vote:,})\n")

         # 6d: Print county results to terminal.
        print(county_results)
    
    
         # 6e: Save county votes to text file.
        txt_file.write(county_results)
         # 6f: Write if statement to determine winning county and get its vote count.
    
        if (county_vote > county_voter):
            county_voter = county_vote
            largest_county = county_name
        
    # 7: Print county with largest turnout to terminal.
    largest_county = (f"-------------------------\n"
                      f"Largest County Turnout: {largest_county}\n"
                      f"-------------------------\n")
    print(largest_county)
    # 8: Save county with largest turnout to text file.
    txt_file.write(largest_county)

    # Save final candidate vote count to text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to terminal.
        print(candidate_results)
        txt_file.write(candidate_results)
        #  Save candidate results to our text file.
                

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

# Print winning candidate to terminal
winning_candidate_summary = (f"-------------------------\n"
                             f"Winner: {winning_candidate}\n"
                             f"Winning Vote Count: {winning_count:,}\n"
                             f"Winning Percentage: {winning_percentage:.1f}%\n"
                             f"-------------------------\n")
print(winning_candidate_summary)

# Save winning candidate's name to text file
with open(file_to_save, "a") as txt_file:
    txt_file.write(winning_candidate_summary)