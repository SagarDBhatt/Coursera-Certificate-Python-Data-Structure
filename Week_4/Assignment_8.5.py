counter = 0

try:
    fileName = input("Enter file name:")
    fileHandle = open(fileName)

    for line in fileHandle:

        if not line.startswith("From"):
            continue
        elif line.startswith("From:"):
            continue
        else:
            wordList = line.split()
            print(wordList[1])
            counter += 1

    print("There were", counter, "lines in the file with From as the first word")


except FileNotFoundError:
    print("File not found")