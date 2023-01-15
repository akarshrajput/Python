# program to find the fixing order of teams.
teams=["India","Pakistan","South Africa","Bangladesh","Newzeland","Netherlands","England","Australia"]
for a in teams:
    for b in teams:
        if a!=b:
            print(a," vs ",b)