class clsPersona:

    def __init__(self,nom,ema,cel):
        self.nombre = nom
        self.email = ema
        self.celular = cel

    def registrase():
        pass

class clsUsuario:
    def __init__(self,user,password):
        self.nombreUsuario = user
        self.password = password    

    def login():
        pass


class clsProfesor(clsPersona,clsUsuario):

    def __init__(self,nom,ema,cel,esp,u,p):
        clsPersona.__init__(self,nom,ema,cel)
        clsUsuario.__init__(self,u,p)
        self.especialidad = esp

    def calificar(self):
        pass



class clsAlumno:

    def __init__(self,nom,ema,cel):
        self.nombre = nom
        self.email = ema
        self.celular = cel

    def enviarEjercicios():
        pass

class clsCurso:

    def __init__(self,cod,nom,nota):
        self.codigo = cod
        self.nombre = nom
        self.nota = nota



    #CREAR UN SISTEMA DE CURSOS, AGREGAR CURSOS, MOSTRAR CURSOS... CRUD:: OYTHON REACT ETC.
    