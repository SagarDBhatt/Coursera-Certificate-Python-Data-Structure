# Problem Statement

# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for
# lines of the form: X-DSPAM-Confidence:    0.8475 Count these lines and extract the floating point values from each
# of the lines and compute the average of those values and produce an output as shown below. Do not use the sum()
# function or a variable named sum in your solution. You can download the sample data at
# http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
# Without using sum(): Test commit

fName = input("Enter File Name:")

try:
    fHandle = open(fName, 'r')
    totalOfVal = 0
    count = 0

    for line in fHandle:
        if line.startswith("X-DSPAM-Confidence:"):
            index = line.find("0")
            value = float(line[index:])
            totalOfVal += value
            count += 1

    print("Average spam confidence:", float(totalOfVal / count))


except:
    print("File name is not valid")
