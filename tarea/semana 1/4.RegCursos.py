from os import system
#REGUSTRO DE CURSOS , CRUD , CODIGO, CURSO, NOTAS
def menu():
    system('cls')
    print("="*60)
    print("="*15 + "REGISTRO DE NOTAS DE CURSOS" + "="*18)
    print("="*60)
    print("Opciones:")
    print("     [1] Consulta")
    print("     [2] Registro")
    print("     [3] Actualizar")
    print("     [4] Eliminar")
    print("     [0] Salir")
    print("="*60)
    opcion = input("Ingrese el número de la acción que desea realizar: ")
    return opcion
   
#DEFINIR VARIABLE DE ENTRADA Y SALIDA
cursos = []
salir = "0"
#LOGICA
def consulta():
    for a in cursos:
        for clave, valor in a.items():
            print(clave +":"+ valor)
        print("="*20)

def registro(id,nom,nota):
    nuevoCurso = {
        'código' : id,
        'nombre' : nom,
        'calificación' : nota
    }
    cursos.append(nuevoCurso)



def actualizar():
    system('cls')
    print("="*60)
    print("="*21 + "ACTUALIZANDO DATOS" + "="*21)
    print("="*60)
    cursoActualizado = input("Ingrese el curso a actualizar: ")
    for i in range(len(cursos)):
        a = cursos[i]
        for clave,valor in a.items():
            if valor == cursoActualizado:
                print(a)
                posCurso = i
                break
    print("Actualizando datos:")
    id = input("Código: ")
    nom = input("Nombre del curso: ")
    nota = input("Calificación: ")    
    nuevoCurso = {
        'código' : id,
        'nombre' : nom,
        'calificación' : nota
    }
    del cursos[posCurso]
    cursos.insert(posCurso,nuevoCurso)

def eliminar():
    system('cls')
    print("="*60)
    print("="*13 + "ELIMINACIÓN DE REGISTROS GUARDADOS" + "="*13)
    print("="*60)
    eliminar = input("Ingrese el curso a eliminar: ")
    for i in range(len(cursos)):
        a = cursos[i]
        for clave, valor in a.items():
            if valor == eliminar:
                posCurso = i
                print(a)
                break
    print("\n---------------Curso Eliminado---------------")
    del cursos[posCurso]

        

#RESULTADO
while(salir == "0"): 
    opcion = menu()


    if opcion == "1":
        system('cls')
        print("="*60)
        print("="*20 + "RESULTADO DE BUSQUEDA" + "="*19)
        print("="*60)
        consulta()
        print("Pulsa enter para regresar al menú") 
        input("") 


    if opcion == "2":
        system('cls')
        print("="*60)
        print("="*23 + "NUEVO REGISTRO" + "="*23)
        print("="*60)
        print("Registrando nuevo alumno:")
        id = input("Código: ")
        nom = input("Nombre del curso: ")
        nota = input("Calificación: ")
        r = registro(id,nom,nota)
        if r == 1:
            print("---------!registro exitoso!-------------")
        while(salir == "0"):
            print("\nContinuar:  ¿si?        ¿no?")
            op = input(" ")
            if (op == "si"):
                system('cls')
                print("="*60)
                print("="*23 + "NUEVO REGISTRO" + "="*23)
                print("="*60)
                print("Registrando nuevo alumno:")
                id = input("Código: ")
                nom = input("Nombre del curso: ")
                nota = input("Calificación: ")
                r = registro(id,nom,nota)
                if r == 1:
                    print("---------!registro exitoso!-------------")
            if (op == "no"):
                break 


    if opcion == "3":
        actualizar()
        while(salir == "0"):
            print("\nContinuar:  ¿si?        ¿no?")
            op = input("")
            if (op == "si"):
                actualizar()
            if (op == "no"):
                break


    if opcion == "4":
        eliminar()
        while(salir == "0"):
            print("\nContinuar:  ¿si?        ¿no?")
            op = input("")
            if (op == "si"):
                eliminar()
            if (op == "no"):
                break


    if opcion == "0":
        break
