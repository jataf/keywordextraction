import spacy
from bs4 import BeautifulSoup



# Sprachmodell laden
nlp = spacy.load("de_core_news_sm")

# Öffnen der lokal gespeicherten Webseite:
with open("Informatik _ E- Portfolio IT3.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

# Alternative Möglichkeit zum öffnen der lokal gespeicherten Webseite:
# soup = BeautifulSoup(open("Informatik _ E- Portfolio IT3.html").read())

# Text von der Webseite in Variable speichern
result = soup.get_text()

doc = nlp(result)

'''
# Alternative 
inhalt = BeautifulSoup(open("Informatik _ E- Portfolio IT3.html").read())
inhalt_struktur = inhalt.decode("UTF-8")
text_inhalt_gesamt = inhalt.get_text()

doc = nlp(text_inhalt_gesamt)

'''

rows = []
i = 0

for ent in doc.ents:
    row = [i, ent.text, ent.label_, str(spacy.explain(ent.label_))]
    rows.append(row)
    print(row)
    i = i + 1

