# pum-datos

Datos públicos que lee el sitio de PUM!.

- `cetes.json`: tasa de CETES a 28 días (anual, %) y fecha de la subasta. La usa el simulador de ahorro para el retiro en el Marketplace. Se actualiza cada miércoles.

El sitio lee el archivo desde `https://raw.githubusercontent.com/PUMSolutions/pum-datos/main/cetes.json`. Si no puede leerlo, usa la tasa que trae incluida.
