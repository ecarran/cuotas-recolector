from fastapi import FastAPI, Response
from cuotas import recolectar_datos, obtener_csv

app = FastAPI()

@app.get("/")
def root():
    return {"estado": "ok", "mensaje": "cuotas-recolector activo"}

@app.get("/healthz")
def healthz():
    return "OK"

@app.get("/recolectar")
def recolectar():
    df = recolectar_datos()
    return {"estado": "ok", "nuevos_registros": len(df)}

@app.get("/descargar-csv")
def descargar_csv():
    csv_bytes = obtener_csv()
    return Response(content=csv_bytes, media_type="text/csv", headers={
        "Content-Disposition": "attachment; filename=cuotas.csv"
    })