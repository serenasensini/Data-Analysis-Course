# Esercizi Docker - difficolta crescente

Questa cartella contiene una sequenza di esercizi pensati per verificare e consolidare le competenze dei partecipanti su:

- utilizzo di immagini da Docker Hub;
- esecuzione e gestione di container;
- lettura e scrittura di un `Dockerfile`;
- concetti base del mondo container (immagini, processi, porte, layer, cleanup);
- correzione di file malfunzionanti o incompleti.

## Prerequisiti

- Docker installato e funzionante
- terminale bash
- accesso a Docker Hub per scaricare immagini pubbliche

## Percorso consigliato

1. `es01-dockerhub-run.md` - immagini Docker Hub e comandi base
2. `es02-container-lifecycle.md` - ciclo di vita container, log, exec, porte
3. `es03-fix-cowsay/README.md` - correzione di un `Dockerfile` semplice
4. `es04-fix-ubuntu-toolbox/README.md` - miglioramento di un `Dockerfile` piu realistico
5. `es05-python-hello/README.md` - containerizzazione di una mini app Python
6. `es06-volumi-persistenza.md` - persistenza dati, volumi e bind mount

## File gia presenti nella cartella

- `Dockerfile-cowsay`: esempio di immagine minimale con `cowsay`
- `Dockerfile-sl`: esempio di immagine minimale con `sl`
- `Dockerfile-ubuntu`: esempio di immagine Ubuntu con tool di utilita

Questi file possono essere usati come riferimento **solo dopo** aver tentato gli esercizi di correzione.

## Suggerimento metodologico

Per ogni esercizio prova a:

1. leggere la consegna;
2. scrivere i comandi o completare il file;
3. eseguire il test richiesto;
4. annotare cosa hai imparato o quale errore hai corretto.

## Verifica finale consigliata

Al termine, ogni partecipante dovrebbe saper:

- scaricare ed eseguire un'immagine da Docker Hub;
- distinguere immagine e container;
- esporre una porta e verificare un servizio;
- leggere e correggere un `Dockerfile`;
- costruire un'immagine custom e lanciare un container da essa.

