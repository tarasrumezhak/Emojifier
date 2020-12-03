import numpy as np
import pandas as pd
from googletrans import Translator

data = pd.read_csv("emojify_data.csv", names=["text", "emoji_id", "?", "??"])

text = data["text"]

emoji = data["emoji_id"]

translator = Translator()

text_translated = []

# for txt in text.tolist():
translations = translator.translate(text.tolist(), src="en", dest='uk')
    # text_translated.append(translation)
# print(translations[0])

for translation in translations:
    text_translated.append(translation.text)

new_data = pd.DataFrame(columns=['text', 'emoji_id'])

new_data['text'] = pd.Series(text_translated)

new_data['emoji_id'] = emoji

print(new_data.head())

new_data.to_csv("emoji_ukr.csv", index=False)