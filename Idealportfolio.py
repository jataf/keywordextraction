import requests
from bs4 import BeautifulSoup


# Funktion: Wort umgeben mit Span mit passender CSS-Class, tag = label
# \u2192 eingefügt, da vorher auch Pfeile von Spacy als Entitäten gezählt wurden
# gibt Body als string zurück
# Jedem Label wird ein Titel zugewiesen und mit in das HTML geschrieben. Beim Hovern über eine Wortmarkierung, wird der Label-Name angezeigt
def replace_with_span(body_str, word, tag):
    tagToTitle = {
        "daten": "Datentyp",
        "variable": "Variable",
        "methode": "Methode",
        "klasse": "Klasse",
        "objekt": "Objektorientiertes Design",
        "sprache": "Programmiersprache",
        "events": "Events",
        "zeit": "Zeitgesteuerte Aktion",
        "zeichen": "Zeichenelemente",
        "elemente": "Elemente",
        "person": "Personen"
    }
    return body_str.replace(word, "<span title='" + tagToTitle[tag] + "' class=\"" + tag.lower() + "\">" + word + "</span>")

# Portfolio aus der Usereingabe laden
#print("Bitte Portfolio URL eingeben:")
#print("([1] eingeben um Beispiel Portfolio zu verwenden)")
#url = input()
#if (url == "1"):
 #   url = "https://serdareviceportfolioit3.wordpress.com/ruby-portfolio/"
#print("Portfolio von URL " + url + " wird prozessiert.")

# Portfolio aus dem Web laden
url = "https://serdareviceportfolioit3.wordpress.com/ruby-portfolio/"
request = requests.get(url)

# Portfolio parsen, um Text verwenden zu können
# from_encoding="UTF-8" notwendig für BeautifulSoup
soup = BeautifulSoup(request.content, 'html.parser', from_encoding="UTF-8")
doc = (soup.get_text())


# Neue CSS-Classes definieren und im Dokument einfügen
new_style = soup.new_tag("style")
new_style.string = ".daten { background-color:#66FF99; padding:0.1em 0.2em; } \
                    .variable { background-color:#FFFF99; padding:0.1em 0.2em; } \
                    .methode { background-color:#FF7F7F; padding:0.1em 0.2em; } \
                    .klasse { background-color: #F781BE; padding:0.1em 0.2em; } \
                    .objekt { background-color:#dec1a6; padding:0.1em 0.2em; } \
                    .sprache { background-color:#0088FF; padding:0.1em 0.2em; } \
                    .events { background-color:#fffacd; padding:0.1em 0.2em; } \
                    .zeit { background-color:#f4a460; padding:0.1em 0.2em; } \
                    .zeichen { background-color:#f08080; padding:0.1em 0.2em; } \
                    .elemente { background-color:#ffb6c1; padding:0.1em 0.2em; } \
                    .person { background-color:#7b68ee; padding:0.1em 0.2em; }"

soup.find("title").insert_after(new_style)

# Body des Dokuments verwenden (ganzer Seiteninhalt)
body = soup.find('body')
body_str = str(body)
body.clear()


