from flask import Flask
from Machine_learning.logger import logging

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    logging.info("we are testing our logging module.")
    return "testing the logging file success!"


if __name__ == "__main__":
    app.run(debug=False)  # Specify port 6000
