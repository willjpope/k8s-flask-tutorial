from app import app
import config
from subprocess import STDOUT, check_call
import os

check_call(['apt-get', 'install', '-y', 'unixodbc-dev'],
     stdout=open(os.devnull,'wb'), stderr=STDOUT) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
