from flask import Flask, request

import config

app = Flask(__name__)

@app.route("/")
def hello():
    usrname = request.environ.get('REMOTE_USER')
    return "Hello World!" + usrname + '            ' + str(request.headers)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
