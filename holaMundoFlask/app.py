from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "¡Hola mundo!"

@app.route("/greet", methods=['GET'])
def greeting():
    return "¡Esto es un saludo!"

# Variables
@app.route("/greetToSomeone/<nombre>", methods=['GET'])
def greetToSomeone(nombre):
    return f"¡Hello {nombre}!"

# Query
@app.route("/goodByeSomeone", methods=['GET'])
def goodByeSomeone():
    nombre = request.args.get("nombre")
    return f"¡Good bye {nombre}!"

# Post
@app.route("/mensaje", methods=["POST"])
def message():
    name = request.form.get("name")
    message = request.form.get("message")

    return f"¡Hola <b>{name}</b>, tu mensaje es: <b>{message}</b>!"

@app.route("/formMensaje", methods=["GET"])
def formMensaje():
    return '''
            <form method="POST" action="/mensaje">
            <div><label>Name: <input type="text" name="name"></label></div>
            <div><label>Message: <input type="text" name="message"></label></div>
            <input type="submit" value="Submit">
            </form>'''

@app.route("/message", methods=["GET", "POST"])
def message2():

    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        return '''
            <h1>The name value is: {}</h1>
            <h1>The mesage value is: {}</h1>
            '''.format(name, message)
    
    return '''
            <form method="POST">
            <div><label>Name: <input type="text" name="name"></label></div>
            <div><label>Message: <input type="text" name="message"></label></div>
            <input type="submit" value="Submit">
            </form>'''
        #f"Hola {name} tu mensaje es : {message}"

if __name__ == "__main__":
    app.run(debug=True)