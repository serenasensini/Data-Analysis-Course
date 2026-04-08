# LAB01 - Data analysis base con pandas e container Docker

## Obiettivo
Simulare un processo semplice di data analysis su un dataset di film e pubblicarlo tramite una API Flask containerizzata.
In questa consegna l'API e gia funzionante, ma le tre analisi con pandas sono lasciate come esercizio.

## Dataset

File usato: `data/IMDb_Dataset.csv`

Colonne minime usate nel laboratorio:
- `Title`
- `IMDb Rating`
- `Year`
- `Genre`

## Struttura del laboratorio
- `app.py`: entrypoint Flask
- `api/routes.py`: definizione endpoint
- `services/imdb_loader.py`: caricamento e validazione CSV
- `requirements.txt`: dipendenze Python
- `Dockerfile`: containerizzazione API
- `smoke_test.py`: test rapido dei codici di risposta

## Endpoints richiesti

### `GET /health`
Verifica che il servizio sia attivo.
### `GET /api/oldestMovie`
DA COMPLETARE: deve restituire il film piu vecchio.
### `GET /api/bestMovie`
DA COMPLETARE: deve restituire il film con rating piu alto.
### `GET /api/totMoviePerYear`
DA COMPLETARE: deve restituire il totale film per anno.
> Nota: i tre endpoint `/api/*` al momento ritornano status `301` con un messaggio "not implemented".

## Setup locale

```bash
cd /home/utente/Data-Analysis-Course/Lab01-DataAnalysis
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Verifica base

```bash
python smoke_test.py
```

## Avvio API locale

```bash
python app.py
```

Test veloce endpoint:
```bash
curl -i http://localhost:5000/health
curl -i http://localhost:5000/api/oldestMovie
curl -i http://localhost:5000/api/bestMovie
curl -i http://localhost:5000/api/totMoviePerYear
```

## Avvio con Docker

Build immagine:

```bash
docker build -t lab01-imdb-api .
```

Run container:

```bash
docker run --rm -p 5000:5000 lab01-imdb-api
```

## Esercizio per i partecipanti (TODO)

Completare le funzioni in `api/routes.py` usando pandas, partendo da `get_dataset()`:
1. `oldest_movie()`
   - convertire `Year` a numerico
   - selezionare anno minimo
   - restituire titolo e anno
2. `best_movie()`
   - convertire `IMDb Rating` a numerico
   - selezionare rating massimo
   - restituire titolo, rating e anno
3. `total_movie_per_year()`
   - raggruppare per `Year`
   - calcolare il conteggio film
   - restituire struttura JSON ordinata per anno
## Criteri di completamento
- API raggiungibile su porta `5000`
- endpoint `/health` risponde `200`
- endpoint `/api/*` implementati con logica pandas
- container Docker esegue correttamente l'API
