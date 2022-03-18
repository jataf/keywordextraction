import spacy
from bs4 import BeautifulSoup
import requests
from spacy import displacy
import re

# Sprachmodell laden
NER = spacy.load('C:\\Users\\Verena Günther\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\de_core_news_sm\\de_core_news_sm-3.2.0')

URL = "https://alexandraseportfolioit3.wordpress.com/informatik/"
html_content = requests.get(URL).text

soup = BeautifulSoup(html_content, "lxml")
body = soup.body.text


text3 = NER(body)

options = {"compact": True, "bg": "#09a3d5",
           "color": "red", "font": "Source Sans Pro"}
displacy.serve(text3, style="ent", options=options)
# displacy.serve(text3,style="dep")



for ent in text3.ents:
    print(ent.text, ent.label_, str(spacy.explain(ent.label_)))

