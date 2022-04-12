Project: Keyword Extraction from e-portfolios

With this program the words of a German portfolio are assigned to categories and marked in different colors. The Output is displayed in a local copy of the portfolio.
The categories are predefined from spacy. On top of that, the already existing categories are extended with extra categories, based on the concept-maps. The categories are explained with Mouseover/Hover effect. 
Which word belongs to which category is set with the software spacy and with a dictionary created by hand, based on the concept-maps.
The program is a command-line program. 

Software, libraries and language models you need:
-	Python
-	request
-	spacy
-	bs4 von BeautifulSoup
-	de_core_news_sm von Spacy
-	sys
-	re

The program is programmed in the programming language python because it is used by working with spacy.
For the NLP-process the library of spacy was used. In the beginning of this project the comparison of different NLP-libraries resulted in the best promising for this work would be spacy. Spacy offers different advantages. Spacy is a fast and efficient library for working with large text amounts. Spacy Open-Source is in comparison with other NLP-libraries quickly understandable. 
To send http-requests and to transfer the html-code to the python script, python-request-library is used. 
To get relevant information of the downloaded html-code and to parse structured data, the python library BeautifulSoup is used. BeautifulSoup offers different functions to analyze and work with the html.
The sys-modul is used by python to hand over arguments. The user is requested to type in a html-adress. If no html is given, a deposit portfolio loaded. 
The program is based on german portfolios. Because of this, the german pipeline of spacy ‘de_core_news_sm’ is used. If portfolios with other languages should be analyzed, than another language model is needed. Keep in mind that the dictionary is based on german concept-maps. So it won’t be working with other languages. 
To load the language model it is useful to indicate the path file. With the written action from spacy nlp = spacy.load('de_core_news_sm-3.2.0') the language model couldn’t be loaded in our case. 
The results of spacy are inaccurate and the classification of the categories is not fitting in most cases. Therefore a continuation of the project with the purchasable version https://prodi.gy/ would be an alternative to consider.

Table of contents
1 How to install and run the project
2 Keyword Extraction (Endergebnis)
3 Dictionary
4 Dictionary ohne Spacy
5 Dictionary mit Ergänzungen von Spacy
6 Annotation in HTML
7 Annotation mit Eingabeaufforderung
8 Deutsche Pipeline mit Ausgabe in Datei
9 Vergleichsprogramm englische Pipeline mit Ausgabe in Datei
10 Programm lokal gespeichertes Portfolio
11 Vergleichsprogramm large Pipeline mit Ausgabe in Konsole
12 Ausgabe mit Displacy und Ausgabe auf lokalem Server

1 How to install and run the project
Import python, request, spacy, bs4 von BeautifulSoup, de_core_news_sm from spacy. The programs can be started by command-line. Some programs consist of a user request. More detailed is written in the individual sections.

2 Keyword Extraction (Endergebnis) Program: Final keyword_extraction Program-name: final_keyword_extraction.py
Process: after starting the program the user can enter a website address. If no webadress is given, the predefined portfolio will be loaded.
The portfolio is analyzed by the Dictionary (Chapter 3) and by the pipeline provided from spacy. Then a local webserver is generated on which a copy of the portfolio with the results is displayed. The words are colored depending on the categories. 
 
Software, libraries, and language models you need:

    Python
    request
    spacy
    bs4 von BeautifulSoup
    de_core_news_sm von Spacy
    sys
    Dictionary.py
    re

3 Dictionary
Program: Dictionary Program name: Dictionary.py
In this program the words are assigned to categories by hand. The categories are based on the concept-maps which Mrs. Rebholz offered. The program dictionary.py is used in several programs of this project.
Software, libraries, and language models you need:
Python 

4 Dictionary ohne spacy – dictionary without spacy
Program: dictionary ohne Spacy Program name: dictionary_ohne_spacy.py
With this program an optimal analyzation of the entities is displayed. Because the results provided by spacy are not, with this program the best case is given. All entities are created in the dictionary by hand. The results are displayed in a copy of the portfolio. 
Note: specific words like “Klasse”, “center”, “style” couldn’t be included in the dictionary, because in the output they are interpreted as code. For now, there is no solution for this problem. The words which can’t be allocated, are stored in the program with “#”. 

Software, libraries, and language models you need:
    Python
    request
    bs4 von BeautifulSoup

5 Dictionary mit Ergänzungen von spacy – Dictionary with additions from spacy
Program: Dictionary mit Ergänzungen von Spacy
Program name: spacy_de_dicitionary_spacy_concept_maps.de
With this program the hand-based mapping of the entities (program dictionary) is connected to the analysis of spacy. 

Software, libraries, and language models you need:

    Python
    request
    spacy
    bs4 von BeautifulSoup
    de_core_news_sm von Spacy
    Dictionary.py

