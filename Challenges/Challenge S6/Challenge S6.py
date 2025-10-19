stringsFile = open("strings.txt", "rt")
outputFile = open("output.txt", "wt")

phrase = ""
for line in stringsFile:
    if line.strip() == "I":
        phrase += " " + line.strip().capitalize()
    elif line.strip() == "Almadrasa":
        phrase += " " + line.strip()
    else:
        phrase += " " + line.strip().lower()
print(f"{phrase.rstrip()}" , file=outputFile)
print(phrase)
outputFile.close()
stringsFile.close()