- This file pulls from a CSV file, either from scouting data from a specific team, or ScoutRadioz data
- The user inputs the category of data that they are looking to view

- **Autonomous**: *totalAutoNotes* and *autoSpeaker*
- **Teleop**: *totalTeleopNotes*,*teleopSource*,*teleopFloor*,*teleopAmp*,*teleopSpeaker*
- **Other**: *totalNotes*,*contributedPoints*,*reliabilityFactor*

- From the selection, the code will generate a bar chart with the value that each robot obtained
- Hover over each bar to get the value from a specific match, along with the match code

To install all of the necessary libraries, use the following commands in terminal:
- pip install pandas
- pip install plotly.express (to graph the data in a bar chart)
