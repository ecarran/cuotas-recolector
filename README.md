# Cuotas LaLiga (FastAPI)

Este proyecto expone dos endpoints:

- `/recolectar`: recoge las cuotas actuales (no guarda archivo)
- `/descargar-csv`: recolecta y devuelve un archivo CSV descargable

## Uso con GitHub Actions

Configura un cron-job en GitHub Actions que haga:

```bash
curl -o cuotas.csv https://<tu-app>.onrender.com/descargar-csv
```

Y luego lo suba como commit automático.

## Requisitos

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Formato CSV

- liga, fecha, mercado, casa, local, visitante, seleccion, cuota, timestamp