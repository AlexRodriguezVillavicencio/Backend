from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
import sqlite3
import tkinter as tk

class curso:

    db_name = 'db_cursosEscritotio.s3db'

    def ejecutarSql(self,sql,parametros = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            resultado = cursor.execute(sql,parametros)
            conn.commit()
        return resultado
#obtencion de datos registrados anteriormente
    def readCursos(self):   
        rsCursos = self.trvCursos.get_children()
        for e in rsCursos:
            self.trvCursos.delete(e)
        sqlCursos = "select * from cursos"
        resultado = self.ejecutarSql(sqlCursos)
        for fila in resultado:
            self.trvCursos.insert('',0, text=fila[0], values=(fila[1],fila[2]))
#validacion de los campos para guadrarlos en la base de datos
    def validacion(self):
        return len(self.curso.get()) != 0  and len(self.nota.get()) != 0
#agregando nuevos cursos
    def createCurso(self):
        if self.validacion():
            sqlInsertCurso = 'insert into cursos values(?,?,?)'
            parametros = (self.id.get(), self.curso.get(),self.nota.get())
            self.ejecutarSql(sqlInsertCurso,parametros)
            self.mensajePop['text'] = 'Registro exitoso'
            self.readCursos()
        else:
            self.mensajePop['text'] = 'Llene todos los campos'
#eliminando cursos
    def eliminarCurso(self):
        self.mensajePop['text'] = ''
        try:
            self.trvCursos.item(self.trvCursos.selection())['text']
        except IndexError as e:
            self.mensajePop['text'] = 'selecciona un registro'
            return
        curso = self.trvCursos.item(self.trvCursos.selection())['text']
        sqlCursos = 'DELETE FROM cursos WHERE id = ?'
        self.createCurso(sqlCursos,(id,))
        self.mensajePop['text'] = 'Curso eliminado satisfactoriamente'
        self.readCursos()



    def __init__(self,window):
        self.wind = window
        self.wind.title('Lenguajes de Programación')

        frame = LabelFrame(self.wind,text = "Registro de notas por curso")
        frame.grid(row=0, column=0, columnspan=3,pady=10)
#creando etiquetas para llenado
        Label(frame, text='id: ').grid(row=1,column=0)
        self.id = Entry(frame)
        self.id.grid(row=1,column=1)
        Label(frame, text='curso: ').grid(row=2,column=0)
        self.curso = Entry(frame)
        self.curso.grid(row=2,column=1)
        Label(frame, text='nota: ').grid(row=3,column=0)
        self.nota = Entry(frame)
        self.nota.grid(row=3,column=1)
        #creación de botones
        tk.Button(frame,text='registrar',command=self.createCurso, bg = 'green',fg='white').grid(row=4,columnspan=2,sticky= W + E)
        tk.Button(frame,text='editar',command=self.createCurso, bg='yellow').grid(row=5,column=0,sticky= W + E)
        tk.Button(frame,text='eliminar',command=self.eliminarCurso,bg='red',fg='white').grid(row=5,column=1,sticky= W + E)
        #mensajes saltones
        self.mensajePop = Label(text='',fg='red' , bg= '#000')
        self.mensajePop.grid(row=4, column=0,columnspan=3,sticky=W+E)

        self.trvCursos = Treeview(height=10,columns=('#1','#2'))
        self.trvCursos.grid(row=5,column=0)
        # self.trvCursos['show'] = 'headings'
        self.trvCursos.heading('#0',text='id', anchor=CENTER)
        self.trvCursos.heading('#1',text='curso', anchor=CENTER)
        self.trvCursos.heading('#2',text='nota', anchor=CENTER)

        self.readCursos()

window = Tk()
app = curso(window)
window.mainloop()