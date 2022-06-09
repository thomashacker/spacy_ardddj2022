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

Dieses spaCy Projekt beinhaltet Prodigy und spaCy Workflows um Kommentare zu Artikeln aus derStandard.at zu annotieren und ein Text Klassifikations Modell zu trainieren.

