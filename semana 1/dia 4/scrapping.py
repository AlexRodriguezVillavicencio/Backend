import requests
from bs4 import BeautifulSoup
# https://www.sbs.gob.pe/robots.txt
# con robots.txt puedo saber que scrapear y que no
#https://www.sbs.gob.pe/app/pp/sistip_portal/paginas/publicacion/tipocambiopromedio.aspx

req = requests.get('https://www.sbs.gob.pe/app/pp/sistip_portal/paginas/publicacion/tipocambiopromedio.aspx')

status_code = req.status_code
if status_code == 200:
    print("acceso a la pagina exitoso")
    html = BeautifulSoup(req.text,"html.parser")
    # print(html)
    """
    <table class="rgMasterTable" border="0" id="ctl00_cphContent_rgTipoCambio_ctl00" style="width:100%;table-layout:auto;empty-cells:show;">
			<colgroup>
		<col>
		<col>
		<col>
	</colgroup>
<thead>
				<tr>
					<th scope="col" class="rgHeader APLI_fila1" style="font-weight:bold;text-align:center;">MONEDA</th><th scope="col" class="rgHeader APLI_fila1" style="font-weight:bold;text-align:center;">COMPRA (S/)</th><th scope="col" class="rgHeader APLI_fila1" style="font-weight:bold;text-align:center;">VENTA (S/)</th>
				</tr>
			</thead><tbody>
			<tr class="rgRow" id="ctl00_cphContent_rgTipoCambio_ctl00__0">
				<td class="APLI_fila3" style="width:40%;">Dólar de N.A.</td><td class="APLI_fila2" style="width:30%;">3.936</td><td class="APLI_fila2" style="width:30%;">3.944</td>
			</tr><tr class="rgAltRow" id="ctl00_cphContent_rgTipoCambio_ctl00__1">
				<td class="APLI_fila3" style="width:40%;">Peso Colombiano</td><td class="APLI_fila2" style="width:30%;">0.001</td><td class="APLI_fila2" style="width:30%;">0.001</td>
			</tr><tr class="rgRow" id="ctl00_cphContent_rgTipoCambio_ctl00__2">
				<td class="APLI_fila3" style="width:40%;">Libra Esterlina</td><td class="APLI_fila2" style="width:30%;">5.427</td><td class="APLI_fila2" style="width:30%;">5.471</td>
			</tr><tr class="rgAltRow" id="ctl00_cphContent_rgTipoCambio_ctl00__3">
				<td class="APLI_fila3" style="width:40%;">Peso Mexicano</td><td class="APLI_fila2" style="width:30%;">&nbsp;</td><td class="APLI_fila2" style="width:30%;">0.227</td>
			</tr><tr class="rgRow" id="ctl00_cphContent_rgTipoCambio_ctl00__4">
				<td class="APLI_fila3" style="width:40%;">Franco Suizo</td><td class="APLI_fila2" style="width:30%;">4.290</td><td class="APLI_fila2" style="width:30%;">4.290</td>
			</tr><tr class="rgAltRow" id="ctl00_cphContent_rgTipoCambio_ctl00__5">
				<td class="APLI_fila3" style="width:40%;">Euro</td><td class="APLI_fila2" style="width:30%;">4.535</td><td class="APLI_fila2" style="width:30%;">4.941</td>
			</tr>
			</tbody>

		</table>
    """
    tabla = html.find('table', {'class':'rgMasterTable'})
    # print(tabla)
    for c in range(6):
        dolar = tabla.find('tr',{'id':'ctl00_cphContent_rgTipoCambio_ctl00__' + str(c)})
        # print(dolar)
        lstTipoCambioDolar = dolar.find_all('td')
        strNombreMoneda = lstTipoCambioDolar[0].text
        strValorCompra = lstTipoCambioDolar[1].text
        strValorVenta = lstTipoCambioDolar[2].text
        print(strNombreMoneda + "|" + strValorCompra + "|" + strValorVenta)

else:
    print("error al acceder a la pagina: " + str(status_code))

#PARA GUARDARLO EN UN NUEVO ARCHIVO TXT, QUE SE CREE AUTOMATICAMENTE:
f = open('cambio.txt', 'a')
f.write(strNombreMoneda + "|" + strValorCompra + "|" + strValorVenta)
f.close()