import math
from wordfreq import zipf_frequency

# Made by Pratham Mehta

class Wordle:
    def __init__(self):
        self.freq = {}
        self.words = []
        self.combinations = []
        self.possibilities = []

    def frequency(self):
        self.words = sorted(self.words, key = lambda k: zipf_frequency(word = k, lang = 'en'), reverse = True)

    def analyze(self, analyze, erase):
        weight = 0;
        bits = 0;
        check = 0;

        elements = [analyze[0], analyze[1], analyze[2], analyze[3], analyze[4], analyze[5]]

        if (erase == True):
            for i in range(6):
                if analyze.count(elements[i]) > 1 and self.combinations[0][i] != 'n':
                    for j in range(6):
                        if elements[i] == elements[j] and self.combinations[0][j] == 'n':
                            temp = list(self.combinations[0])
                            temp[j] = 'y'
                            self.combinations[0] = ''.join(temp)

        for combination in self.combinations:
            for word in self.words:
                for i in range(6):
                    if combination[i] == 'y':
                        if word.find(analyze[i]) >= 0 and word[i] != analyze[i]:
                            check = check + 1

                    elif combination[i] == 'g':
                        if word[i] == analyze[i]:
                            check = check + 1

                    elif combination[i] == 'n':
                        if word.find(analyze[i]) == -1:
                            check = check + 1

                    if check == 6:
                        self.possibilities.append(word)

                check = 0

            try:
                weight = weight + (len(self.possibilities) / len(self.words))
                p = len(self.possibilities) / len(self.words)
                bits = bits + (p * math.log(1 / p, 2))
            except:
                pass

            if erase == False:
                self.possibilities = []

        if erase == False:
            self.freq[analyze] = bits / weight
    
    def read(self):
        with open("words.txt") as f:
            contents = f.read().splitlines() 
            self.words.append(contents)

        with open("combinations.txt") as f:
            contents = f.read().splitlines() 
            self.combinations.append(contents)

        self.words = self.words.pop()
        self.combinations = self.combinations.pop()

        self.frequency()

    def reset(self):
        for word in self.words:
            self.freq[word] = 0

    def top(self):
        return sorted(self.freq, key=self.freq.get, reverse=True)[:15]
