
from flask import Flask
from flask import jsonify

import pymysql
app = Flask(__name__)
# Parametros para la conexion
def conexion():
    return pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='dbdesire')

# Definir funciones para las consultas
#Usuarios
def obtener_usuarios():
    try:
        conn = conexion()
        datos = []
        respuesta = []
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM usuarios where estado = 1")
            datos = cursor.fetchall()
            for fila in datos:
                item={'id':fila[0],'usuario':fila[1],'nombres':fila[3],'apellidos':fila[4],'correo':fila[5],'telefono':fila[6],'rol':fila[7]}
                respuesta.append(item)
        conn.close()
        return jsonify({'msj': respuesta})
    except:
        return jsonify({'msj': 'Error en la bd'})

def obtener_usuario(idUsuario):
    try:
        conn = conexion()
        datos = []
        respuesta = []
        with conn.cursor() as cursor:
            sql = "SELECT * FROM usuarios where id = '{0}'".format(idUsuario)
            cursor.execute(sql)
            datos = cursor.fetchall()          
            for fila in datos:
                item={'id':fila[0],'usuario':fila[1],'nombres':fila[3],'apellidos':fila[4],'correo':fila[5],'telefono':fila[6],'rol':fila[7]}
                respuesta.append(item)
        conn.close()
        return jsonify({'msj': respuesta})
    except:
        return jsonify({'msj': 'Error en la bd'})
def doble_usuario(usuario):
    try:
        conn = conexion()
        datos = []
        with conn.cursor() as cursor:
            sql = "SELECT * FROM usuarios where usuario = '{0}'".format(usuario)
            cursor.execute(sql)
            datos = cursor.fetchall()          
            if not len(datos) == 0:
                conn.close()
                return {"duplicado" : True, "msj": "El usuario ya fue registrado"}
            else:
                conn.close()
                return {"duplicado" : False, "msj": "Usuario disponible"}     
    except:
        return jsonify({'msj': 'Error en la bd'})
def doble_correo(correo):
    try:
        conn = conexion()
        datos = []
        with conn.cursor() as cursor:
            sql = "SELECT * FROM usuarios where correo = '{0}'".format(correo)
            cursor.execute(sql)
            datos = cursor.fetchall()          
            if not len(datos) == 0:
                conn.close()
                return {"duplicado" : True, "msj": "El correo ya fue registrado"}
            else:
                conn.close()
                return {"duplicado" : False, "msj": "Correo disponible"}     
    except:
        return jsonify({'msj': 'Error en la bd'})
def doble_telefono(telefono):
    try:
        conn = conexion()
        datos = []
        with conn.cursor() as cursor:
            sql = "SELECT * FROM usuarios where telefono = '{0}'".format(telefono)
            cursor.execute(sql)
            datos = cursor.fetchall()          
            if not len(datos) == 0:
                conn.close()
                return {"duplicado" : True, "msj": "El numero telefonico ya fue registrado"}
            else:
                conn.close()
                return {"duplicado" : False, "msj": "Numero telefonico disponible"}     
    except:
        return jsonify({'msj': 'Error en la bd'})

def registrar_usuario(usuario, password, nombre, apellido, correo, telefono):
    try:
        resusuario = doble_usuario(usuario)
        rescorreo = doble_correo(correo)
        restelefono= doble_telefono(telefono)
        if(resusuario['duplicado'],rescorreo['duplicado'],restelefono['duplicado']) != True:
            conn = conexion()
            with conn.cursor() as cursor:
                sql = "".format()
                print (sql)
                cursor.execute(sql)
            conn.close()
        else:
            return jsonify({'msj': 'Ocurrio un error'})
    except:
        return
@app.route('/')
def hello_world():

    return doble_correo('chipermas@gmail.com')


if __name__ == "__main__":
    app.run(debug=True)
