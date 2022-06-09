<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Annotation von Social Media Kommentaren in Prodigy

Dieses spaCy Projekt enthält vorgefertige Prodigy Workflows, um Kommentare von derStandard.at zu annotieren.

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `textcat` | Annotiere Kommentare von Usern jenachdem ob diese angebracht oder unangebracht sind |
| `train` | Trainiere ein temporäres Modell um den Annotationsprozess zu beschleunigen. |
| `correct` | Korrigiere Vorhersagen des temporären Modells. |
| `train_spacy` | Trainiere ein Textcat Modell mit spaCy. |
| `streamlit` | Starte die Streamlit App um dein trainiertes Modell mit eigenen Queries zu testen. |
| `reset` | Lösche die Datenbank in Prodigy. |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| [`assets/derStandard_Kommentare.json`](assets/derStandard_Kommentare.json) | Local | 8.000 Kommentare aus dem [One Million Posts: A Data Set of German Online Discussions](https://ofai.github.io/million-post-corpus/) Datensatz |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->