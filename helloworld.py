from sys import argv, exit
import csv


if len(argv) != 3:
    print("Missing command line arguments")
    exit(1)
x = False
with open(argv[1], "r") as database:
    reader = csv.reader(database)
    header = next(reader)
    with open(argv[2], "r") as sequences:
        DNA = csv.reader(sequences)
        DNALine = next(DNA)
        STRlist = [None] * ((len(header)) - 1)
        DNALinestring = DNALine[0]
        index = 0

        count = 0

        for i in range(0, len(header) - 1):
            maxed = 0
            index = DNALinestring.find(header[i + 1], 0, len(DNALinestring))
            previndex = index
            if index > -1:
                count += 1
                while True:
                    index = DNALinestring.find(
                        header[i + 1],
                        index + len(header[i + 1]),
                        index + 2 * (len(header[i + 1])),
                    )

                    if index == (previndex + len(header[i + 1])):
                        count += 1
                        previndex = index
                    else:
                        if count > maxed:
                            maxed = count
                        count = 0
                        index = DNALinestring.find(
                            header[i + 1], previndex + len(header[i + 1])
                        )

                        previndex = index
                        count += 1
                        if index < 0:
                            count = 0
                            break
                STRlist[i] = str(maxed)

    dummylist = [None] * (len(header) - 1)
    for line in reader:
        for m in range(1, len(line)):
            dummylist[m - 1] = line[m]
        if STRlist == dummylist:
            print(line[0])
            x = True
        if x == True:
            break
if x == False:
    print("No Match")