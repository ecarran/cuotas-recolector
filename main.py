from fastapi import FastAPI, Response, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from cuotas import recolectar_datos, obtener_csv
from datetime import datetime
import asyncio

app = FastAPI()

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.api_route("/", methods=["GET", "HEAD"], response_class=PlainTextResponse)
async def root(request: Request):
    return "OK"

@app.get("/ping")
async def ping():
    await asyncio.sleep(0.5)
    return {"message": "pong", "timestamp": datetime.now().isoformat()}

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
