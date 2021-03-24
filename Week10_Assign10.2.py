fname = input("File name = ")
handle = open(fname)
hourdict = dict()

for lines in handle:
    if lines.startswith("From "):
        words = lines.split()
        hours = words[5].split(":")[0]
        # print(hours)
        hourdict[hours] = hourdict.get(hours, 0) + 1


for k, v in sorted(hourdict.items()):
    print(k, v)
