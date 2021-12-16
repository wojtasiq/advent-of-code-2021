measurements = []

f = open("1.in", "r")

for line in f:
    measurements.append(int(line))

f.close()

counter = 0
prev = None

for x in measurements:
    if prev is not None and prev < x:
        counter += 1
    prev = x

print(counter)
