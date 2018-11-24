import nltk
import re
import dateutil.parser as dparser

class GetInfo(object):
    def __init__(self, text):
        self.download();
        
        self.text = text
        self.textArray = self.mutate(text)

        # Add to this array
        self.totalWords = ['total', 'sum', 'balance']

    def download(self):
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('maxent_ne_chunker')
        nltk.download('words')
    
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
        try:
            return entities[0]
        except Exception:
            return ''  

    def get_date(self):
        # Meant to match  dates like: 19.08.15
        # regex = '.*?(?P<date>(\d{2,4}(\.\s?|[^a-zA-Z\d])\d{2}(\.\s?|[^a-zA-Z\d])(20)?1[3-6]))\s+'

        for line in self.textArray:
            try:
                date = dparser.parse(line,fuzzy=True)
            except Exception: 
                pass
        formatDate = ''
        formatDate += str(date.day)
        formatDate += '.'
        formatDate += str(date.month)
        formatDate += '.'
        formatDate += str(date.year)

        return formatDate

    def get_total(self):
        totals = []
        total= 0
        for total_line in self.totalWords:
            for line in self.textArray:
                if total_line in line:
                    totals += [line]
        if len(totals) > 0:
            for s in totals[-1].split():
                try:
                    total = float(s)
                    if total.is_integer:
                        return total
                except Exception: 
                    pass
            value = [float(s) for s in totals if s.isdigit()]
            return value
        else:
            return 0
        