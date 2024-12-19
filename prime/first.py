x=int(input("team A score "))
y=int(input("currently B score "))
if y>x:
    print("Team B won the Match")
elif y==x:
    print("tie ")
else:
    print((x+1)-y,"runs are needed to win the match ")


