from fastapi import FastAPI, Response
from cuotas import recolectar_y_guardar, obtener_csv

app = FastAPI()

@app.get("/")
def root():
    return {"estado": "ok", "mensaje": "cuotas-recolector activo"}

@app.get("/healthz")
def healthz():
    return "OK"

@app.get("/recolectar")
def recolectar():
    total = recolectar_y_guardar()
    return {"estado": "ok", "nuevos_registros": total}

@app.get("/descargar-csv")
def descargar_csv():
    csv_bytes = obtener_csv()
    return Response(content=csv_bytes, media_type="text/csv", headers={
        "Content-Disposition": "attachment; filename=cuotas.csv"
    })