# LAB02 - Docker + MySQL + Python (scaffold)
Questo laboratorio prepara una base per usare container Docker con MySQL e una semplice app Python per eseguire query SQL.
L'obiettivo e didattico: alcune parti sono intenzionalmente lasciate incomplete (TODO) per i partecipanti.

## Obiettivi del laboratorio
- Avviare MySQL in un container Docker
- Eseguire una app Python in container
- Connettere l'app al database MySQL
- Completare query SQL di esempio
- Migliorare il `Dockerfile` seguendo i TODO

## Struttura
- `Dockerfile`: immagine della app Python (parzialmente guidata)
- `docker-compose.yml`: stack con `mysql` + `app`
- `app.py`: connessione e query di esempio (con TODO)
- `requirements.txt`: dipendenze Python
- `sql/init.sql`: schema + dati iniziali
- `smoke_test.py`: verifica veloce senza database

## 1) Verifica rapida locale (senza DB)

```bash
cd /home/utente/Data-Analysis-Course/Lab02-SQLDatabase
python smoke_test.py
```

## 2) Avvio stack con Docker Compose
```bash
cd /home/utente/Data-Analysis-Course/Lab02-SQLDatabase
docker compose up --build
```

Quando i container sono avviati, l'app prova la connessione a MySQL ed esegue le query disponibili.

## 3) Spazio esercitazione (TODO)

### In `app.py`
1. Completare la query media stipendio per dipartimento.
2. Aggiungere una query per il dipendente piu anziano.
3. Gestire eventuali errori di connessione con retry/backoff.

### In `Dockerfile`
1. Ottimizzare i layer (`COPY`/`RUN`) per ridurre i rebuild.
2. Eseguire il processo con utente non-root.
3. Aggiungere variabili ambiente o argomenti build se necessari.

## Query SQL iniziali proposte
- Già pronta: conteggio totale dipendenti.
- Da completare: media salario per dipartimento.
- Da aggiungere: dipendente piu anziano.

## Note didattiche
- `DRY_RUN=1` evita la connessione al DB e serve per validare lo scaffold.
- Se vuoi sperimentare, puoi cambiare i dati in `sql/init.sql` e rilanciare i container.
