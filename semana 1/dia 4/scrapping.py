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