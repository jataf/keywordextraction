import sys
import requests
import spacy
from bs4 import BeautifulSoup


# wenn keine URL eingegeben wird, dann wird das hier hinterlegte Portfolio prozessiert. >1 weil, an Stelle 0 immer Skriptname steht.
url = "https://serdareviceportfolioit3.wordpress.com/ruby-portfolio/"
if len(sys.argv) > 1:
    url = sys.argv[1]
    
# Funktion: Wort umgeben mit Span mit passender CSS-Class, tag = label
# \u2192 eingefügt, da vorher auch Pfeile von Spacy als Entitäten gezählt wurden
# gibt Body als string zurück
# Jedem Label wird ein Titel zugewiesen und mit in das HTML geschrieben. Beim Hovern über eine Wortmarkierung, wird der Label-Name angezeigt
def replace_with_span(body_str, word, tag):
    tagToTitle = {
        "MISC": "Misc: Miscellaneous entities, e.g. events, nationalities, products or works of art",
        "PER": "Per: Named person or family",
        "LOC": "Loc: Non-GPE locations, mountain ranges, bodies of water",
        "ORG": "Org: Companies, agencies, institutions, etc."
    }
    if word != '\u2192':
        return body_str.replace(word, "<span title='" + tagToTitle[tag] + "' class=\"spacy_" + tag.lower() + "\">" + word + "</span>")
    return body_str

# Sprachmodell laden
nlp = spacy.load('de_core_news_sm-3.2.0')


print("Portfolio von URL " + url + " wird prozessiert.")
request = requests.get(url)

# Portfolio parsen, um Text verwenden zu können
# from_encoding="UTF-8" notwendig für BeautifulSoup
soup = BeautifulSoup(request.content, 'html.parser', from_encoding="UTF-8")
doc = nlp(soup.get_text())


# Neue CSS-Classes definieren und im Dokument einfügen
new_style = soup.new_tag("style")
new_style.string = ".spacy_loc { background-color:#66FF99; padding:0.1em 0.2em; } \
                    .spacy_misc { background-color:#FFFF99; padding:0.1em 0.2em; } \
                    .spacy_per { background-color:#FF7F7F; padding:0.1em 0.2em; } \
                    .spacy_org { background-color:#58ACFA; padding:0.1em 0.2em; }"
soup.find("title").insert_after(new_style)

# Body des Dokuments verwenden (ganzer Seiteninhalt)
body = soup.find('body')
body_str = str(body)
body.clear()


# Jede gefundene Entität von spacy einfärben
# Ruby wird der Kategorie MISC zugeordnet
# Es wird ein Dictionary befüllt, in welchem jedes Wort dem passenden Label zugeordnet wird. Da die Keys eines Dictionaries einzigartig sind,
# kann jedes Wort nur einem einzigen Label zugeordnet werden.
wordToClass = dict({"Ruby": "MISC"})
for ent in doc.ents:
    if ent.text not in wordToClass.keys():
        wordToClass[ent.text] = ent.label_


# Aufruf der Methode replace_with_span mit den einzelnen Wort-Label Paaren
keys_list = list(wordToClass)
for key in keys_list:
    body_str = replace_with_span(body_str, key, wordToClass[key])


# Veränderten Body einfügen
soup.body.append(body_str)

# Neues HTML-Dokument mit veränderter Seite befüllen
# prettify formatiert den Code wieder in einzelne Zeilen
neueHTML = open("test.html", "wb")
neueHTML.write(soup.prettify(formatter=None).encode("UTF-8"))
neueHTML.close()

# Lokaler Webserver spielt erzeugte HTML aus
try:
    # Python 2
    from SimpleHTTPServer import test, SimpleHTTPRequestHandler
except ImportError:
    # Python 3
    from http.server import test, SimpleHTTPRequestHandler
print("See result here: http://localhost:8000/test.html")
test(SimpleHTTPRequestHandler)
