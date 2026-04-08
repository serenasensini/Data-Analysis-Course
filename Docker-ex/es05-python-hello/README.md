# ES05 - Containerizzare una mini applicazione Python

## Obiettivo

Creare o completare un `Dockerfile` per eseguire una piccola applicazione Python in un container.

## Materiale

- `app.py`
- `requirements.txt`
- `Dockerfile.todo`

## Consegna

1. Completa `Dockerfile.todo` rinominandolo o trasformandolo in un `Dockerfile` funzionante.
2. Costruisci l'immagine della mini app Python.
3. Avvia il container.
4. Verifica che l'output del programma venga mostrato correttamente.
5. Prova a passare una variabile ambiente personalizzata al container per cambiare il messaggio mostrato.

## Criteri di successo

- la build funziona;
- il container esegue `app.py`;
- il messaggio cambia se passi una variabile ambiente.

## TODO suggeriti ai partecipanti

- scegliere immagine base Python appropriata;
- copiare i file nell'ordine giusto;
- installare le dipendenze;
- impostare il comando finale.

## Bonus

- Riduci il numero di layer.
- Prova a usare un tag specifico dell'immagine Python invece di `latest`.

