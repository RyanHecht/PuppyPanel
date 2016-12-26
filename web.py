from flask import Flask, current_app, request, jsonify
from gevent.wsgi import WSGIServer
import db
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
    db.go_out(date,time)
    return "out"

@app.route("/feed", methods=['GET'])
def feed():
    date = request.args.get('date')
    time = request.args.get('time')
    db.add_meal(date, time, "meal")
    return "fed"

@app.route("/pill", methods=['GET'])
def pill():
    date = request.args.get('date')
    time = request.args.get('time')
    stamp = request.args.get('stamp')
    db.add_pill(date, time, stamp)
    return "pilled"

@app.route("/undo/<action>")
def undo(action):
    if action == "meal":
        return jsonify(db.undo_meal())
    elif action == "out":
        return jsonify(db.undo_out())
    elif action == "pill":
        return jsonify(db.undo_pill())

@app.route("/get/<action>")
def get(action):
    if action == "meal":
        return jsonify(db.get_meal())
    elif action == "out":
        return jsonify(db.get_out())
    elif action == "pill":
        return jsonify(db.get_pill())

if __name__ == "__main__":
    print("Starting Webserver")
    db.init()
    http_server = WSGIServer(('', 80), app)
    http_server.serve_forever()
