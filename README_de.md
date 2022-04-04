# keywordextraction
Project: Keyword extraction from e-portfolios

Mit diesem Programm werden die Wörter aus einem deutschsprachigen Portfolio jeweils einer Kategorie zugeordnet und diese farblich in einer Kopie des Portfolios markiert. Die Kategorien sind von spacy vordefiniert und wurden mit zusätzlichen Kategorien ergänzt. Die Kategorien werden durch Mouseover/Hover erläutert.
Die Zuordnung der Wörter zu bestimmten Kategorien findet durch vortrainierte Pipelines der Software spacy statt und durch eine händisch erstelltes Dictionary, welches sich an den Concept-Maps orientiert.

Das Programm kann über die Kommandozeile verwendet werden.

Benötigte Software, Bibliotheken & Sprachmodell(e):
- Python
- request
- spacy
- bs4 von BeautifulSoup
- de_core_news_sm von Spacy
- sys


Das Programm ist in der Programmiersprache Python programmiert, da diese Programmiersprache für spacy verwendet wird. 

Für den NLP-Prozess wurde die Bibliothek spacy verwendet. Im Vorfeld wurde ein Vergleich verschiedener Bibliotheken vorgenommen, bei dem sich diese Bibliothek als vielversprechend herausgestellt hat. Vorteile von spacy sind beispielsweise, dass spacy sehr schnell und effizient eine große Menge an Textdaten verarbeiten kann, spacy Open-Source ist und im Gegensatz zu anderen Bibliotheken (wie bspw. NLTK) schnell verständlich ist.
Um http-Anfragen in Python zu senden und den HTML-Code der Seite in das Python Skript zu übertragen wurde die Python-Request-Bibliothek verwendet.
Um relevante Informationen aus dem „heruntergeladenen“ HTML-Code herauszufinden und strukturierte Daten zu parsen, wurde die Python-Bibliothek BeautifulSoup verwendet. BeautifulSoup stellt eine Menge an Funktionen zu Verfügung, mit denen das erhaltene HTML analysiert werden kann. 
Das sys-Modul von Python wird verwendet, um Argumente zu übergeben. Der Nutzer wird aufgefordert eine HTML-Adresse einzugeben. Wird keine HTML eingegeben, wird ein hinterlegtes Portfolio geladen.

Das Programm ist auf deutschsprachige Portfolios ausgerichtet, daher wurde die deutsche Pipeline de_core_news_sm von Spacy verwendet. Sollen Portfolios anderer Sprachen ausgewertet werden, so müssen die entsprechenden Sprachmodelle geladen werden.

Um das Sprachmodell zu laden sollte der Dateipfad mit angegeben werden. Mit der von spacy aufgeführten Aktion nlp = spacy.load('de_core_news_sm-3.2.0') konnte in unserem Fall das Sprachmodell nicht geladen werden. Um das Sprachmodell erfolgreich zu laden, sollte der dazugehörigen Dateipfad mit angegeben werden.
Die Ergebnisse, die spacy liefert, sind sehr ungenau und die Zuordnung der Wörter zu den Kategorien erfolgt nicht zufriedenstellend. Die Pipeline von spacy kann in dem kostenlosen Modell nicht trainiert werden. Daher wäre eine Fortführung des Projekts mit der entgeltlichen Version “https://prodi.gy/” eine zu überlegende Alternative.

 
Inhaltsverzeichnis
1. Wie man das Projekt installiert und ausführt    
2. Keyword Extraction (Endergebnis)
3. Dictionary    
4. Dictionary ohne Spacy    
5. Dictionary mit Ergänzungen von Spacy
6. Annotation in HTML    
7. Annotation mit Eingabeaufforderung        
8. Deutsche Pipeline mit Ausgabe in Datei    
9. Vergleichsprogramm englische Pipeline mit Ausgabe in Datei    
10. Programm lokal gespeichertes Portfolio    
11. Vergleichsprogramm large Pipeline mit Ausgabe in Konsole    
12. Ausgabe mit Displacy und Ausgabe auf lokalem Server

