from flask import Flask

app = Flask(__name__)
# app is object and flask is class
# object app created by flask class
# main is file name & app is object name therefore we need to change file name and object name accordingly in Procfile in notepad++


@app.route('/', methods=['GET', 'POST'])
def index():
    return "<h1>This is Flask Application</h1>"


if __name__ == "__main__":
    app.run()