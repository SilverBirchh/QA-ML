import nltk
import re

class GetInfo(object):
    def __init__(self, text):
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('maxent_ne_chunker')
        nltk.download('words')

        self.text = text
        self.textArray = self.mutate(text)

        # Add to this array
        self.totalWords = ['total', 'sum', 'balance']
    
    def mutate(self, text):
        textArray = text.splitlines()
        return [line.lower().strip() for line in textArray]

    def get_store(self):
        text = self.text
        entities = []

        for sent in nltk.sent_tokenize(text):
            for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
                if hasattr(chunk, 'label'):
                    entities += [''.join(c[0] for c in chunk)]

        # More often than not the store name is at the top
        return entities[0]

    def get_date(self):
        # Meant to match  dates like: 19.08.15
        regex = '.*?(?P<date>(\d{2,4}(\.\s?|[^a-zA-Z\d])\d{2}(\.\s?|[^a-zA-Z\d])(20)?1[3-6]))\s+'

        for line in self.textArray:
            match = re.match(regex, line)
            if match:
                return match.group(1)

    def get_total(self):
        totals = []
        for total_line in self.totalWords:
            for line in self.textArray:
                if total_line in line:
                    totals += [line]

        return totals[-1]