from app import app
import config
import os

os.system('apt-get install -y unixodbc-dev')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
