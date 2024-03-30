-**Data from TBA and Statbotics Folder**-

- These files pull the team list from The Blue Alliance API, and pulls the EPA values from the Statbotics API
- **The EVENT code compares the team's EPA at the event specific by the user input, and the TEAM code compares teams using their overall EPA for the season**
- *This tool is a way to compare teams relative to their overall EPA values, and comparing teams can be useful for coming up with picks*
- Use scoutingTEAMv2.py and graphTEAM.py to compare and view EPA values for specific teams.
- Use scoutingEVENTv3.py and graphEVENT.py to look at a team's overall EPA compared to other teams at a specific event.

To install all of the necessary libraries, use the following commands in terminal:
- pip install statbotics        (to import the EPA values)
- pip install re                
- pip install sys
- pip install plotly.express    (to graph the data in a bar chart)
- pip install pandas
- pip install requests          (to import the team list and other data from The Blue Alliance)

*Currently working on parsing scouting data such that the code can view speaker shots, amp shots and other fields on the bar chart as well*
