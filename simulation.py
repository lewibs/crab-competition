import random
import math

N_STEPS = 2
N_SIMS = 100000000
MOVESET = [[0,1],[1,0],[0,-1],[-1,0],[0,0]]

step = lambda: random.choice(MOVESET)
is_alive = lambda a: a != [0,0]
move = lambda a,b:[a[0]+b[0], a[1]+b[1]]

dist = []
for i in range(N_SIMS):
    steps = (step() for _ in range(N_STEPS))
    position = [0,0]
    for s in list(steps):
        if is_alive(s):
            position = move(position, s)
        else:
            break

    distance = math.sqrt(math.pow(position[0], 2) + math.pow(position[1], 2))
    dist.append(distance)
    
average_dist = sum(dist) / len(dist)
print(average_dist)