from app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
