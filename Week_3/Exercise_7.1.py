# Problem Statement

# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the
# contents of the file in upper case. Use the file words.txt to produce the output below. You can download the sample
# data at

try:
    fileName = input("Enter file name:")
    fileHandle = open(fileName)

    for fileLine in fileHandle:
        print(fileLine.upper().rstrip())


except:
    print("The file name = "+ fileName + " is NOT valid")