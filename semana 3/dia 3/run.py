from flask import Flask, json,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


#app es el corazón 
app = Flask(__name__)
#conectando el ORM a la base de datos
#  app.config['SQLALCHEMY_DATABASE_URI']='mysql+libreriamysql://user:pass:@localhost/bdname
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flaskapi'
#por defecto
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

#******************CLASES PARA BD****************++

class Alumno(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(100))
    email = db.Column(db.String(100),unique=True)
    
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email

db.create_all()

class AlumnosSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','email')

alumno_schema = AlumnosSchema()
alumnos_schema = AlumnosSchema(many=True)

#**************para registrar******
#creamos una neuva ruta
@app.route('/setAlumno',methods=['POST'])
def setAlumno():
    nombre = request.json['nombre']
    email = request.json['email']

    #equivalente a insert into alumno 
    nuevoAlumno = Alumno(nombre,email)
    db.session.add(nuevoAlumno)
    db.session.commit()

    return alumno_schema.jsonify(nuevoAlumno)

#creo otra ruta
@app.route('/alumnos',methods=['GET'])
def getAlumnos():
    listadoAlumnos = Alumno.query.all()  #SELECT * FROM ALUMNOS
    dataALumnos = alumnos_schema.dump(listadoAlumnos)
    
    return jsonify(dataALumnos)

#ruta para metodo actualizar
@app.route('/updateAlumno/<id>',methods=['PUT'])
def updateAlumno(id):
    alumno = Alumno.query.get(id)  # select * from alumno where  id=
    
    nombre = request.json['nombre']
    email = request.json['email']
    #update alumno set
    alumno.nombre =nombre
    alumno.email = email

    db.session.commit()

    return alumno_schema.jsonify(alumno)

#ruta para elimnar alumno
@app.route('/deleteAlumno/<id>',methods=['DELETE'])
def deleteAlumno(id):
    alumno = Alumno.query.get(id) 
    #delete from where id=
    db.session.delete(alumno)
    db.session.commit()



@app.route('/')
def index():
    return jsonify({'mensaje':'Bienvenido a mi API'})

if __name__ == "__main__":
    app.run(debug=True)