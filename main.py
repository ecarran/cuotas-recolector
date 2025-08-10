from fastapi import FastAPI, Response
from cuotas import recolectar_datos, generar_csv

app = FastAPI()

@app.get("/recolectar")
def recolectar():
    df = recolectar_datos()
    return {"estado": "ok", "registros": len(df)}

@app.get("/descargar-csv")
def descargar_csv():
    df = recolectar_datos()
    csv_bytes = generar_csv(df)
    return Response(content=csv_bytes, media_type="text/csv", headers={
        "Content-Disposition": "attachment; filename=cuotas.csv"
    })