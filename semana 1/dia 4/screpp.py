import requests
from bs4 import BeautifulSoup

req = requests.get('https://sonemas.pe/sonemas')

status_code = req.status_code
if status_code == 200:
    print("acceso a la pagina exitoso")
    html = BeautifulSoup(req.text,"html.parser")
    # print(html)
    """

    """

    # producto = html.find('div', {'id':'txtHint'})
    nombres = html.find('div', {'class':'ficha_producto'})
    # nombres= producto.find('div', {'class' :'fp_descripcion'})
    print(nombres)
#     for c in range(6):
#         dolar = tabla.find('tr',{'id':'ctl00_cphContent_rgTipoCambio_ctl00__' + str(c)})
#         # print(dolar)
#         lstTipoCambioDolar = dolar.find_all('td')
#         strNombreMoneda = lstTipoCambioDolar[0].text
#         strValorCompra = lstTipoCambioDolar[1].text
#         strValorVenta = lstTipoCambioDolar[2].text
#         print(strNombreMoneda + "|" + strValorCompra + "|" + strValorVenta)

# else:
#     print("error al acceder a la pagina: " + str(status_code))

# #PARA GUARDARLO EN UN NUEVO ARCHIVO TXT, QUE SE CREE AUTOMATICAMENTE:
# f = open('cambio.txt', 'a')
# f.write(strNombreMoneda + "|" + strValorCompra + "|" + strValorVenta)
# f.close()