from flask import Flask, Response, request
import os
import socket
import time
import hashlib

app = Flask(__name__)

# Enable debugging if the DEBUG environment variable is set and starts with Y
app.debug = os.environ.get("DEBUG", "").lower().startswith('y')

hostname = socket.gethostname()

@app.route("/")
def index():
    return "HASHER running on {}\n".format(hostname)

@app.route("/", methods=['POST'])
def hash():
    # time.sleep(0.1)
    digest = hashlib.sha256(request.data).hexdigest()
    return Response(digest, mimetype='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
