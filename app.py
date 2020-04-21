from flask import Flask, Request

import config

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! " + print(request.headers[X-Remote-User])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
