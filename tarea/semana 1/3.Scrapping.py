import requests
from bs4 import BeautifulSoup
from os import system
# https://www.sbs.gob.pe/robots.txt
# con robots.txt puedo saber que scrapear y que no
#https://www.sbs.gob.pe/app/pp/sistip_portal/paginas/publicacion/tipocambiopromedio.aspx
system('cls')
print("="*60)
print("="*22 + "CAMBIO DE MONEDAS" + "="*21)
print("="*60)
print("El cambio para hoy es:\n")

salir = "0"

#LOGICA
req = requests.get('https://www.sbs.gob.pe/app/pp/sistip_portal/paginas/publicacion/tipocambiopromedio.aspx')

status_code = req.status_code
if status_code == 200:
    # print("acceso a la pagina exitoso")
    html = BeautifulSoup(req.text,"html.parser")


    tabla = html.find('table', {'class':'rgMasterTable'})
    # print(tabla)
    for c in range(6):
        dolar = tabla.find('tr',{'id':'ctl00_cphContent_rgTipoCambio_ctl00__' + str(c)})
        # print(dolar)
        lstTipoCambioDolar = dolar.find_all('td')
        strNombreMoneda = lstTipoCambioDolar[0].text
        strValorCompra = lstTipoCambioDolar[1].text
        strValorVenta = lstTipoCambioDolar[2].text
        print("MONEDA       |  COMPRA  |  VENTA")
        print(strNombreMoneda + " | " + strValorCompra + " |  " + strValorVenta)
        print("="*60)

else:
    print("error al acceder a la pagina: " + str(status_code))

#PARA GUARDARLO EN UN NUEVO ARCHIVO TXT, QUE SE CREE AUTOMATICAMENTE:
f = open('cambio.txt', 'a')
f.write(strNombreMoneda + "|" + strValorCompra + "|" + strValorVenta)
f.close()


#Resultados
while(salir == "0"):
    print("[1] Deseo comprar     [2] Deseo vender      [0] Salir")
    opcion = input(" ")
    if opcion == "1":
        system('cls')
        print("="*60)
        print("="*27 + "COMPRA" + "="*27)
        print("="*60)
        monto = float(input("ingrese el monto en soles: "))
        for c in range(6):
            dolar = tabla.find('tr',{'id':'ctl00_cphContent_rgTipoCambio_ctl00__' + str(c)})
            lstTipoCambioDolar = dolar.find_all('td')
            strNombreMoneda = lstTipoCambioDolar[0].text
            strValorVenta = float(lstTipoCambioDolar[2].text)
            resultado = float(monto/strValorCompra)
            print('Por',monto,'soles usted recibirá ', resultado, strNombreMoneda)

    if opcion == "2":
        system('cls')
        print("="*60)
        print("="*22 + "VENTA" + "="*21)
        print("="*60)
        monto = float(input("ingrese el monto en moneda extranjera: "))
        for c in range(6):
            dolar = tabla.find('tr',{'id':'ctl00_cphContent_rgTipoCambio_ctl00__' + str(c)})
            lstTipoCambioDolar = dolar.find_all('td')
            strNombreMoneda = lstTipoCambioDolar[0].text
            strValorCompra = float(lstTipoCambioDolar[1].text)
            resultado = float(monto*strValorCompra)
            print(monto,strNombreMoneda," equivalen a: ", resultado, "soles")
    if opcion == "0":
        break