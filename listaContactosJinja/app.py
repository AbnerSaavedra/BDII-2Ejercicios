from flask import Flask, redirect, request, render_template, url_for, flash

app = Flask(__name__, template_folder="./templates")
app.config['SECRET_KEY'] = "clave_secreta"

contactList = []

@app.route("/contacts", methods=["GET"])
def contacts():
    return render_template("listaContactos.html.jinja", contactList=contactList)

@app.route("/about", methods=["GET"])
def aboutUs():
    aboutUs = "I am a software engineer and I am working as a software instructor."
    return render_template("aboutUs.html.jinja", aboutUs=aboutUs)

@app.route('/contact', methods=['GET', 'POST'])
def crearContacto():
    if request.method == "POST":
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        email = request.form['email']
        direccion = request.form['direccion']

        if not nombre:
            flash('El nombre es obligatorio')
        if not apellido:
            flash('El apellido es obligatorio')

        if nombre and apellido:
            contactList.append({'nombre': nombre, 'apellido': apellido, "telefono": telefono, "email": email, "direccion": direccion})
            return redirect(url_for('contacts'))

    return render_template("crearContacto.html.jinja")

@app.route("/verContacto", methods=["GET"])
def verContacto():
    index = request.args.get("index")
    nombre = request.args.get("nombre")
    print("Nombre: ", nombre)
    contacto = contactList[int(index)]

    return render_template("verContacto.html.jinja", contacto=contacto)

if __name__ == "__main__":
    app.run(debug=True)