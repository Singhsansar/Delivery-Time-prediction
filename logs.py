from flask import Flask
from Delivery_time_prediction.logger import logger

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    logger.info("we are testing our logging module.")
    return "testing the logging file success!"


if __name__ == "__main__":
    app.run(debug=False)  # Specify port 6000
