# gespeichert in C:\Users\Verena Günther\PycharmProjects\keywordExtraction
import spacy
from bs4 import BeautifulSoup
import requests


# Sprachmodell laden
nlp = spacy.load('C:\\Users\\Verena Günther\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python310\\site-packages\\en_core_web_sm\\en_core_web_sm-3.2.0')

URL = "https://tutorial.djangogirls.org/en/how_the_internet_works/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
result = soup.get_text()

doc = nlp(result)



neue_datei = open('datei_englisch.txt', "w")
# cols =["Nummer", "Text", "Label", "Erklärung des Labels"]

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
