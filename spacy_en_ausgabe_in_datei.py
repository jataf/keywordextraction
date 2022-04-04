import spacy
from bs4 import BeautifulSoup
import requests


# Sprachmodell laden
nlp = spacy.load("en_core_web_sm")

URL = "https://tutorial.djangogirls.org/en/how_the_internet_works/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
result = soup.get_text()

doc = nlp(result)



neue_datei = open('datei_englisch.txt', "w")

rows = []
i = 0

for ent in doc.ents:
    row = [i, ent.text, ent.label_, str(spacy.explain(ent.label_))]
    rows.append(row)
    neue_datei.write(str(row))
    neue_datei.write("\n")
    neue_datei.write("\n")
    i = i + 1


neue_datei.close()
