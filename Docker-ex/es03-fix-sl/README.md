# ES03 - Correggere un Dockerfile semplice

## Obiettivo

Correggere un `Dockerfile` non funzionante e costruire un'immagine custom minimale.

## Materiale

File da correggere: `Dockerfile.broken`

## Consegna

1. Analizza il file `Dockerfile.broken`.
2. Individua gli errori sintattici o logici.
3. Correggilo in modo che l'immagine:
   - parta da Ubuntu;
   - installi `sl`;
   - permetta di eseguire `sl` come comando di default.
4. Costruisci l'immagine.
5. Avvia un container in modalita interattiva e verifica l'esecuzione del comando.

## Criteri di successo

- la build termina senza errori;
- il container esegue correttamente `sl`.

## Hint

Controlla con attenzione:

- nome del package manager;
- sintassi di `RUN`;
- posizione di `sl` nel `PATH`;
- uso corretto di `ENTRYPOINT` e `CMD`.

Per visualizzare correttamente `sl` potrebbe essere utile eseguire il container con terminale interattivo.

## Nota

Dopo aver completato l'esercizio puoi confrontare il risultato con `../Dockerfile-sl`.