# Jede gefundene Entität von spacy einfärben
# Ruby wird der Kategorie MISC zugeordnet
# Es wird ein Dictionary befüllt, in welchem jedes Wort dem passenden Label zugeordnet wird. Da die Keys eines Dictionaries einzigartig sind,
# kann jedes Wort nur einem einzigen Label zugeordnet werden.
wordToClass = dict({"String": "daten",
                    "Programmieren": "sprache",
                    "Programmierung": "sprache",
                    "Objektorientierte Umgebung": "objekt",
                    "Frau Rebholz": "person",
                    "Herr Müller": "person",
                    "Ruby": "sprache",
                    "Rubys": "sprache",
                    "Datentypen": "daten",
                    "Variablen": "variable",
                    #"Variable": "variable",
                    "Kontrollstrukturen": "sprache",
                    "Arrays": "variable",
                    "Array": "variable",
                    "ARRAYS": "variable",
                    "ARRAY": "variable",
                    "array": "variable",
                    "Hashes": "variable",
                    "HASHES": "variable",
                    "Hash": "variable",
                    "Test-Driven-Development": "methode",
                    "Objektorientierung": "objekt",
                    "flows": "elemente",
                    "flow": "elemente",
                    "stacks": "elemente",
                    "stack": "elemente",
                    "Shoes": "sprache",
                    "Interaktionen": "events",
                    "Yukihiro Matsumoto": "person",
                    "Webframework": "sprache",
                    "Programmiersprachen": "sprache",
                    "Skriptsprache": "sprache",
                    "Zeile": "sprache",
                    "Maschinensprache": "sprache",
                    "Interpreter": "sprache",
                    "objektorientierte": "objekt",
                    #"Objekt": "objekt", #sorgt für Fehler in der Ausgabe HTML-Code wird angezeigt
                    "Klasse": "klasse",
                    #"Programmiersprache": "sprache", #sorgt für gleichen Fehler wie bei Objekt
                    "Programmiermethodiken": "sprache",
                    "Programmierparadigmen": "sprache",
                    ">Maschinensprache": "sprache",
                    #">Ruby": "sprache",
                    "SHOES": "sprache",
                    #"Programm": "sprache", #es kommt auch zu dem Fehler
                    "INTERPRETER": "sprache",
                    "Maschinenbefehle": "objekt",
                    "ALGORITHMEN": "sprache",
                    "Algorithmen": "sprache",
                    #"Programme": "sprache",
                    "Anweisungen": "sprache",
                    "interpretiert": "sprache",
                    "Code": "sprache",
                    "puts": "sprache",
                    "DATENTYPEN": "daten",
                    #"Daten": "daten",
                    "Computerprogrammen": "sprache",
                    "Integer": "daten",
                    "Float": "daten",
                    "ZEICHEN": "daten",
                    "Raute": "sprache",
                    "Zahlen": "daten",
                    "Zeichen": "daten",
                    "Boolean": "daten",
                    "Boolsche Werte": "daten",
                    "Bool’sche": "daten",
                    "true": "sprache",
                    "false": "sprache",
                    "Zahl": "daten",
                    "lokal": "klasse",
                    "lokalen": "klasse",
                    "globalen": "klasse",
                    "global": "klasse",
                    #"nil": "sprache",
                    "Literale": "sprache",
                    "Literal": "sprache",
                   # "Methode": "methode",
                    "Methoden": "methode",
                    "Operatoren": "klasse",
                    "Operator": "klasse",
                    "Zuweisungsoperatoren": "klasse",
                    "Punktoperator": "klasse",
                    "Funktionen": "objekt",
                    "Funktion": "objekt",
                    "Parameter": "variable",
                    "parameter": "variable",
                    "Schleife": "sprache",
                    "Iterator": "sprache",
                    "Iteratoren": "sprache",
                    "ITERATOREN": "sprache",
                    "Iteration": "sprache",
                    #"Element": "elemente",
                    "downto": "methode",
                    "upto": "methode",
                    "step": "methode",
                    "Bubble-Sort Prinzip": "methode",
                    "Vererbung": "klasse",
                    "vererben": "klasse",
                    "Subklassen": "klasse",
                    "Framework": "sprache",
                    "FLOWS": "elemente",
                    "Flows": "elemente",
                    "Flow": "elemente",
                    "STACKS": "variable",
                    "Stacks": "variable",
                    "code": "objekt",
                    "LINIEN": "zeichen",
                    "line": "zeichen",
                    "RECHTECKE": "zeichen",
                    "Rechteck": "zeichen",
                    "rect": "zeichen",
                    "STERNE": "zeichen",
                    "star": "zeichen",
                    "KREIS": "zeichen",
                    "oval": "zeichen",
                    "Linien": "zeichen",
                    "Ränder": "zeichen",
                    "fill": "sprache",
                    "stroke": "sprache",
                    "under": "sprache",
                   # "align": "sprache",
                    "Stack": "variable",
                   # "center": "sprache",
                   # "style": "sprache",
                   # "curve": "sprache",
                   # "emphasis": "sprache",
                   # "family": "sprache",
                   # "weight": "sprache,
                    "Radio": "elemente",
                    "radio": "elemente",
                    "Button": "elemente",
                    "EDIT LINES": "elemente",
                    "edit lines": "elemente",
                    "Edit Lines": "elemente",
                   #"EVENTS": "events",
                   # "Events": "events",
                    "Drücken von Tasten": "events",
                    "Mausklick": "events",
                    #"HOVER": "events",
                    #"hover": "events",
                    #"Hover": "events",
                    "CLICK EVENTS": "events",
                    "Click-Event": "events",
                    "Kreis": "zeichen",
                    "Klick": "events",
                    "Klicken": "events",
                    "KEYPRESS EVENT": "events",
                    "Keypress-Event": "events",
                    "Eingaben": "events",
                    "Drück": "events",
                    "drücken": "events",
                    "MOTION EVENT": "events",
                    "Motion-Event": "events",
                    "Mauszeiger": "events",
                    "ANIMATION EVENT": "events",
                    "Animation": "events"

                    })
#for ent in doc.ents:
   # if ent.text not in wordToClass.keys():
    #    wordToClass[ent.text] = ent.label_


# Aufruf der Methode replace_with_span mit den einzelnen Wort-Label Paaren
keys_list = list(wordToClass)
for key in keys_list:
    body_str = replace_with_span(body_str, key, wordToClass[key])


# Veränderten Body einfügen
soup.body.append(body_str)

# Neues HTML-Dokument mit veränderter Seite befüllen
# prettify formatiert den Code wieder in einzelne Zeilen
neueHTML = open("idealportfolio.html", "wb")
neueHTML.write(soup.prettify(formatter=None).encode("UTF-8"))
neueHTML.close()
