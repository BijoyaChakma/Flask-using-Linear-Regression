from flask import Flask

app= Flask(__name__)

@app.route("/")
def wel():
    return "welcome"

@app.route("/home")
def home():
    return "this is my country"

if __name__=="__main__":
    app.run(debug=True)