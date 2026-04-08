FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./
COPY load_csv.py ./
COPY data ./data

# TODO (partecipanti): completare l'immagine includendo script entrypoint o profili separati per import/query.
CMD ["python", "app.py"]

