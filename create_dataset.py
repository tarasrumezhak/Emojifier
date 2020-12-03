import json
import re
import nltk
import codecs
# nltk.download('punkt')


with open('telegram/egege/result.json') as f1:
    data_egege = json.load(f1)

with open('telegram/cs_ba/result.json') as f2:
    data_cs_ba = json.load(f2)

with open('telegram/tovarystvo_dumky/result.json') as f3:
    data_tovarystvo_dumky = json.load(f3)

with open('telegram/ucu_random/result.json') as f4:
    data_ucu_random = json.load(f4)

with open('telegram/lnu/result.json') as f5:
    data_lnu = json.load(f5)

with open('telegram/danka_the_best/result.json') as f6:
    data_danka_the_best = json.load(f6)

corpus = []

messages = data_egege['messages'] + data_cs_ba['messages'] + data_tovarystvo_dumky['messages']\
           + data_ucu_random['messages'] + data_lnu['messages'] + data_danka_the_best['messages']

for message in messages:
    if isinstance(message['text'], str):
        text = re.sub(r'[,!?;-]+', '.', message['text'])
        corpus.append(nltk.word_tokenize(text))

print(len(corpus))

# print(corpus)

with open("corpus.json", "w") as f:
    json.dump(corpus, codecs.getwriter('utf-8')(f))


