import math

steps = 16
width = steps+1+steps
height = steps+1+steps
center = [steps, steps]

def sum_table(table):
    s = 0
    for row in table:
        s+=sum(row)

    return s

def print_table(table):
    for row in table:
        print(row)

def make_table():
    return [[0 for _ in range(width)] for _ in range(height)]

def add_tables(a,b):
    new_table = make_table()
    for R in range(width):
        for H in range(height):
            new_table[R][H] = a[R][H] + b[R][H]
    return new_table

def divide_table_scalar(a, b):
    new_table = make_table()
    for R in range(width):
        for H in range(height):
            new_table[R][H] = a[R][H] / b
    return new_table

def calculate_distance(probabilities):
    table = make_table()
    s = 0
    for R in range(width):
        for H in range(height):
            dist = math.sqrt(math.pow(R-center[0],2)+ math.pow(H-center[0],2)) * probabilities[R][H]
            table[R][H] = dist
            s += dist
    return s

#Init table
tables = [make_table()]
tables[-1][center[0]][center[1]] = 1

#dead crabs is the sum of all past tables
dead_crabs = make_table()
dead_crabs = add_tables(dead_crabs, tables[-1])

actions_taken = 0

for step in range(1,steps+1):
    tables.append(make_table())

    for R in range(width):
        for H in range(height):
            old = tables[-2]
            new = tables[-1]

            if R+1 < width:
                new[R+1][H] += old[R][H]
            if R-1 >= 0:
                new[R-1][H] += old[R][H]
            if H+1 < height:
                new[R][H+1] += old[R][H]
            if H-1 >= 0:
                new[R][H-1] += old[R][H]

    alive_crabs = tables[-1]
    val = sum_table(alive_crabs)
    dead_crabs = add_tables(alive_crabs, dead_crabs)
    actions_taken = (sum_table(tables[-2]) * 5) + actions_taken
    total_posible_states = sum_table(dead_crabs)
    probabilities = divide_table_scalar(dead_crabs, actions_taken)
    distance = calculate_distance(probabilities)

# targets
# 0.8
# 0.9325483399593903
# 1.1278347196718377
# 1.195318099299252
# 1.2824979283019036
print(distance)