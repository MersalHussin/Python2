valuesFile = open("values.txt","rt")
outputFile = open("output.txt","wt")
print("Reading values from values.txt and writing to output.txt")

sum = 0
for line in valuesFile:
    sum += int(line)
    print(line.rstrip(), file = outputFile)
print("Sum: " + str(sum) , file= outputFile)
valuesFile.close()
outputFile.close()
print("Done!")