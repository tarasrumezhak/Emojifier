import numpy as np
import csv

def read_csv(filename):
    phrase = []
    emoji = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        i = 0
        for row in csvReader:
            if i != 0:
                phrase.append(row[0])
                emoji.append(row[1])
            i+=1

    X = np.asarray(phrase)
    Y = np.asarray(emoji, dtype=int)

    return X, Y

X, Y = read_csv("emoji_ukr.csv")

print(Y)