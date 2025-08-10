import requests
import time
import pandas as pd
from datetime import datetime
from io import StringIO
import os
API_KEY = os.getenv("ODDS_API_KEY")
BASE = "https://api.the-odds-api.com/v4/sports/{sport}/odds"
MARKET = "h2h"
REGION = "eu"

SPORTS = [
    "soccer_spain_la_liga",
    "soccer_spain_segunda_division",
]

def fetch_odds(sport_key):
    params = {
        "apiKey": API_KEY,
        "regions": REGION,
        "markets": MARKET,
        "oddsFormat": "decimal",
        "dateFormat": "iso",
    }
    url = BASE.format(sport=sport_key)
    r = requests.get(url, params=params, timeout=20)
    if r.status_code == 422:
        return []
    r.raise_for_status()
    return r.json()

def flatten(events, timestamp):
    rows = []
    for ev in events:
        home = ev.get("home_team")
        away = ev.get("away_team")
        starts = ev.get("commence_time")
        for bk in ev.get("bookmakers", []):
            for mkt in bk.get("markets", []):
                if mkt.get("key") != "h2h":
                    continue
                for out in mkt.get("outcomes", []):
                    rows.append({
                        "liga": ev.get("sport_title"),
                        "fecha": starts,
                        "mercado": mkt.get("key"),
                        "casa": bk.get("title"),
                        "local": home,
                        "visitante": away,
                        "seleccion": out.get("name"),
                        "cuota": out.get("price"),
                        "timestamp": timestamp
                    })
    return rows

def recolectar_datos():
    all_rows = []
    now = datetime.now().isoformat()
    for sport in SPORTS:
        try:
            events = fetch_odds(sport)
            if events:
                all_rows.extend(flatten(events, now))
            time.sleep(0.3)
        except Exception as e:
            print(f"❌ Error con {sport}: {e}")
    return pd.DataFrame(all_rows)

def generar_csv(df: pd.DataFrame) -> bytes:
    buffer = StringIO()
    df.to_csv(buffer, index=False, encoding="utf-8-sig")
    return buffer.getvalue().encode("utf-8-sig")
