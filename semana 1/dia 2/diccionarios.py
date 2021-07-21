#MANEJO DE DICCIONARIOS
capitales = {'peru':'lima','ecuador':'quito','chile':'santiago'}
print(capitales)
capital = {'usa':'washinton'}
capitales.update(capital)
print(capitales)

alumnos = {
    'name':'alex',
    'email':'example@email.com',
    'celphone': '919191192'
}

print(alumnos['email'])
alumnoModelo = alumnos.copy()
alumnos['email'] = 'email@email.pe'
print(alumnos['email'])
print(alumnoModelo)
#alumnos.pop('celphone')
#print(alumnos)
#alumnos.clear() o alumnos = {} , para eliminar
a = alumnos.pop('dni', 'no existe dni')
print(a)
print(alumnos.key())
print(alumnos.values())

#DIFERENTES FROMAS DE RECORRER UN ARREGLO
for clave in alumnos:
    print(clave,alumnos[clave])

for clave in alumnos.keys:
    print(clave,alumnos[clave])

for clave,valor in alumnos.items():
    print(clave,valor)