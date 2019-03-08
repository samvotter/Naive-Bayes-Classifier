import textFilters as tF


class FrequencyDistribution:

    def __init__(self):
        self.dict = {}
        self.total = 0
        self.others = []

    def build(self, word):
        if word in self.dict:
            self.dict[word] += 1
        else:
            self.dict[word] = 1

    def removeStopwords(self):
        for word in tF.stopWords:
            if word in self.dict:
                del self.dict[word]

    def capitals(self):
        bads = []
        for word in self.dict:
            if word[0].upper() + word[1:] in self.dict and word != word[0].upper() + word[1:]:
                self.dict[word] += self.dict[word[0].upper() + word[1:]]
                bads.append(word[0].upper() + word[1:])
        for item in bads:
            del self.dict[item]

    def clean(self):
        self.removeStopwords()
        self.capitals()

    def proportion(self):
        for key in self.dict:
            self.total += self.dict[key]
        for key in self.dict:
            self.dict[key] /= self.total









