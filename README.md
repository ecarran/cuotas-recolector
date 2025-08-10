# Cuotas Recolector (en memoria) - Versión Corregida

Servicio en FastAPI que recolecta cuotas en memoria desde The Odds API.

## Endpoints

- `/` → mantiene vivo el servicio
- `/healthz` → útil para cron-jobs sin consumir cuota
- `/recolectar` → añade cuotas con timestamp al acumulador en RAM
- `/descargar-csv` → descarga el CSV completo acumulado

Ideal para usar con Render + GitHub Actions