import re
import json
from collections import Counter

class BagOfWords:
    def __init__(self, input_data):

        if hasattr(input_data, 'read'):
            input_text = input_data.read().lower()
        else:
            input_text = input_data.lower()

        normalized_text = re.sub(r'[^a-zA-Z\s]', '', input_text)

        self.word_counts = Counter(normalized_text.split())
    
    def __str__(self):
        return ', '.join(f"{word}:{count}" for word, count in self.word_counts.items())
    
    def __contains__(self, word):
        return word in self.word_counts

    def __iter__(self):
        return iter(sorted(self.word_counts, key=self.word_counts.get, reverse=True))
    
    def __add__(self, other):
        combined = Counter(self.word_counts)
        combined.update(other.word_counts)
        new_bag = BagOfWords('')
        new_bag.word_counts = combined
        return new_bag

    def __getitem__(self, word):
        return self.word_counts[word]
    
    def __setitem__(self, word, count):
        self.word_counts[word] = count
   
    def top10(self):
        return self.word_counts.most_common(10)
    
    def count(self, word):
        return self.word_counts[word]
    
    def save(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.word_counts, file)
    
    def load(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            self.word_counts = Counter(json.load(file))



bow = BagOfWords(open("pg1787.txt", encoding='utf-8'))



print("Most common 10 words: ", bow.top10())

print("The hamlet word count: ", bow.count("hamlet"))



import pickle

with open('bag_of_words.pkl', 'wb') as pkl_file:
    pickle.dump(bow, pkl_file)

with open('bag_of_words.pkl', 'rb') as pkl_file:
    loaded_bow = pickle.load(pkl_file)


bow.save('bag_of_words.json')
bow1 = BagOfWords('')
bow1.load('bag_of_words.json')
print(bow1)