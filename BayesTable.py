class bayesTable:

    def __init__(self, h, j, m):
        self.combined = {}
        for item in h.dict:
            self.combined[item] = [h.dict[item], j.dict[item], m.dict[item]]

        self.rows = {}
        for item in self.combined:
            self.rows[item] = self.combined[item][0] + self.combined[item][1] + self.combined[item][2]

        self.total = 0
        for item in self.rows:
            self.total += self.rows[item]

        self.probs = {}
        self.hTotal = self.colSum(0)
        self.jTotal = self.colSum(1)
        self.mTotal = self.colSum(2)

        self.Ph = self.hTotal/(self.hTotal + self.jTotal + self.mTotal)
        self.Pj = self.jTotal/(self.hTotal + self.jTotal + self.mTotal)
        self.Pm = self.mTotal/(self.hTotal + self.jTotal + self.mTotal)

        for item in self.combined:
            self.probs[item] = [(self.combined[item][0] + 1/self.hTotal)/(self.hTotal+1),
                                (self.combined[item][1] + 1/self.jTotal)/(self.jTotal+1),
                                (self.combined[item][2] + 1/self.mTotal)/(self.mTotal+1)]

        self.hUnknown = (1 / self.hTotal) / (self.hTotal + 1)
        self.jUnknown = (1 / self.jTotal) / (self.jTotal + 1)
        self.mUnknown = (1 / self.mTotal) / (self.mTotal + 1)

    def colSum(self, colNum):
        total = 0
        for item in self.combined:
            total += self.combined[item][colNum]
        return total

