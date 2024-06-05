import math

crab_states = [[[1,0,0]]]
# crab: [status, x, y] alive=True dead=False

def move_crab(crab):
    crab_states[-1].append([0,crab[1], crab[2]])
    if crab[0]:
        crab_states[-1].append([1,crab[1], crab[2]+1])
        crab_states[-1].append([1,crab[1], crab[2]-1])
        crab_states[-1].append([1,crab[1]-1, crab[2]])
        crab_states[-1].append([1,crab[1]+1, crab[2]])

def crab_dist(crab):
    return math.sqrt(math.pow(crab[1],2)+math.pow(crab[2],2))

for i in range(15):
    crab_states.append([])
    for c in crab_states[-2]:
        move_crab(c)

sum = 0
for c in crab_states[-1]:
    sum += crab_dist(c)

length = 0
for states in crab_states:
    length += len(states)
length -= len(crab_states) - 1

print(f"distance: {sum / length}")