from flask import Flask, request, render_template

app = Flask(__name__, template_folder="./templates")

@app.route("/saludoJinja/<nombre>", methods=["GET"])
def saludoJinja(nombre):
    return render_template("home.html.jinja", nombre=nombre)

@app.route("/items", methods=["GET"])
def listarItems():
    items = [{"nombre": "Uno", "categoria": "Número"}, {"nombre": "Dos", "categoria": "Número"},
             {"nombre": "Tres", "categoria": "Número"}, {"nombre": "A", "categoria": "Letra"},
             {"nombre": "B", "categoria": "Letra"}]
    titulo = "Listar items"
    return render_template("listaItems.html.jinja", items=items, titulo=titulo)

@app.route("/verificarMayoriaEdad", methods=["GET"])
def verificarMayoriaEdad():
    persona = {"nombre": "Abner Saavedra", "edad": 17}
    return render_template("condicionalEdad.html.jinja", persona=persona)

if __name__ == "__main__":
    app.run(debug=True)