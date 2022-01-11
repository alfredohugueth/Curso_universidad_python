from flask import Flask, request, render_template, url_for, jsonify
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

# El nombre predeterminado es APP
# Para correr en modo desarrollo: set FLASK_APP=app.py en windows, en mac es EXPORT FLASK_APP=app.py
# set FLASK_ENV = development windows, export FLASK_ENV = development

app = Flask(__name__)


# http://localhost:5000/
@app.route('/')
def inicio():
    app.logger.info(f'Entramos al path {request.path}')
    return 'HOLA MUNDO DESDE FLASK'


@app.route('/saludar/<nombre>')  # <variable> nos permite recibir variables dentro de la url
def saludar(nombre: str):
    return f'Saludos {nombre.upper()}'


@app.route('/edad/<int:edad>')  # Para variables de tipo diferente a string, <tipo:variable>
def mostrar_edad(edad: int):
    return f'Tu edad es: {edad}'


@app.route('/mostrar/<nombre>', methods={'GET', 'POST'})
def monstrar_nombre(nombre):
    return render_template('mostrar.html', nombre_llave=nombre)


@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('monstrar_nombre', nombre='alfredo'))


@app.route('/salir')
def salir():
    return abort(404)


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html', error=error), 404


# REST Representation State Transfer
@app.route('/api/mostrar/<nombre>', methods={'GET', 'POST'})
def mostrar_json(nombre):
    valores = {
        'nombre': nombre,
        'metodo_http': request.method
    }
    return jsonify(valores)  # jsonify convierte el tipo de dato retornado a un diccionario
