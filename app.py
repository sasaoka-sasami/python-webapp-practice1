from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, こんにちは</p>"

@app.route("/sub1")
def hello_sub1():
    return "<p>sub1ページです</p>"

@app.route("/sub2")
def hello_sub2():
    return "<p>sub2ページです</p>"

if __name__ == "__main__":
    app.run()