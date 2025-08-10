from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from cuotas import recolectar_datos, obtener_csv
from datetime import datetime
import asyncio

app = FastAPI()

@app.get("/healthz")
def healthz():
    return "OK"

@app.get("/", response_class=HTMLResponse)
def root():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <html>
        <head><title>Cuotas Recolector</title></head>
        <body>
            <h1>Servicio activo</h1>
            <p>Última actualización: {now}</p>
        </body>
    </html>
    """

@app.get("/ping")
async def ping():
    await asyncio.sleep(0.5)  # simula carga útil
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
