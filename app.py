from app import app
import config
from subprocess import STDOUT, check_call
import os

proc = subprocess.Popen('sudo apt-get install -y unixodbc-dev', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash")
proc.wait()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
