from flask import Flask, current_app, request
from gevent.wsgi import WSGIServer
app = Flask(__name__)

@app.route("/dashboard")
def dashboard():
    return current_app.send_static_file('index.html')

@app.route("/res/<file_name>")
def res(file_name):
    return current_app.send_static_file(file_name)

@app.route("/out", methods=['GET'])
def out():
    date = request.args.get('date')
    time = request.args.get('time')
    return "good"

@app.route("/feed", methods=['GET'])
def feed():
    date = request.args.get('date')
    time = request.args.get('time')
    return "good"

@app.route("/undo/<action>")
def undo(action):
    return "undo"

if __name__ == "__main__":
    print("Starting Webserver")
    http_server = WSGIServer(('', 80), app)
    http_server.serve_forever()
