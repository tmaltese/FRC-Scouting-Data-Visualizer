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

-**Data from CSV Folder**-

- This file pulls from a CSV file, either from scouting data from a specific team, or ScoutRadioz data
- The user inputs the category of data that they are looking to view

- **Autonomous**: *totalAutoNotes* and *autoSpeaker*
- **Teleop**: *totalTeleopNotes*,*teleopSource*,*teleopFloor*,*teleopAmp*,*teleopSpeaker*
- **Other**: *totalNotes*,*contributedPoints*,*reliabilityFactor*

- From the selection, the code will generate a bar chart with the value that each robot obtained
- Hover over each bar to get the value from a specific match, along with the match code

To install all of the necessary libraries, use the following commands in terminal:
- pip install pandas
- pip instal plotly.express (to graph the data in a bar chart)
