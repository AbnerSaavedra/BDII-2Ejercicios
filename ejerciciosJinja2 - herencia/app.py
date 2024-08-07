from flask import Flask, redirect, request, render_template, url_for, flash

app = Flask(__name__, template_folder="./templates")
app.config['SECRET_KEY'] = "clave_secreta"

messagesList = []

@app.route("/tasks", methods=["GET"])
def returnTasks():
    tasks = ["Sleep", "Eat", "Study", "Be happy"]
    return render_template("listTasks.html.jinja", tasks=tasks)

@app.route("/about", methods=["GET"])
def aboutUs():
    aboutUs = "I am a software engineer and I am working as a software instructor."
    return render_template("aboutUs.html.jinja", aboutUs=aboutUs)

@app.route("/CV", methods=["GET"])
def CV():
    personalData = {"name": "Abner Saavedra", "address": "Lara"}
    
    workExperience = [{"title": "Fullstack developer (remote mode)", "factory": "Hispanos soluciones", 
                       "startDate": "October 2022", "endDate": "January 2023",
                       "activities":["NodeJS/Angular fullstack developer at Ragatex.",
                        "Data model creation and implementation",
                        "REST API service development",
                        "Integration and consumption of REST API services",
                        "Testing and debugging REST API services",
                        "Creation and integration of software components",
                        "Debugging and improvement of existing functionalities",
                        "HTML and CSS web layout",
                        "Continuous integration of advances",]}]
    
    education = ["UE El Cercado", "LB Jorge Antonio Rodríguez", "UCLA", "SEPAD"]
    skills = ["Projects managment", "Software development", "Process improvement"]

    return render_template("cv.html.jinja", personalData=personalData, workExperience=workExperience, 
                           skills=skills, education=education)

@app.route('/contact', methods=['GET', 'POST'])
def crearMensaje():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('El título es obligatorio')
        if not content:
            flash('El contenido es obligatorio')

        if title and content:
            messagesList.append({'title': title, 'content': content})
            return redirect(url_for('messages'))

    return render_template("crearMensaje.html.jinja")

@app.route("/messages", methods=["GET"])
def messages():
    return render_template("messages.html.jinja", messages=messagesList)

if __name__ == "__main__":
    app.run(debug=True)