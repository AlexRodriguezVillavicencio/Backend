'''PRGRAMA PARA GESTION DE ALUMNOS'''
#CRUD: CREATE, READ, IPDATE, DELETE
#DEFINIR VARIABLE DE ENTRADA Y DE SALIDA
alumnos = []
alumno = {}
salir = 'no'

#LOGICA

def createAlumno(nombre,email,celular):
    nuevoAlumno = {
            'nombre': nombre,
            'email': email,
            'celular': celular
        }
    alumnos.append(nuevoAlumno)
    return 1

def readAlumno():
    print("listado de alumnos")
    for a in alumnos:
        print("======================")
        for clave,valor in a.items():
            print(clave + ": " + valor)


while(salir == 'no'):
    print("OPCIONES: 1 - registar alumnos  2 - mostrar alumnos")
    opcion = input()
    if(opcion == "1"):
        print("registro de nuevo alumno: ")
        nombre = input("nombre: ")
        email = input("email: ")
        celular = input("celular: ")
        r = createAlumno(nombre,email,celular)
        if r == 1:
            print("registro exitoso")
    elif(opcion == "2"):
        readAlumno()
    else:
        print("marco una opcion incorrecta")
        continue
    print("desea salir del porgrama?")
    salir = input()
#MOSTRAR RESULTADOS