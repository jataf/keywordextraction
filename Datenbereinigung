
import spacy
from spacy import displacy
from bs4 import BeautifulSoup
import requests
nlp = spacy.load("de_core_news_lg")
URL = "https://serdareviceportfolioit3.wordpress.com/ruby-portfolio/"
#URL = "https://tutorial.djangogirls.org/de/how_the_internet_works/"
page = requests.get(URL)


soup = BeautifulSoup(page.content, "html.parser")

#Versuch nach jedem p Punkt zu setzen
div_tag = soup.new_tag("div")
div_tag.string = "."
soup.p.string.wrap(soup.new_tag(div_tag))

result = soup.get_text().replace(". ", ".\n").lower()
#print("\n".join(item for item in result.split('\n') if item))

#Satzzeichen entfernen
#new_doc = re.sub("[^0-9a-z]"," ", result)

# Verarbeitet einen Text
doc = nlp(result)
text = ""

for token in doc:
    text += token.lemma_ + " "

doc2 = nlp(text)

#Ausgabe wird in lokalen Server mit farblicher Markierung der Wörter angezeigt
sentence_spans = list(doc2.sents)
#displacy.serve(sentence_spans, style="dep")
displacy.serve(doc2, style="ent")