6 Annotation in HTML 
Program: Annotation in HTML Programm name: spacy_de_annotation_in_HTML.py
Entities are detected by spacy and displayed in a local copy of the portfolio. The words are assigned to different categories simultaneously. The categories are displayed in different colors. 
Software, libraries, and language models you need:
    Python
    request
    spacy
    bs4 von BeautifulSoup
    de_core_news_sm von Spacy

7 Annotation mit Eingabeaufforderung – annotation with input request 
Program: Annotation mit Eingabeaufforderung Program name: spacy_de_annotation_mit_eingabeaufforderung.py
Entities are detected by spacy from a german portfolio and displayed in a local copy of the portfolio. The user has the possibility to enter a web address or to use an already stored portfolio. In both cases the user must give an input. Note: please use complete URL containing of “https://”. 
If requested to use the already stored portfolio, the user must press the enter the number 1 in the command line and confirm the input.
Then spacy detects the entities and assign them to the categories. To avoid assignments of one word to multiple categories, a dictionary is used. With the dictionary every word can be assigned to only one category. The categories are displayed in different colors. 
As the next step a local server is generated on which the results are displayed. It is visible which word is assigned to which category. With a mouseover/hover effect it is possible to see the name of the category of the colored word. 

 Software, libraries, and language models you need:
    Python
    request
    spacy
    bs4 von BeautifulSoup
    de_core_news_sm von Spacy

8 Deutsche Pipeline mit Ausgabe in Datei – German pipeline with output in file
Program: Programm deutsche Pipeline mit Ausgabe in Datei Program name: spacy_de_ausgabe_in_datei.py
Entities are detected with spacy from a German portfolio and saved as a table in a file. In the table the detected words are counted. Furthermore, the word, shortcut of the categories and the description of the category is displayed in the table.
The program was written to figure out, how many entities spacy can detect from a specific portfolio or website. The results spacy provides aren’t pleasing. Therefore, a program to compare the German with the English pipeline was written. The aim was to get to know if the English pipeline provides better results than the German pipeline. Therefore, the same website in English and German has been used for the analysis. The result showed that the English pipeline was even worse than the German one.

Software, libraries, and language models you need:
    Python
    request
    spacy
    bs4 von BeautifulSoup
    de_core_news_sm von Spacy

9 Vergleichsprogra,, englische Pipeline mit Ausgabe in Datei – English pipeline with output in file
The program has the same function as the program above (Chapter 8). The Website which has been used was English written. It was the exact same content as in the German website. The result showed that the English pipeline was even worse than the German one.
Software, libraries, and language models you need:
    Python
    request
    spacy
    bs4 von BeautifulSoup
    de_core_news_sm von Spacy
	
10 Programm local gespeichertes Portfolio – program local saved portfolio
Program: Programm lokal gespeichertes Portfolio Program name: spacy_de_verarbeitung_lokales_portfolio.py
Entities are detected from a local saved file by spacy. The output is displayed in a table in the command line.
In the table the detected words are counted. Furthermore, the word, shortcut of the categories and the description of the category is displayed in the table.
In contrast to the other programs a local saved portfolio is analyzed. 
Software, libraries, and language models you need:
    Python
    request
    spacy
    bs4 von BeautifulSoup
    de_core_news_sm von Spacy

11 Vergleichsprogramm large Pipeline mit Ausgabe in Konsole – large pipeline with output in command line
Program: Vergleichsprogramm large Pipeline mit Ausgabe in Konsole Program name: spacy_de_lg.py
Entities are detected from a portfolio by spacy. The output is displayed in a table in the command line. In the table the detected words are counted. Furthermore, the word, shortcut of the categories and the description of the category is displayed in the table.
The program is a comparison with the small pipeline from spacy. The aim is to detect if the large pipeline provides better results than the default pipeline (de_core_news_sm). The detected words in the large pipeline were even smaller than in the default pipeline. 
Note: By using pandas not all detected entities are listed in the command line. Just the first and last five words are displayed. 
Software, libraries, and language models you need:
    Python
    request
    spacy
    bs4 von BeautifulSoup
    de_core_news_sm von Spacy
    pandas as pd

12 Ausgabe mit Displacy und Ausgabe auf lokalem Server - Output with displacy and on a local server
Program: Ausgabe mit Displacy und Ausgabe auf lokalem Server Program name: spacy_de_displacy_ausgabe_lokaler_server.py
Entities are detected by spacy from a German portfolio and displayed on a local server. The Display is made by the use of Displacy. It is a visualizer provided by spacy.
The detected entities are colored by displacy. Each color assigns to a category. The original formatting of the website is not adopted by displacy. 
Note: For using the local server “localhost:5000” should be typed in the browser rather than the displayed link.

Software, libraries, and language models you need:
    Python
    request
    spacy
    bs4 von BeautifulSoup
    de_core_news_sm von Spacy
    displacy von spacy
