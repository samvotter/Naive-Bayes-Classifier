Preprocessing:
text data is read in word by word. For words to be added into the frequency table they must pass through:

                    1) if word[-1:] == "," or word[-1:] == "." or word[-1:] == ":" \
                            or word[-1:] == "?" or word[-1:] == "!"or word[-1:] == ";" or word[-1:] == ")":
                        word = word[:-1]
                    2) if word[0] == "(":
                        word = word[1:]
                    3) if word.isalpha():

1) if the word ends with common punctuation, the punctuation is removed and the word kept.
2) if the word begins with "(", the symbol is removed and the word kept.
3) once steps 1 and 2 are passed, the resulting word is checked to see if it is comprised entirely of alphabetical characters. 
If so, then it is added to the frequency table

    4) def clean(self):
          self.removeStopwords()
          self.capitals()

4) clean does two things: removes any stop words, and combines any words that differ only by capitalization.
	removeStopwords() takes out things like "the" or "a" or "them"
	captials() combines values like dictionary["capital"] = 4, dictionary["Capital"] = 5, into just dictionary["Capital"] = 9



Training:
The Niave Bayes model is trained over the whole data set. All words from all Hamiliton are in the hamilton frequency table,
	all the words from all jay files are in jay's table, all madison's files are in mad's table.

All three tables are combined to form one table including words for all three authors:

combined = []
for item in ham.dict:
    combined.append(item)
for item in jay.dict:
    combined.append(item)
for item in mad.dict:
    combined.append(item)

combined = set(combined)

for item in combined:
    if item not in ham.dict:
        ham.dict[item] = 0
    if item not in jay.dict:
        jay.dict[item] = 0
    if item not in mad.dict:
        mad.dict[item] = 0

0's are then smoothed when creating the proportion of frequency / all:

 for item in self.combined:
            self.probs[item] = [(self.combined[item][0] + 1/self.hTotal)/(self.hTotal+1),
                                (self.combined[item][1] + 1/self.jTotal)/(self.jTotal+1),
                                (self.combined[item][2] + 1/self.mTotal)/(self.mTotal+1)]



Features:
The only features I really tested were turning on or off the preprocessing features I already described. The end result is what you see here.


Performance:
The classifier works well. It has a 100% success rate for the training data. When the auhtor is known to be Hamilton, it will predict Hamilton.
	When the Author is Jay it predicts Jay, when the author is Madison it predicts Madison. 100% perfect. For all the disputed files,
	it predicts Hamilton for each one. I included the raw data for how it makes the prediction and on several disputed papers you can see
	that it comes close to predicting Madison. However ultimately Hamilton wins out on each case. 

I included a function at the end where it will accept new test files. To make a predict it expects to see an already formatted frequency table
	which I have already programmed in. Just put the test file in the project directory and type in the name when prompted.   


