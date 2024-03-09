# from flask import Flask
# import os, sys
# from Machine_learning.logger import logging
# from Machine_learning.exception import CustomException

# app = Flask(__name__)


# @app.route("/", methods=["GET", "POST"])
# def index():
#     try: 
#         raise Exception("This is a test Exception file")
#     except Exception as e:
#         temp = CustomException(e)
#         logging.error(temp.error_message)  # Use logging.error to log exceptions
#         logging.info("we are testing our logging module.")  # Use logging.info for general logs
        
#     return "testing the logging file success!"


# if __name__ == "__main__":
#     app.run(debug=False)  # Specify port 6000
