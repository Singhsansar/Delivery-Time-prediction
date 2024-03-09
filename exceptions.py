from flask import Flask
from Delivery_time_prediction.logger import logging
from Delivery_time_prediction.exception import CustomException

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    try:
        raise Exception("This is a test Exception file")
    except Exception as e:
        temp = CustomException(e)
        logging.error(temp.error_message)  # Use logging.error to log exceptions
        logging.info(
            "we are testing our logging module."
        )  # Use logging.info for general logs

    return "testing the logging file success!"


if __name__ == "__main__":
    app.run(debug=False)  # Specify port 6000
