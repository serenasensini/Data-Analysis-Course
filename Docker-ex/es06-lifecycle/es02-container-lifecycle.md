# ES02 - Ciclo di vita del container

## Obiettivo

Allenarsi con i comandi di gestione del ciclo di vita: avvio, stop, restart, log, accesso interattivo e ispezione.

## Scenario

Usa l'immagine `redis:7-alpine` oppure un'immagine equivalente disponibile su Docker Hub.

## Consegna

1. Avvia un container Redis in background.
2. Verifica che sia in esecuzione.
3. Visualizza i log del container.
4. Entra nel container con una shell usando `docker exec`.
5. Individua il processo principale in esecuzione nel container.
6. Ferma il container.
7. Riavvialo.
8. Infine rimuovilo.

## Domande guida

- Cosa cambia tra un container lanciato in foreground e uno in background?
- A cosa serve `docker exec`?
- Cosa succede ai dati del container se lo rimuovi?

## Vincoli

- Usa un nome esplicito per il container.
- Esegui almeno un comando dall'interno del container.

## Bonus

Esegui anche un comando `docker inspect` e individua:

- indirizzo IP del container;
- nome immagine usata;
- stato corrente.

