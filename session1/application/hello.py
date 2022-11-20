from flask import Flask, redirect, url_for, request


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello you are in the home page"

@app.route("/<name>")
def user(name):
    return f"Home {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route('/formtest', methods=['POST', 'GET'])
def form_test():
    if request.method == 'POST':
        return 'Username: %s' % (request.form['username'])
    else:
        return '''  <form action="/formtest" method="post">
            Name: <input name="username" type="text" /> <br/>
            <input value="Send" type="submit" />
        </form>  '''


if __name__ == "__main__":
    app.run()
