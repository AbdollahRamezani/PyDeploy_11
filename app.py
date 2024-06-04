from flask import Flask, render_template, request

app = Flask("Test Project")

@app.route("/", methods=["GET"])
def index():
    name = "abdollah"
    return render_template("index.html", firstname=name, lastname="ramezani")

@app.route("/download", methods=["GET"])
def download():
    media = ["image", "music", "movie"]
    return render_template("download.html", media=media)

@app.route("/me")
def my_information():
    my_info = {"firstname":"abdollah", "email":"a.ramezani84@gmail.com"}
    return my_info

@app.route("/blog", methods=["GET", "POST"])
def blog():
    if request.method == "GET":
        return "This is GET method"
    
    elif request.method == 'POST':
        return "Thid id POST method"  



