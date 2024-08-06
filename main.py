from flask import Flask, render_template

app = Flask(__name__)

#@app.route("/")
#@app.route("/<name>/")
#def hello_world(name="stranger"):
#    return f"Hello, {name}"

#@app.route("/")
#@app.route("/<password>/")
#def hello_world(password=None):
#    if password == "1234":
#        return f"Access granted"
#    else:
#        return f"Access denied"

#@app.route("/")
#def hello_world():
#    html = """
#    <h1>Test run of local server</h1>
#    <p>This is just a text</p>
#    """
#    return html

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()