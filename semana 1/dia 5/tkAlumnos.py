from tkinter import *
from tkinter.ttk import Treeview
import sqlite3

# para nuestra base d eatos vamos a desacargar sqlite administrador:
#http://sqliteadmin.orbmu2k.de/

class Alumno:

    db_name = 'database.s3db'

    #creamos para la base de datos
    def ejecutarSql(self,sql,parametros = ()):
        with sqlite3.connect(self.db_name) as conn:
            #aqui agreagamos conusltas
            cursor = conn.cursor()
            resultado = cursor.execute(sql,parametros)
            conn.commit()
        return resultado

    def readAlumnos (self):
        rsAlumnos = self.trvAlumnos.get_children()
        #limpiando la tabla
        for element in rsAlumnos:
            self.trvAlumnos.delete(element)

        sqlAlumnos = 'SELECT * FROM ALUMNOS'
        resultado  = self.ejecutarSql(sqlAlumnos)
        for fila in resultado:
            self.trvAlumnos.insert('',0,text= fila[0],values= fila[1])

    def createAlumno(self):
        sqlInsertAlumno = "insert into alumnos values(?,?)"
        #creando la tupla
        parametros = (self.nombre.get(),self.email.get())
        self.ejecutarSql(sqlInsertAlumno,parametros)
        self.readAlumnos()

    def __init__(self,window):
        self.wind = window
        self.wind.title('Alumnos')

                
        #CREAMOS UN FRAME
        frame = LabelFrame(window,text = "Registro de nuevo Alumno")
        frame.grid(row=0, column=0,columnspan=3,pady=20)

        #CAMPOS DEL FORMULARIOS
        #creamos label para nombre
        lbNombre = Label(frame,text = 'Nombre : ')
        lbNombre.grid(row=1,column=0)
        #textfiled para caja de textp añumno y alo asignamos al atributo nombre del alumno
        self.nombre = Entry(frame)
        self.nombre.grid(row=1,column=1)
        #
        lbEmail = Label(frame,text = 'Email : ')
        lbEmail.grid(row=2,column=0)
        self.email = Entry(frame)
        self.email.grid(row=2,column=1)
        

        #coton para crear neuvo alumno
        btnNuevoAlumno = Button(frame,text = 'Registrar Alumno',command=self.createAlumno)
        btnNuevoAlumno.grid(row=4,columnspan=2,sticky= W + E)


        self.trvAlumnos = Treeview(height=10,columns=2)
        self.trvAlumnos.grid(row=5,column=0,columnspan=2)
        self.trvAlumnos.heading('#0',text='Nombre',anchor=CENTER)
        self.trvAlumnos.heading('#1',text='Email',anchor=CENTER)
        
        
        self.readAlumnos()


window = Tk()
app = Alumno(window)
window.mainloop()

