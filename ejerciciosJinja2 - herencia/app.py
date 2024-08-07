from flask import Flask, request, render_template

app = Flask(__name__, template_folder="./templates")

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

if __name__ == "__main__":
    app.run(debug=True)