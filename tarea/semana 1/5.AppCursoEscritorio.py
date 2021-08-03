from tkinter import *
from tkinter.ttk import Treeview
import sqlite3

class curso:

    db_name = 'db_cursosEscritotio.s3db'

    def ejecutarSql(self,sql,parametros = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            resultado = cursor.execute(sql,parametros)
            conn.commit()
        return resultado

    def readCursos(self):
        rsCursos = self.trvCursos.get_children()
        for element in rsCursos:
            self.trvCursos.delete(element)

        sqlCursos = 'SELECT * FROM CURSOS'
        resultado = self.ejecutarSql(sqlCursos)
        for fila in resultado:
            self.trvCursos.insert('',0, text=fila[0], values=(fila[1],fila[2]))

    def createCurso(self):
        sqlInsertCurso = 'insert into cursos values(?,?)'
        parametros = (self.id.get(), self.curso.get(),self.nota.get())
        self.ejecutarSql(sqlInsertCurso,parametros)
        self.readCursos()


    def __init__(self,window):
        self.window = window
        self.window.title('Lenguajes de Programación')

        frame = LabelFrame(window,text = "Registro de notas por curso")
        frame.grid(row=0, column=0, columnspan=3,pady=10)

        Label(frame, text='id: ').grid(row=1,column=0)
        Entry(frame).grid(row=1,column=1)
        Label(frame, text='curso: ').grid(row=2,column=0)
        Entry(frame).grid(row=2,column=1)
        Label(frame, text='nota: ').grid(row=3,column=0)
        Entry(frame).grid(row=3,column=1)

        Button(frame,text='registrar',command=self.createCurso).grid(row=4,columnspan=2,sticky= W + E)

        self.trvCursos = Treeview(height=10,columns=('#1','#2'))
        self.trvCursos.grid(row=5,column=0)
        # self.trvCursos['show'] = 'headings'
        self.trvCursos.heading('#0',text='id', anchor=CENTER)
        self.trvCursos.heading('#1',text='curso', anchor=CENTER)
        self.trvCursos.heading('#2',text='nota', anchor=CENTER)

        self.readCursos()

window = Tk()
app= curso(window)
window.mainloop()
