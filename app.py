from flask import Flask
from flask import render_template

app = Flask(__name__)

list = [
    'test1',
    'test2',
    'test3',
    'test4',
]

@app.route("/")
def hello_world():
    return "<p>Hello, こんにちは</p>"

# @app.route("/<name>")
# def hello_sub1(name):
#     return f"<p>{name}ページです</p>"

@app.route("/<name>")
def hello_sub2(name):
    return render_template('index.html', name=name, list=list)

if __name__ == "__main__":
    app.run()