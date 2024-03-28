import statbotics
import re
import sys
import plotly.express as px

# Define function to process input
def process_input(Teamnum, Year, output_file):
    sb = statbotics.Statbotics()
    print("Team Number:", Teamnum)  # Print team number to console
    print("Team Number:", Teamnum, file=output_file)  # Write team number to file
    epa_categories = ['epa_end', 'auto_epa_end', 'teleop_epa_end', 'endgame_epa_end']
    for category in epa_categories:
        epa_value = sb.get_team_year(Teamnum, Year, [category])
        print(category.capitalize().replace('_', ' ') + ": " + str(epa_value))
        print(category.capitalize().replace('_', ' ') + ": " + str(epa_value), file=output_file)  # Write EPA values to file
    print("\n", file=output_file)  # Add a newline between entries in the file

# Main loop
Year = int(input("Enter Year: "))  # Ask for the year once
inputs = []  # Store inputs before "Done" is entered
while True:
    try:
        Teamnum = int(input("Input Team Number: "))
        Done = input("Type Done if Done, or press Enter to continue: ")
        inputs.append((Teamnum, Year))  # Store inputs with the same year
        if Done.lower() == "done":
            with open("../output.txt", "w") as f:
                for Teamnum, Year in inputs:
                    process_input(Teamnum, Year, f)
            break
    except ValueError:
        print("Please enter a valid integer for Team Number.")
