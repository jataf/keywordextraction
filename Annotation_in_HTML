import requests
import spacy
from bs4 import BeautifulSoup


# Funktion: Wort umgeben mit Span mit passender CSS-Class, tag = label
# \u2192 eingefügt, da vorher auch Pfeile von Spacy als Entitäten gezählt wurden
# gibt Body als string zurück
def replace_with_span(body_str, word, tag):
    if word != '\u2192':
        return body_str.replace(word, "<span class=\"spacy_" + tag.lower() + "\">" + word + "</span>")
    return body_str

# Sprachmodell laden
nlp = spacy.load('de_core_news_sm-3.2.0')

# Portfolio aus dem Web laden
url = "https://serdareviceportfolioit3.wordpress.com/ruby-portfolio/"
request = requests.get(url)

# Portfolio parsen, um Text verwenden zu können
# from_encoding="UTF-8" notwendig für BeautifulSoup
soup = BeautifulSoup(request.content, 'html.parser', from_encoding="UTF-8")
doc = nlp(soup.get_text())


# Neue CSS-Classes definieren und im Dokument einfügen
# loc = grün
# misc = gelb
# per = rot
# org = blau
new_style = soup.new_tag("style")
new_style.string = ".spacy_loc { background-color:#66FF99; padding:0.1em 0.2em; } \
                    .spacy_misc { background-color:#FFFF99; padding:0.1em 0.2em; } \
                    .spacy_per { background-color:#FF7F7F; padding:0.1em 0.2em; } \
                    .spacy_org { background-color:#58ACFA; padding:0.1em 0.2em; }\
                    .spacy_reset { background-color:#ADD8E6 ; padding:0.1em 0.2em; }"
soup.find("title").insert_after(new_style)

# Body des Dokuments verwenden (ganzer Seiteninhalt)
body = soup.find('body')
body_str = str(body)
body.clear()


# Jede gefundene Entität von spacy einfärben
for ent in doc.ents:
    body_str = replace_with_span(body_str, ent.text, ent.label_)


# Veränderten Body einfügen
soup.body.append(body_str)

# Neues HTML-Dokument mit veränderter Seite befüllen
# prettify formatiert den Code wieder in einzelne Zeilen, ohne prettify kam eine Fehlermeldung
neueHTML = open("test.html", "wb")
neueHTML.write(soup.prettify(formatter=None).encode("UTF-8"))
neueHTML.close()
