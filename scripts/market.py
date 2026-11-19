"""Descarga precio y market cap de RLUSD y XRP desde CoinGecko y escribe market.json y market.js."""
import json, sys, time, urllib.request
from datetime import datetime, timezone

URL = ("https://api.coingecko.com/api/v3/simple/price"
       "?ids=ripple-usd,ripple&vs_currencies=usd&include_market_cap=true&include_24hr_change=true")

def get():
    for i in range(3):
        try:
            req = urllib.request.Request(URL, headers={"accept": "application/json", "user-agent": "pum-datos/1.0"})
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.load(r)
        except Exception as e:
            print("intento", i + 1, "falló:", e, file=sys.stderr)
            time.sleep(10 * (i + 1))
    sys.exit(1)

j = get()
r, x = j.get("ripple-usd", {}), j.get("ripple", {})
d = {
    "rlusd_mcap": r.get("usd_market_cap"),
    "rlusd_price": r.get("usd"),
    "xrp_price": x.get("usd"),
    "xrp_mcap": x.get("usd_market_cap"),
    "xrp_change_24h": x.get("usd_24h_change"),
    "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "source": "CoinGecko",
}
if not d["rlusd_mcap"] or not (1e9 < d["rlusd_mcap"] < 2e10) or not d["xrp_price"] or not (0.05 < d["xrp_price"] < 50):
    print("datos fuera de rango, no escribo:", d, file=sys.stderr)
    sys.exit(1)
open("market.json", "w").write(json.dumps(d, indent=2) + "\n")
open("market.js", "w").write("window.__PUM_MARKET=" + json.dumps(d) + ";window.dispatchEvent(new Event('pum-market'));\n")
print(d)
