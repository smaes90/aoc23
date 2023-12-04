with open("data/day4.txt") as file:
    data = file.readlines()

points = 0
cards = [1 for _ in data]

for index, line in enumerate(data):
    line = line.split(":")[1]
    a, b = line.split("|")
    a, b = a.split(), b.split()

    n = len(set(a) & set(b))

    if n > 0:
        points += 2 ** (n - 1)

    for i in range(n):
        cards[index + i + 1] += cards[index]

print("deel 1: " + str(points))
print("deel 2: " + str(sum(cards)))