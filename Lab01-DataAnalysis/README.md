# LAB01 - Flask + pandas + Docker

Questo laboratorio prepara una piccola API Flask che legge un dataset film e lascia ai partecipanti l'implementazione con pandas delle statistiche richieste.
La guida completa del laboratorio e in `LAB01.md`.

## Avvio rapido
```bash
cd /home/utente/Data-Analysis-Course/Lab01-DataAnalysis
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python smoke_test.py
python app.py
```
## Avvio con Docker
```bash
docker build -t lab01-imdb-api .
docker run --rm -p 5000:5000 lab01-imdb-api
```
