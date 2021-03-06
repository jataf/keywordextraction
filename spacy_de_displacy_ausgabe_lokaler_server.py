import spacy
from spacy import displacy
from bs4 import BeautifulSoup
import requests

nlp = spacy.load("de_core_news_sm")
URL = "https://serdareviceportfolioit3.wordpress.com/ruby-portfolio/"
page = requests.get(URL)


soup = BeautifulSoup(page.content, "html.parser")
result = soup.get_text().replace(". ", ".\n")

# Verarbeitet einen Text
doc = nlp(result)

#Ausgabe wird in lokalen Server mit farblicher Markierung der Wörter angezeigt
sentence_spans = list(doc.sents)
displacy.serve(doc, style="ent")
