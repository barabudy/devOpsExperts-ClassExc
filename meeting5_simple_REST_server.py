from flask import Flask
app = Flask("myRestAPIApp")


@app.route('/')
def hello_world():
    return "<h1>Hello! I am a Flask web app</h1>"


app.run(host='0.0.0.0', port="8080")
