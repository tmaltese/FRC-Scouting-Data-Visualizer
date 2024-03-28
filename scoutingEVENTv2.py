import sys
import statbotics
import re
import requests

def fetch_teams(event_code):
    url = f"https://www.thebluealliance.com/api/v3/event/{event_code}/teams/simple"
    headers = {"X-TBA-Auth-Key": "YOUR API KEY"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        teams = response.json()
        team_numbers = [team['team_number'] for team in teams]
        return team_numbers
    else:
        print("Error fetching teams:", response.status_code)
        return None

def fetch_epa_values(team_number, year):
    sb = statbotics.Statbotics()
    epa_categories = ['epa_end', 'auto_epa_end', 'teleop_epa_end', 'endgame_epa_end']
    with open("../epa_output.txt", "a") as f:
        print(f"\nTeam Number: {team_number}", file=f)
        for category in epa_categories:
            epa_value = sb.get_team_year(team_number, year, [category])
            epa_value = re.findall(r"\d+\.\d+", str(epa_value))
            if category == 'epa_end':
                print(f"Total EPA: {' '.join(epa_value)}", file=f)
            elif category == 'auto_epa_end':
                print(f"Auto EPA: {' '.join(epa_value)}", file=f)
            elif category == 'teleop_epa_end':
                print(f"Teleop EPA: {' '.join(epa_value)}", file=f)
            elif category == 'endgame_epa_end':
                print(f"Endgame EPA: {' '.join(epa_value)}", file=f)

event_code = input("Input Event Code: ")
teams = fetch_teams(event_code)

if teams:
    print("Teams attending the event:", teams)
    year = int(event_code[:4])  # Extract year from the event code
    with open("../epa_output.txt", "w") as f:
        for team_number in teams:
            fetch_epa_values(team_number, year)
    print("EPA data has been exported to 'epa_output.txt'.")
else:
    print("No teams found for the event.")
