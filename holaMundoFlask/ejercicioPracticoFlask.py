import random
from flask import Flask, jsonify, request

app = Flask(__name__)

student_names = ["John", "Jane", "Bob", "Alice", "Mike", "Emma", "Oliver", "Sophia"]
notes = [random.randint(0, 100) for _ in range(10)]

@app.route("/")
def hello_world():
    return "¡Hola mundo!"

@app.route("/palindromo/<palabra>", methods=['GET'])
def palindromo(palabra):
    inicio = 0
    fin = len(palabra) - 1
    while palabra[inicio] == palabra[fin]:
        if inicio >= fin:
            return f"Si es palindromo <b>{palabra}</b>"
        inicio += 1
        fin -= 1
    return f"No es palindromo <b>{palabra}</b>"

@app.route("/palindromo2/<palabra>", methods=['GET'])
def palindromo2(palabra):
    p = palabra[::-1]
    if p == palabra:
        return f"La Palabra {palabra} si es Palindromo"
    else:
        return f"La Palabra No es Palindromo"

@app.route("/materia", methods=["GET"])
def listarMaterias():
    materia = request.args.get("materia")
    cantidad_str = request.args.get("cantidad")

    if not materia or not cantidad_str:
        return jsonify({"errores": "Invalid request"}), 400

    try:
        cantidad = int(cantidad_str)
    except ValueError:
        return jsonify({"error": "Cantidad debe ser un número entero"}), 400

    students = []
    for _ in range(cantidad):
        student_name = random.choice(student_names)
        note = random.choice(notes)
        approved = "Aprobó" if note >= 60 else "No aprobó"
        students.append({"nombre": student_name, "nota": note, "aprobado": approved})

    return jsonify({"materia": materia, "estudiantes": students})

@app.route("/json", methods=["GET"])
def devolverJSON():
    return jsonify({"nombre": "Abner Saavedra", "edad": 33})


if __name__ == "__main__":
    app.run(debug=True)