------------------------------------------------------------------------------------------------------------------------------------------------------------------------


1.    Wie man das Projekt installiert und ausführt

Importieren von Python, request, spacy, bs4 von BeautifulSoup, de_core_news_sm von Spacy. 
Alle Programme können über die Konsole gestartet werden. Je nach Programm erfolgt eine Eingabeaufforderung. Näheres wird in den einzelnen Abschnitten der Programme beschrieben.



2.    Keyword Extraction (Endergebnis)
Programm: Final keyword_extraction
Programm-Name: final_keyword_extraction.py

Ablauf:
Nach Aufruf des Programms kann der Nutzer eine Webadresse eingeben. Wird keine Webadresse vom Nutzer eingegeben, dann wird das hinterlegte Portfolio geladen. 
Das Portfolio wird anhand eines zuvor angelegten Dictionary (siehe Kapitel 3) und durch eine Pipeline von spacy bestimmten Kategorien zugeordnet. Anschließend wird ein lokaler Webserver generiert, auf dem eine Kopie des Portfolios mit den Ergebnissen der Auswertung zu sehen ist. Durch farbliche Hinterlegungen wird dargestellt, welcher Kategorie das jeweilige Wort zugeordnet ist. 

Damit mehrfach vorkommende Wörter nicht doppelt zugeordnet werden, werden die gefunden Wörter in einem Dictionary gespeichert. Dabei kann jedes Wort nur einmal vorkommen. 


Benötigte Software, Bibliotheken & Sprachmodell(e):
- Python
- request
- spacy
- bs4 von BeautifulSoup
- de_core_news_sm von Spacy
- sys
- Dictionary.py



3.    Dictionary

Programm: Dictionary 
Programmname: Dictionary.py
In diesem Programm ist die händische Zuordnung von Wörtern des Portfolio zu Kategorien hinterlegt. Die Kategorien orientieren sich an den Concept-Maps, die von Frau Rebholz zur Verfügung gestellt wurden.
Das Dictionary wird in mehreren Programmen aufgerufen.

Benötigte Software, Bibliotheken & Sprachmodell(e):
- Python



4.    Dictionary ohne Spacy

Programm: dictionary ohne Spacy
Programm-Name: dictionary_ohne_spacy.py
Mit diesem Programm soll eine optimale Auswertung der Entitäten dargestellt werden. Da die Ergebnisse durch spacy unzureichend ausfallen, soll durch dieses Programm der “Best-Case” aufzeigt werden. Dabei sind alle Entitäten händisch in einem Dictionary angelegt. Die Ausgabe erfolgt in einer neu erstellten Kopie des Portfolios.

Anmerkung: Bestimmte Wörter wie „Klasse“ oder Methoden wie „center“, „style“ konnten nicht in die Kategorien aufgenommen werden, da sie in der Ausgabe als Code ausgewertet werden. Hierfür konnte bisher keine Lösung gefunden werden. Die Worte, die nicht zugeordnet werden können, sind im Programm mit # hinterlegt.


Benötigte Software, Bibliotheken & Sprachmodell(e):
- Python
- request
- bs4 von BeautifulSoup



5.    Dictionary mit Ergänzungen von Spacy

Programm: Dictionary mit Ergänzungen von Spacy
Programmname: spacy_de_dicitionary_spacy_concept_maps.de

Mit diesem Programm soll die händische Zuordnung der Entitäten (Programm Dictionary) mit der Auswertung von spacy verbunden werden. 

Benötigte Software, Bibliotheken & Sprachmodell(e):
- Python
- request
- spacy
- bs4 von BeautifulSoup
- de_core_news_sm von Spacy
- Dictionary.py



6.    Annotation in HTML

Programm: Annotation in HTML
Programm-Name: spacy_de_annotation_in_HTML.py

