import paperDictionary as pD
import FrequencyTable as fT
import BayesTable as bT
import math


ham = fT.FrequencyDistribution()
jay = fT.FrequencyDistribution()
mad = fT.FrequencyDistribution()
hamPapers = {}
jayPapers = {}
madPapers = {}
unk = {}

def testcase(filename):
    test = fT.FrequencyDistribution()
    with open(str(filename) + ".txt") as file:
        for line in file:
            for word in line.split():
                if word[-1:] == "," or word[-1:] == "." or word[-1:] == ":" \
                        or word[-1:] == ";" or word[-1:] == ")" or word[-1:] == "?" or word[-1:] == "!":
                    word = word[:-1]
                if word[0] == "(":
                    word = word[1:]
                if word.isalpha():
                    test.build(word)
    test.clean()
    return test.dict

def makePrediction(freqTable):
    hamGuess = lookupTable.Ph
    jayGuess = lookupTable.Pj
    madGuess = lookupTable.Pm
    for item in freqTable:
        if item in lookupTable.probs:
            hamGuess += math.log(lookupTable.probs[item][0])
            jayGuess += math.log(lookupTable.probs[item][1])
            madGuess += math.log(lookupTable.probs[item][2])
        else:
            hamGuess += math.log(lookupTable.hUnknown)
            jayGuess += math.log(lookupTable.jUnknown)
            madGuess += math.log(lookupTable.hUnknown)
    print("\t", hamGuess)
    print("\t", jayGuess)
    print("\t", madGuess)
    result = max(hamGuess, jayGuess, madGuess)
    if result == hamGuess:
        print("I think this paper was written by Hamilton.")
    elif result == jayGuess:
        print("I think this paper was written by Jay.")
    else:
        print("I think this paper was written by Madison.")


for i in range(1, 86):
    if pD.paperDictionary[i] == "Hamilton":
        print(i, pD.paperDictionary[i])
        hamPapers[i] = fT.FrequencyDistribution()
        with open(str(i) + ".txt") as file:
            for line in file:
                for word in line.split():
                    if word[-1:] == "," or word[-1:] == "." or word[-1:] == ":"\
                            or word[-1:] == ";" or word[-1:] == ")" or word[-1:] == "?" or word[-1:] == "!":
                        word = word[:-1]
                    if word[0] == "(":
                        word = word[1:]
                    if word.isalpha():
                        ham.build(word)
                        hamPapers[i].build(word)
    elif pD.paperDictionary[i] == "Jay":
        print(i, pD.paperDictionary[i])
        jayPapers[i] = fT.FrequencyDistribution()
        with open(str(i) + ".txt") as file:
            for line in file:
                for word in line.split():
                    if word[-1:] == "," or word[-1:] == "." or word[-1:] == ":" \
                            or word[-1:] == "?" or word[-1:] == "!"or word[-1:] == ";" or word[-1:] == ")":
                        word = word[:-1]
                    if word[0] == "(":
                        word = word[1:]
                    if word.isalpha():
                        jay.build(word)
                        jayPapers[i].build(word)
    elif pD.paperDictionary[i] == "Madison":
        print(i, pD.paperDictionary[i])
        madPapers[i] = fT.FrequencyDistribution()
        with open(str(i) + ".txt") as file:
            for line in file:
                for word in line.split():
                    if word[-1:] == "," or word[-1:] == "." or word[-1:] == ":" \
                            or word[-1:] == "?" or word[-1:] == "!"or word[-1:] == ";" or word[-1:] == ")":
                        word = word[:-1]
                    if word[0] == "(":
                        word = word[1:]
                    if word.isalpha():
                        mad.build(word)
                        madPapers[i].build(word)
    else:
        print(i, pD.paperDictionary[i])
        unk[i] = fT.FrequencyDistribution()
        with open(str(i) + ".txt") as file:
            for line in file:
                for word in line.split():
                    if word[-1:] == "," or word[-1:] == "." or word[-1:] == ":" \
                            or word[-1:] == "?" or word[-1:] == "!"or word[-1:] == ";" or word[-1:] == ")":
                        word = word[:-1]
                    if len(word) > 0:
                        if word[0] == "(" and word[0] != "(":
                            word = word[1:]
                        if word.isalpha():
                            unk[i].build(word)

ham.clean()
jay.clean()
mad.clean()

combined = []
for item in ham.dict:
    combined.append(item)
for item in jay.dict:
    combined.append(item)
for item in mad.dict:
    combined.append(item)

combined = set(combined)

# needs smoothing
for item in combined:
    if item not in ham.dict:
        ham.dict[item] = 0
    if item not in jay.dict:
        jay.dict[item] = 0
    if item not in mad.dict:
        mad.dict[item] = 0

for paper in unk:
    unk[paper].clean()

for paper in hamPapers:
    hamPapers[paper].clean()

for paper in jayPapers:
    jayPapers[paper].clean()

for paper in madPapers:
    madPapers[paper].clean()

lookupTable = bT.bayesTable(ham, jay, mad)

for i in range(1, 86):
    print("\nFor federalist paper", i, ". . .")
    if i in hamPapers:
        makePrediction(hamPapers[i].dict)
    elif i in jayPapers:
        makePrediction(jayPapers[i].dict)
    elif i in madPapers:
        makePrediction(madPapers[i].dict)
    elif i in unk:
        makePrediction(unk[i].dict)

print("If you would like to test a file, please include the file in the project directory, ", end='')
makePrediction(testcase(input(" write the name of a testfile here (do not include .txt)")))




