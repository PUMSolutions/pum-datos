# pum-datos

Datos públicos que lee el sitio de PUM!.

- `cetes.json`: tasa de CETES a 28 días (anual, %) y fecha de la subasta. La usa el simulador de ahorro para el retiro en el Marketplace. Se actualiza cada miércoles.

El sitio lee el archivo desde `https://raw.githubusercontent.com/PUMSolutions/pum-datos/main/cetes.json`. Si no puede leerlo, usa la tasa que trae incluida.
- `market.json` y `market.js`: market cap de RLUSD y precio y market cap de XRP, de CoinGecko. Una GitHub Action los actualiza cada 10 minutos. Los lee el one pager de Ripple Treasury desde `https://cdn.jsdelivr.net/gh/PUMSolutions/pum-datos@main/market.js`.
