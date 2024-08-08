from flask import Flask, redirect, request, render_template, url_for, flash
from db import collection
from bson.objectid import ObjectId

app = Flask(__name__, template_folder="./templates")
app.config['SECRET_KEY'] = "clave_secreta"

@app.route("/elements", methods=["GET"])
def elements():
    elementos = collection.find()
    return render_template("listaElementos.html.jinja", elementos=elementos)


@app.route("/", methods=["GET", "POST"])
def add_element():
    if request.method == "POST":

        nombre = request.form['nombre']
        edad = request.form['edad']

        element = {
            'nombre' : nombre,
            'edad' : edad
        }

        print("Element: ", element)

        collection.insert_one(element)
        elementos = collection.find()
        return render_template("listaElementos.html.jinja", elementos=elementos)

    return render_template("crearElemento.html.jinja")

@app.route("/<id>", methods=["GET"])
def getElement(id):
    oid = ObjectId(id)
    element = collection.find_one({'_id': oid})
    return render_template("detalleElemento.html.jinja", element=element)

@app.route("/modificar/<id>", methods=["GET", "POST"])
def updateElement(id):
    oid = ObjectId(id)
    element = collection.find_one({'_id': oid})
    if request.method == "POST":
        new_element = request.form
        element = collection.replace_one({'_id': oid},
                                        {
                                            'nombre': new_element['nombre'],
                                            'edad': new_element['edad']
                                        })
        return redirect(url_for('elements'))
    return render_template("updateElemento.html.jinja", element=element)


@app.route("/delete/<id>", methods=["GET"])
def deleteElement(id):
    oid = ObjectId(id)
    collection.delete_one({'_id': oid})
    elementos = collection.find()
    return render_template("listaElementos.html.jinja", elementos=elementos)

if __name__ == "__main__":
    app.run(debug=True)