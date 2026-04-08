# LAB03 - MySQL + CSV + Client esterno + Python

Questo laboratorio unisce i due esempi precedenti:

1. avviare MySQL con Docker,
2. caricare un dataset da `.csv`,
3. verificare i dati da un client esterno (TablePlus, DBeaver, DataGrip, ecc.),
4. interrogare il database da una applicazione Python.

Il laboratorio e guidato, ma contiene alcuni `TODO` per lasciare spazio di esplorazione ai partecipanti.

## Obiettivi didattici

- capire come esporre un DB MySQL in container;
- importare dati CSV in una tabella SQL;
- verificare i dati con un client GUI esterno;
- eseguire query SQL da Python;
- completare parti mancanti di codice/configurazione.

## Struttura del progetto

- `docker-compose.yml`: avvio del container MySQL
- `sql/init.sql`: creazione tabella `movies`
- `data/movies_dataset.csv`: dataset di esempio
- `load_csv.py`: script Python di import CSV -> MySQL
- `app.py`: script Python con query dimostrative
- `requirements.txt`: dipendenze Python
- `.env.example`: variabili ambiente di riferimento
- `smoke_test.py`: test rapido senza connessione reale (`DRY_RUN`)
- `Dockerfile`: esempio base da completare

## Prerequisiti

- Docker e Docker Compose installati
- Python 3.11+ (o compatibile con i pacchetti)
- Un client SQL esterno (es. TablePlus)

## Step 0 - Setup locale

```bash
cd /home/ssensini/PycharmProjects/Data-Analysis-Course/Lab03-Full
cp .env.example .env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Step 1 - Avvio del database MySQL

```bash
cd /home/ssensini/PycharmProjects/Data-Analysis-Course/Lab03-Full
docker compose up -d
```

Controllo stato:

```bash
docker compose ps
```

Il DB espone la porta `3307` sull'host locale.

## Step 2 - Caricamento dataset CSV

Eseguire lo script di import:

```bash
cd /home/ssensini/PycharmProjects/Data-Analysis-Course/Lab03-Full
python load_csv.py
```

Cosa fa lo script:

- legge `data/movies_dataset.csv` con pandas;
- connette MySQL usando variabili ambiente;
- svuota la tabella `movies`;
- inserisce le righe del CSV.

## Step 3 - Test da client esterno (TablePlus o simili)

Apri il tuo client e crea una nuova connessione MySQL con questi parametri:

- Host: `127.0.0.1`
- Port: `3307`
- User: `root`
- Password: `root`
- Database: `lab03_movies`

Query di verifica suggerite:

```sql
SELECT COUNT(*) AS totale_film FROM movies;
SELECT * FROM movies ORDER BY release_year ASC LIMIT 5;
SELECT genre, COUNT(*) AS totale FROM movies GROUP BY genre ORDER BY totale DESC;
```

## Step 4 - Query dal codice Python

Per eseguire l'app in modalita reale:

```bash
cd /home/ssensini/PycharmProjects/Data-Analysis-Course/Lab03-Full
DRY_RUN=0 python app.py
```

Output atteso (indicativo):

- film piu vecchio,
- film con rating piu alto,
- query placeholder per "totale film per anno" (da completare).

## Step 5 - Esercizi da completare (TODO)

### In `app.py`

1. Sostituire la query placeholder con il conteggio film per anno:
   - suggerimento: `GROUP BY release_year`.
2. Aggiungere una query con filtro per genere.
3. Migliorare la gestione errori di connessione.

### In `load_csv.py`

1. Aggiungere validazione esplicita delle colonne CSV.
2. Gestire righe non valide o valori mancanti.

### In `docker-compose.yml` e `Dockerfile`

1. Aggiungere un servizio opzionale per UI DB (es. Adminer).
2. Containerizzare anche il flusso import/query in modo piu completo.

## Verifica rapida scaffold

```bash
cd /home/ssensini/PycharmProjects/Data-Analysis-Course/Lab03-Full
python smoke_test.py
```

## Cleanup

```bash
cd /home/ssensini/PycharmProjects/Data-Analysis-Course/Lab03-Full
docker compose down
```

Per rimuovere anche i volumi (ripartenza pulita):

```bash
docker compose down -v
```

