# fileName = input("Enter file name")
handle = open("mbox-short.txt")

counts = dict()
bigWord = None
bigCount = 0

for lines in handle:
    if lines.startswith("From "):
        # print(lines)
        splits = lines.split()
        # print(splits)
        counts[splits[1]] = counts.get(splits[1], 0) + 1

for key, value in counts.items():
    if value > bigCount:
        bigWord = key
        bigCount = value

print(bigWord, bigCount)

