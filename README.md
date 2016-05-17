# Large-scale Simple Question Answering with Memory Network

## Installation

Create the `SETTINGS.json` file in the root of the project containing settings from the `SETTINGS.json.example`.
One have to specify location of all datasets and other local configuration information.

## Preprocessing

Objects in the Freebase dataset are separated by a whitespace and are located in the 3rd column of those files.
Both the `f(y)` and the list of available freebase entities is prepared by the `preprocessing/freebase.py` script.
The vocabulary of individual words is produced with the `preprocessing/vocabulary.py` script.
Questions preprocessing `g(q)` is done with the `preprocessing/questions.py` script.
