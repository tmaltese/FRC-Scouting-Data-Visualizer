import re
import pandas as pd
import plotly.graph_objects as go

# Define a function to extract EPA values from the given line format
def extract_epa_value(line):
    match = re.search(r"(\d+\.\d+)", line)
    if match:
        return float(match.group())
    return None

# Read data from the file
with open("../epa_output.txt", "r") as file:
    lines = file.readlines()

# Initialize lists to store data
team_numbers = []
auto_epa_values = []
teleop_epa_values = []
endgame_epa_values = []
total_epa_values = []

# Initialize variables to store current team's data
current_team_number = None
current_auto_epa = None
current_teleop_epa = None
current_endgame_epa = None
current_total_epa = None

# Parse data from each line
for line in lines:
    if line.startswith('Team Number:'):
        # If a new team number is encountered, append the previous team's data
        if current_team_number is not None:
            team_numbers.append(current_team_number)
            auto_epa_values.append(current_auto_epa)
            teleop_epa_values.append(current_teleop_epa)
            endgame_epa_values.append(current_endgame_epa)
            total_epa_values.append(current_total_epa)
        # Reset current team's data
        current_team_number = int(line.split(':')[1].strip())
        current_auto_epa = None
        current_teleop_epa = None
        current_endgame_epa = None
        current_total_epa = None
    elif line.startswith('Auto EPA:'):
        current_auto_epa = extract_epa_value(line)
    elif line.startswith('Teleop EPA:'):
        current_teleop_epa = extract_epa_value(line)
    elif line.startswith('Endgame EPA:'):
        current_endgame_epa = extract_epa_value(line)
    elif line.startswith('Total EPA:'):
        current_total_epa = extract_epa_value(line)

# Append the last team's data
if current_team_number is not None:
    team_numbers.append(current_team_number)
    auto_epa_values.append(current_auto_epa)
    teleop_epa_values.append(current_teleop_epa)
    endgame_epa_values.append(current_endgame_epa)
    total_epa_values.append(current_total_epa)

# Create DataFrame to organize the data
df = pd.DataFrame({
    'Team Number': team_numbers,
    'Auto EPA': auto_epa_values,
    'Teleop EPA': teleop_epa_values,
    'Endgame EPA': endgame_epa_values,
    'Total EPA': total_epa_values
})

# Sort DataFrame by Total EPA in descending order and reset index
df = df.sort_values(by='Total EPA', ascending=False).reset_index(drop=True)

# Create a list of colors for the bars
colors = {'Auto EPA': 'rgba(0, 0, 255, 0.6)', 'Teleop EPA': 'rgba(0, 255, 0, 0.6)', 'Endgame EPA': 'rgba(255, 0, 0, 0.6)'}

# Create the bar chart
fig = go.Figure()

# Add bars for Auto EPA, Teleop EPA, and Endgame EPA for each team
for col in ['Auto EPA', 'Teleop EPA', 'Endgame EPA']:
    fig.add_trace(go.Bar(
        x=df.index,  # Using index as x values
        y=df[col],
        name=col,
        marker_color=colors[col],
        hoverinfo='y'
    ))

# Add Total EPA annotations above each bar with adjusted y position
for index, row in df.iterrows():
    fig.add_annotation(
        x=index,
        y=row['Total EPA'],
        text=str(round(row['Total EPA'], 2)),  # Rounding to 2 decimal places
        showarrow=True,
        arrowhead=1,
        ax=0,
        ay=-40   # Adjusted y position to prevent overlap
    )

# Set custom x-axis tick labels
fig.update_layout(
    title='EPA Values by Team Number',
    xaxis=dict(title='Team Number', tickvals=df.index, ticktext=df['Team Number'].astype(str)),
    yaxis=dict(title='EPA Value'),
    barmode='stack',
    bargap=0.2
)

fig.show()
