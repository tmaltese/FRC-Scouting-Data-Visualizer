import pandas as pd
import plotly.graph_objects as go

# Read data from the CSV file
df = pd.read_csv("2024MRCMP_DAY1.csv")

# Dictionary to store grouped field options
field_options = {
    'A': ['totalAutoNotes', 'autoSpeaker'],
    'T': ['totalTeleopNotes', 'teleopSource', 'teleopFloor', 'teleopAmp', 'teleopSpeaker', 'teleopPass'],
    'O': ['totalNotes', 'contributedPoints', 'reliabilityFactor']
}

# Prompt the user to select a field
print("Select a field to display (A for Autonomous, T for Teleop, O for Other):")
selected_group = input("Enter the field group: ").strip().upper()

# Validate user input for group selection
if selected_group not in field_options:
    print("Invalid field group!")
    exit()

# Get the selected group's options
group_fields = field_options[selected_group]

# Prompt the user to select a field within the chosen group
print(f"Select a field within {selected_group}:")
for i, option in enumerate(group_fields):
    print(f"{i+1}. {option}")

field_selection = int(input("Enter the field number: ").strip())

# Validate user input for field selection
if field_selection not in range(1, len(group_fields) + 1):
    print("Invalid field selection!")
    exit()

selected_field = group_fields[field_selection - 1]

# Calculate total value of the selected field for each team
df['total_field'] = df.groupby('team_key')[selected_field].transform('sum')

# Sort teams based on the total value of the selected field in descending order
df_sorted = df.sort_values(by='total_field', ascending=False)

# Create hover text including QM number and the value of the selected field
hover_text = [f"QM: {qm}<br>{selected_field}: {value}"
              for qm, value in zip(df_sorted['match_key'], df_sorted[selected_field])]

# Create an empty list to hold only hover text for each bar
text_on_hover = ['' for _ in range(len(df_sorted))]

# Plot the selected field for each team using Plotly
fig = go.Figure()

fig.add_trace(go.Bar(
    x=df_sorted['team_key'],  # Team Key on x-axis
    y=df_sorted[selected_field],
    hoverinfo='text',
    text=text_on_hover,  # Empty text for initial display
    hovertext=hover_text,  # Assign hover text
    marker=dict(color='rgba(0, 0, 255, 0.6)'),  # Adjust color as needed
))

# Set plot layout
fig.update_layout(
    title=f"{selected_field} Values by Team",
    xaxis=dict(title='Team Key'),
    yaxis=dict(title=f"{selected_field}"),
)

fig.show()
