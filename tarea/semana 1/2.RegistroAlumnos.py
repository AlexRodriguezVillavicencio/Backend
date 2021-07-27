'''PRGRAMA PARA GESTION DE ALUMNOS'''
#CRUD: CREATE, READ, IPDATE, DELETE
print('***************************************************************')
print('**********************REGISTRO DE ALUMNOS**********************')
print('***************************************************************')
print('OPCIONES:')
print('{1} CONSULTAR ALUMNOS')
print('{2} REGISTRAR ALUMNO')
print('{3} ACTUALIZAR ALUMNO')
print('{4} ELIMINAR ALUMNO')
#DEFINIR VARIABLE DE ENTRADA Y DE SALIDA
alumnos = []
alumno = {}
salir = 'no'
#LOGICA
def readAlumno(alumnos):
    print("\nLISTADO DE ALUMNOS:")
    for a in alumnos:
        print("======================")
        for clave,valor in a.items():
            print(clave + ": " + valor)

def createAlumno(nombre,email,celular):
    nuevoAlumno = {
            'nombre': nombre,
            'email': email,
            'celular': celular
        }
    alumnos.append(nuevoAlumno)
    return 1

def updateAlumno(alumnos):
    print(" ACTUALIZAR ALUMNO ")
    posAlumno = -1
    alumnoBusqueda = input("INGRESE EL NOMBRE DEL ALUMNO :")
    for i in range(len(alumnos)):
        a = alumnos[i]
        for clave,valor in a.items():
            if valor == alumnoBusqueda:
                print(a)
                posAlumno = i
                print("posición del alumno:" + str(posAlumno))
                break
    print("ACTUALIZANDO DATOS DEL ALUMNO:")
    nombre = input("NOMBRE : ")
    email = input("EMAIL : ")
    celular = input("CELULAR : ")
    actAlumno =  {
            'nombre': nombre,
            'email': email,
            'celular': celular
        }
    del alumnos[posAlumno]
    alumnos.insert(posAlumno,actAlumno)

def deleteAlumno(alumnos):
    print(" ELIMINAR ALUMNO ")
    posAlumno = -1
    alumnoBusqueda = input("INGRESE EL NOMBRE DEL ALUMNO :")
    for i in range(len(alumnos)):
        a = alumnos[i]
        for clave ,valor in a.items():
            if valor == alumnoBusqueda:
                print(a)
                posAlumno = i
                print("------Eliminado con Exito------")
                break
    del alumnos[posAlumno]

    

#MOSTRAR RESULTADOS
while(salir == 'no'):
    opcion = input("\nIngrese su opción: ")
    if(opcion == "1"):
        readAlumno(alumnos)
        print("=" * 22)

    elif(opcion == "2"):
        nombre = input("nombre: ")
        email = input("email: ")
        celular = input("celular: ")
        r = createAlumno(nombre,email,celular)
        if r == 1:
            print("---------!registro exitoso!-------------")

    elif(opcion == "3"):
        updateAlumno(alumnos)

    elif(opcion == "4"):
        deleteAlumno(alumnos)

    else:
        print("marco una opcion incorrecta")
        continue
    print("desea salir del programa?")
    salir = input()
