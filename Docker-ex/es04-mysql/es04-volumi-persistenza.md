# ES04 - Volumi e persistenza dei dati

## Obiettivo

Capire la differenza tra filesystem effimero del container e dati persistenti tramite volume o bind mount.

## Scenario

Usa l'immagine `mysql:8.4` oppure, in alternativa, un'immagine che scriva dati su disco in modo evidente.

## Consegna

1. Avvia un container MySQL senza volume dedicato.
2. Osserva dove vengono memorizzati i dati del database.
3. Arresta e rimuovi il container.
4. Ricrea lo stesso container, questa volta usando un volume Docker nominato.
5. Verifica che i dati persistano tra un riavvio e la ricreazione del container.

## Output atteso

- il partecipante dimostra che i dati senza volume si perdono piu facilmente;
- il partecipante mostra che con volume i dati possono essere riutilizzati.

## Bonus

- Elenca i volumi presenti sul sistema.
- Rimuovi in modo esplicito un volume non piu necessario.

