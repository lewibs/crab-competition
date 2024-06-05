import math

memo = {}

def distance(x, y, steps):
    if (x, y, steps) in memo:
        return memo[(x, y, steps)]

    if steps == 0:
        dist = math.sqrt(x**2 + y**2)
        return dist 
    
    total = 0

    dist = distance(x + 1, y, steps - 1)
    total += dist
    dist = distance(x, y + 1, steps - 1)
    total += dist
    dist = distance(x - 1, y, steps - 1)
    total += dist
    dist = distance(x, y - 1, steps - 1)
    total += dist

    dist = math.sqrt(x**2 + y**2)
    total += dist
    avg = total / 5

    memo[(x, y, steps)] = avg

    return avg

# Calculate the expected distance
result = distance(0, 0, 16)
print(f"Expected Distance: {result}")