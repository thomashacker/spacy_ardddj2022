# spaCy Workshop #ardddj 2022✨

Dieses Repository enthält die Notebooks und spaCy Projects zum Workshop.

## 🔧 Requirements
Es werden folgende Bibliotheken benötigt:

```pip install spacy```

```pip install jupyter```

Alternativ kann man innerhalb des Projektordners diese Codezeile ausführen:

```pip install -r requirements.txt```

## 🔧 Sprachmodell
Sowohl die Notebooks als auch das spaCy Projekt benötigen das `de_core_news_lg` Sprachmodell:

```spacy download de_core_news_lg```

## 📓 Notebooks

Im Ordner [spaCy_notebooks](spaCy_notebooks) sind verschiedene Jupyter Notebooks welche einige Grundlagen von spaCy erklären und präsentieren.

- 01_Einführung_Grundlagen.ipynb
- 02_Lexikalische Attribute.ipynb

Command um Jupyter Notebook zu starten:

```python -m jupyter notebook```

Viele dieser Inhalte sind Ausschnitte aus dem [kostenlosen spaCy Online Kurs](https://course.spacy.io/de/).

## 🪐 spaCy Project: derStandard.at

Dieses spaCy Projekt beinhaltet Prodigy und spaCy Workflows um Kommentare zu Artikeln aus [derStandard.at](https://www.derstandard.at/consent/tcf/) zu annotieren und ein Text Klassifikations Modell zu trainieren.

Die genutzten Daten sind aus der Veröffentlichung: [One Million Posts: A Data Set of German Online Discussions](https://ofai.github.io/million-post-corpus/#citation)

```
@InProceedings{Schabus2017,
  Author    = {Dietmar Schabus and Marcin Skowron and Martin Trapp},
  Title     = {One Million Posts: A Data Set of German Online Discussions},
  Booktitle = {Proceedings of the 40th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR)},
  Pages     = {1241--1244},
  Year      = {2017},
  Address   = {Tokyo, Japan},
  Doi       = {10.1145/3077136.3080711},
  Month     = aug
}
```