Mit diesem Programm werden Entitäten mit Hilfe von Spacy aus einem deutschsprachigen Portfolio gefunden und anschließend in einer Kopie des Portfolios dargestellt. Die Wörter werden von Spacy teilweise mehreren Kategorien zugeordnet. Die Zuordnung der Kategorien wird farblich dargestellt.


Benötigte Software, Bibliotheken & Sprachmodell(e):
- Python
- request
- spacy
- bs4 von BeautifulSoup
- de_core_news_sm von Spacy


    
7.    Annotation mit Eingabeaufforderung

Programm: Annotation mit Eingabeaufforderung
Programm-Name: spacy_de_annotation_mit_eingabeaufforderung.py

Mit diesem Programm werden Entitäten mit Hilfe von Spacy aus einem deutschsprachigen Portfolio gefunden und anschließend in einer Kopie des Portfolios dargestellt. Dazu hat der Nutzer beim Start des Programms die Möglichkeit ein beliebiges Portfolio über die Kommandozeile einzugeben oder ein bereits hinterlegtes Portfolio zu verwenden. Der Nutzer muss bei beiden Fällen eine Eingabe tätigen. Bei der eigenen Eingabe eines Portfolios muss darauf geachtet werden, dass eine vollständige URL eingegeben wird, das heißt auch einschließlich “https://”.  Soll das bereits hinterlegte Portfolio verwendet werden, muss eine 1 in die Kommandozeile eingegeben und bestätigt werden. Anschließend sucht Spacy die Entitäten und ordnet sie Kategorien zu. Um eine mehrfache Zuordnung eines Wortes zu mehreren Kategorien zu vermeiden wurde ein Dictionary angelegt, mit welchem ein Wort jeweils nur einer Kategorie zugeordnet werden kann.
Den Kategorien werden im Programm verschiedene Farben zugewiesen. Im nächsten Schritt wird ein lokaler Webserver generiert, auf dem eine Kopie des Portfolios mit den Ergebnissen der Auswertung zu sehen ist. Durch farbliche Hinterlegungen wird dargestellt, welcher Kategorie das jeweilige Wort zugeordnet ist. Die farbliche Codierung bzw. die zugeordnete Kategorie wird durch hover/mouseover erläutert. 

Benötigte Software, Bibliotheken & Sprachmodell(e):
- Python
- request
- spacy
- bs4 von BeautifulSoup
- de_core_news_sm von Spacy



8.    Deutsche Pipeline mit Ausgabe in Datei

Programm: Programm deutsche Pipeline mit Ausgabe in Datei
Programm-Name: spacy_de_ausgabe_in_datei.py

Mit diesem Programm werden Entitäten mit Hilfe von Spacy aus einem deutschsprachigen Portfolio gefunden und anschließend in einer Datei in Tabellenform gespeichert. In der erstellten Tabelle werden die gefundenen Worte gezählt, anschließend das gefundene Wort, die Abkürzung der Kategorie sowie eine Beschreibung der Kategorie angezeigt. 

Dieses Programm wurde erstellt, um zu testen, wie viele Entitäten von spacy gefunden werden. Die Ergebnisse der Kategoriezuordnung durch Spacy sind nicht zufriedenstellend  ausgefallen. Aus diesem Grund wurde ein Vergleichsprogramm erstellt, in dem eine englische Pipeline von Spacy verwendet wurde. Das Ziel dabei war es herauszufinden, ob die englische Pipeline bessere Ergebnisse liefert. Dies war allerdings nicht der Fall, hier wurden sogar noch weniger Ergebnisse erzielt.

Benötigte Software, Bibliotheken & Sprachmodell(e):
- Python
- request
- spacy
- bs4 von BeautifulSoup
- de_core_news_sm von Spacy



9.    Vergleichsprogramm englische Pipeline mit Ausgabe in Datei

Programm: Vergleichsprogramm englische Pipeline mit Ausgabe in Datei 
Programm-Name: spacy_en_ausgabe_in_datei.py

