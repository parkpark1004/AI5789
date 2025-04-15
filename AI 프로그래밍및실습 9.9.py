#9.9

with open("coord.txt", "r") as f:
    n = int(f.readline())
    coords = []

    for _ in range(n):
        line = f.readline().strip()
        x, y = map(int, line.split())
        coords.append((x, y))

coords.sort()  

for x, y in coords:
    print(x, y)
