import spacy
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Sprachmodell laden
nlp = spacy.load("de_core_news_lg")

URL = "https://alexandraseportfolioit3.wordpress.com/informatik/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
result = soup.get_text()

doc = nlp(result)

cols =["Text", "Label", "Erklärung des Labels"]

rows = []

for ent in doc.ents:
    row = [ent.text, ent.label_, str(spacy.explain(ent.label_))]
    rows.append(row)

text_doc_object = pd.DataFrame(rows, columns=cols)

print(text_doc_object)




