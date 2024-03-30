import statbotics
import re
import sys
import plotly.express as px
from legacy import execfile

sb = statbotics.Statbotics()
while True:
    Teamnum = int(input("Input Team Number: "))
    Year = int(input("Enter Year: "))
    Done = str(input("Type Done if Done: "))
    a= str(sb.get_team_year(Teamnum,Year,['epa_end']))
    aa= re.findall("\d+\.\d+", a)
    print("Total EPA: " + str(aa))
    b=str(sb.get_team_year(Teamnum,Year,['auto_epa_end']))
    bb=re.findall("\d+\.\d+", b)
    print("Auto EPA: " + str(bb))
    c=str(sb.get_team_year(Teamnum,Year,['teleop_epa_end']))
    cc=re.findall("\d+\.\d+", c)
    print("Teleop EPA: " + str(cc))
    d=str(sb.get_team_year(Teamnum,Year,['endgame_epa_end']))
    dd=re.findall("\d+\.\d+", d)
    print("Endgame EPA: " + str(dd))
    if Done == "Done":
        orig = sys.stdout
        with open("output.txt", "wb") as f:
            sys.stdout = f
            try:
                execfile("scoutinginput.py", {})
            finally:
                sys.stdout = orig
        break






"epa_end"
"auto_epa_end"
"teleop_epa_end"
"endgame_epa_end"
