import sys

scores = []
for x in sys.argv[1:]:
    scores.append(float(x))

total = 0
for s in scores:
    total += s

average = total / len(scores)

print("Sum =", total)
print("Average =", average)
