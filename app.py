from flask import Flask, request

import config

app = Flask(__name__)

@app.route("/")
def hello():
    print("Headers: ", vars(request.headers))
    for header in request.headers.items():
        print(header)
    return "Hello World! "

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
