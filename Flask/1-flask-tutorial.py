from flask import Flask  , redirect , url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! this is the main page <h1>HELLO<h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin/")
def admin():
    return redirect(url_for("user" , name="Admin!"))

if __name__ == "__main__":
    app.run()