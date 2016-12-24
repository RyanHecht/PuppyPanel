from flask import Flask, current_app
from gevent.wsgi import WSGIServer
app = Flask(__name__)

@app.route("/out")
def out():
    print("idk")

def feed():
    print("irdk")

if __name__ == "__main__":
    print("Starting Webserver")
    http_server = WSGIServer(('', 80), app)
    http_server.serve_forever()
