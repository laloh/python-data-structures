n = 5
people = ["rosewood", "rose", "rosy", "rosemarry", "roshh"]


def nameTown(people, n):
    people = list(sorted(people))
    minNamePeople = people.pop(0)
    numIndexEqualList = []
    for p in people:
        numIndexEqual = 0
        for i in range(0, len(minNamePeople)):
            if minNamePeople[i] == p[i]:
                numIndexEqual+=1
        if numIndexEqual != 0:
            numIndexEqualList.append(numIndexEqual)

    return minNamePeople[:min(numIndexEqualList)]

print(nameTown(people, n))