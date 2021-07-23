# list= ['html','css','java','django']
# tuple= ('html','css','java','django')
# set= {'html','css','java','django'}
# dict= {'h1':'html','h2':'css','h3':'java','h4':'django'}
# dicta= [{'nombre': 'q', 'email': 'w', 'celular': 'e'}, {'nombre': 'f', 'email': 'g', 'celular': 'h'}]

# # for i in range(len(list)):
# #     print(list[i])

# print(dicta)
# del dicta[1]
# print(dicta)



#PROGRAMA PARA GESTION DE ALUMUNOS
#CRUD: CREATE, READ, UPDATE, DELETE
#DEFINIR VARIABLES DE ENTRADA Y SALIDA
alumnos = []
alumno = {}
salir = 100

#LOGICA

#con def se crean las funciones
def createAlumno(nombre, email, celular):
    nuevoAlumno = {
        'nombre':nombre,
        'email':email,
        'celular':celular
    }
    alumnos.append(nuevoAlumno)
    return 1
    
def readAlumno():
    # pass
    print('Listado de alumnos')
    for a in alumnos:
        print('=========================')
        for clave, valor in a.items():
            print(clave + ":" +  valor)
            
            
def updateAlumno(nombre):
    # pass    
    encontrado=False
    ok = 1
    posicion=-1;
    
    for posArrary in range(len(alumnos)):
        nvoObj = alumnos[posArrary]
        for clave,valor in nvoObj.items():
            if valor==nombre:            
                encontrado=True
                posicion = posArrary;
                break;
    
    if encontrado == True:
        nombre = input("Nombre : ")
        email = input("Email : ")
        celular = input("Celular : ")
        
        alumnos[posicion]['nombre']=nombre 
        alumnos[posicion]['email']=email    
        alumnos[posicion]['celular']=celular   
        
    else:
        ok = 0;
        
    return ok;
  
    
     

def deleteAlumno(nombre):
    # pass
    encontrado=False
    ok = 1
    posicion=-1;
    
    for posArrary in range(len(alumnos)):
        nvoObj = alumnos[posArrary]
        for clave,valor in nvoObj.items():
            if valor==nombre:            
                encontrado=True
                posicion = posArrary;
                break;
    
    if encontrado == True:
        del alumnos[posicion]         
    else:
        ok = 0;
    return ok;   
            
        
    

def menu():

    print('1: REGISTRAR')
    print('2: MOSTRAR')
    print('3: ACTUALIZAR')
    print('4: ELIMINAR')
    print('0: SALIR\n')
    
    
    opcion = input('DIGITE SU OPCIÓN: ')
    return opcion


while(salir > 0):
    opcion = int(menu())
    
    if(opcion == 0):
        salir = opcion
        
    elif(opcion == 1): 
        nombre = input("Nombre : ")
        email = input("Email : ")
        celular = input("Celular : ")
        r = createAlumno(nombre, email, celular)
        if(r==1):
            print('\nRegistro Exitoso')
       
    elif(opcion == 2):
        readAlumno()
        
    elif(opcion == 3):
        nombre = input('Ingrese el nombre: ')
        result = updateAlumno(nombre)
        if(result == 1):
            print('\nRegistro Actualizado')
        else:
            print('\nNo se encontró el registro')
            

    elif(opcion == 4):
        result = deleteAlumno(nombre)
        if(result == 1):
            print('\nRegistro eliminado')
        else:
            print('\nNo se encontró el registro')
        
    else:
        print('\nMarcó un opcion incorrecta')
        continue
    
      
    
    if(opcion>0):
        print('\n1: Volver al menú  0: Salir del sistema ')
        salir = int(input())

#Mostrar resultados