Dieses Programm hat die gleichen Funktionen wie das Programm “Deutsche Pipeline mit Ausgabe in Datei”. Allerdings wird hier ein englischsprachiges Portfolio und eine englische Pipeline verwendet. Dieses Programm stellt ein Vergleichsprogramm dar, mit dem getestet werden soll, ob die englische Pipeline bessere Ergebnisse liefert als die deutsche. Die Ergebnisse sind jedoch noch geringer ausgefallen. 

Benötigte Software, Bibliotheken & Sprachmodell(e):
- Python
- request
- spacy
- bs4 von BeautifulSoup
- en_core_web_sm von Spacy



10.    Programm lokal gespeichertes Portfolio

Programm: Programm lokal gespeichertes Portfolio
Programm-Name: spacy_de_verarbeitung_lokales_portfolio.py

Mit diesem Programm werden Entitäten mit Hilfe von Spacy aus einem lokal gespeicherten deutschsprachigen Portfolio gefunden und anschließend in der Konsole in Tabellenform ausgegeben. In dieser Tabelle werde die gefundenen Worte gezählt, anschließend das gefundene Wort, die Abkürzung der Kategorie sowie eine Beschreibung der Kategorie angezeigt. 

Im Gegensatz zu den anderen Programmen wird hier ein lokal gespeichertes Portfolio ausgewertet.

Benötigte Software, Bibliotheken & Sprachmodell(e):
- Python
- request
- spacy
- bs4 von BeautifulSoup
- de_core_news_sm von Spacy



11.    Vergleichsprogramm large Pipeline mit Ausgabe in Konsole

Programm: Vergleichsprogramm large Pipeline mit Ausgabe in Konsole
Programm-Name: spacy_de_lg.py

Mit diesem Programm werden Entitäten mit Hilfe von Spacy aus einem deutschsprachigen Portfolio gefunden und anschließend in der Konsole in Tabellenform ausgegeben. In dieser Tabelle werden die gefundenen Worte gezählt, anschließend das gefundene Wort, die Abkürzung der Kategorie sowie eine Beschreibung der Kategorie  angezeigt. 

Dieses Programm stellt ein Vergleichsprogramm dar. Dabei sollte getestet werden, ob eine andere/größere deutschsprachige Pipeline bessere Ergebnisse liefert als die deutsche Standard-Pipeline (de_core_news_sm). Die Ergebnisse sind jedoch noch geringer ausgefallen. 

Anmerkungen: Durch die Verwendung von pandas werden in der Konsole nicht alle gefundenen Entitäten aufgeführt, sondern nur die ersten fünf und die letzten fünf. 

Benötigte Software, Bibliotheken & Sprachmodell(e):
- Python
- request
- spacy
- bs4 von BeautifulSoup
- de_core_news_sm von Spacy
- pandas as pd



12.    Ausgabe mit Displacy und Ausgabe auf lokalem Server

Programm: Ausgabe mit Displacy und Ausgabe auf lokalem Server
Programm-Name: spacy_de_displacy_ausgabe_lokaler_server.py

Mit diesem Programm werden Entitäten mit Hilfe von Spacy aus einem deutschsprachigen Portfolio gefunden und anschließend auf einem lokalen Server dargestellt. Die Darstellung erfolgt durch die Verwendung von Displacy. Dabei werden die Entitäten durch Displacy farblich markiert und eine Zuordnung der Kategorien dargestellt. Die ursprüngliche Formatierung/Darstellung des Portfolios wird nicht übernommen.
Displacy ist ein Visualizer von spacy. 

Anmerkung: Um den lokalen Server verwenden zu können muss im Browser “localhost:5000” eingegeben werden, anstatt des angezeigten Links. 

Benötigte Software, Bibliotheken & Sprachmodell(e):
- Python
- request
- spacy
- bs4 von BeautifulSoup
- de_core_news_sm von Spacy
- displacy von spacy

