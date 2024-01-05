#Time:        54     70     82     75
#Distance:   239   1142   1295   1253

def distance(holdtime, maxtime):
    return holdtime * (maxtime - holdtime)

part1maxtimelist = [54,70,82,75]
part1winnerdistancelist = [239,1142,1295,1253]

part2maxtimelist = [54708275]
part2winnerdistancelist = [239114212951253]


resultslist = []
for winnerdistance,maxtime in zip(part2winnerdistancelist,part2maxtimelist):
    numberofwaystowin = 0
    for holdtime in range(0,maxtime+1):
        if (winnerdistance < distance(holdtime,maxtime)):
            numberofwaystowin+=1
    resultslist.append(numberofwaystowin)

result = 1
for j in resultslist:
    result *=j

print(result)
