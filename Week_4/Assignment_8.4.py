# Problem Statement

# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the
# split() method. The program should build a list of words. For each word on each line check to see if the word is
# already in the list and if not append it to the list. When the program completes, sort and print the resulting
# words in alphabetical order. You can download the sample data at

fileName = input("Enter the file Name: ")
words = list()
try:
    fileHandle = open(fileName)
    for lines in fileHandle:
        for word in lines.rstrip().split():
            if word not in words:
                #print(word)
                words.append(word)

    words.sort()
    print(words)


except FileNotFoundError:
    print("Invalid file Name: ")
