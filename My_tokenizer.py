import numpy as np
from random import choice
class My_tokenizer(object):
    '''class docstring'''
    word_index = dict()
    def fit(self,stringlist)->None:
        '''function docstring'''
        stopwords = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ]
        global symbols
        symbols = '!@#$%^&*?<>+_-=.;: '
        idx = 1
        new_words = list()
        temp = ''
        for line in stringlist :
            for word in line.split() :
                word = word.lower()
                if word not in stopwords and word not in symbols :
                    for letter in word :
                        if letter in symbols :
                            if len(temp) > 0 :
                                new_words.append(temp)
                                temp = ''
                        else :
                            temp += letter
                if len(temp)> 0 :
                    new_words.append(temp)
                    temp = ''
        for word in new_words :
            if word not in stopwords and word not in symbols :
                if word not in self.word_index.keys() :
                    self.word_index[word] = idx
                    idx += 1
    def make_sequences(self,stringlist)->list :
        '''function docstring'''
        temp = ''
        new_words = list()
        seq = []
        sequences = []
        for line in stringlist :
            for word in line.split() :
                for letter in word.lower() :
                    if letter in symbols :
                        if len(temp)>0 :
                            if temp in self.word_index.keys() :
                                seq.append(self.word_index[temp])
                                temp = ''
                            else :
                                temp = ''
                            continue
                        else :
                            continue
                    temp += letter
                if len(temp)>0 :
                    if temp in self.word_index.keys() :
                        seq.append(self.word_index[temp])
                        temp = ''
                    else :
                        temp = ''
            if any(seq) :
                sequences.append(seq)
                seq = []
        return sequences
    def make_matrix(sequences,add_zero = 'R',cut = 'R',size = 10)->(np.array) :
        '''function docstring'''
        matrix = []
        if size>0 :
            for seq in sequences :
                if len(seq) == size :
                    matrix.append(seq)
                elif len(seq)> size :
                    if cut == 'R' :
                        matrix.append(seq[:size])
                    elif cut == 'L' :
                        idx = len(seq)-size
                        matrix.append(seq[idx:])
                    else :
                        return f'cut must be R or L not {cut}'
                else :
                    if add_zero == 'R' :
                        zero_dim = np.zeros(size-len(seq),dtype='int32').tolist()
                        seq.extend(zero_dim)
                        matrix.append(seq)
                    elif add_zero == 'L' :
                        zero_dim = np.zeros(size-len(seq),dtype='int32').tolist()
                        zero_dim.extend(seq)
                        matrix.append(zero_dim)
                    else :
                        return f'add_zero must be R or L no {add_zero}'
            return np.array(matrix)
        else :
            return 'Size must be greater than 0'
    
test_cases = ['i love my dog'
              ,'deep-learning is so fun !'
              ,'I l@ve my cat'
              ,'do you love my dog ?'
              ,'!eeee! best #     '
              ,'    '
              ,'  @@  '
              ,'%this is testing'
              ,'Th!s !S t#sT A@l$0'
              ,'wall close open door door door door door door door']

instance = My_tokenizer()
instance.fit(test_cases)
print(instance.word_index)
sequences = instance.make_sequences(test_cases)
print()
print(sequences)
print()
print(My_tokenizer.make_matrix(sequences,size=3,add_zero='L',cut='L'))
print()
sizes = [i for i in range(5,26,5)]
cut = ['R','L']
for s in sizes :
    sequences = instance.make_sequences(test_cases)
    c = choice(cut)
    a = choice(cut) 
    print(f'Matrix for size = {s} , add_zero = {a} , cut = {c} :\n')
    print(My_tokenizer.make_matrix(sequences,size=s,add_zero=a,cut=c))
exit = input('enter any key to exit :')
