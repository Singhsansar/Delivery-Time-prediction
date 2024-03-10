from flask import Flask, render_template, request
from Delivery_time_prediction.config.configuration import (
    FEATURE_ENGG_OBJ_FILE,
    PREPROCESSING_OBJ_FILE,
    MODEL_FILE_PATH,
)
from Delivery_time_prediction.logger import logger
import os
from Delivery_time_prediction.pipeline.prediction_pipeline import (
    PredictionPipeline,
    customData,
)
from Delivery_time_prediction.pipeline.training_pipeline import Train
from Prediction.batch import BatchPrediction
from werkzeug.utils import secure_filename

feature_engineering_file_path = FEATURE_ENGG_OBJ_FILE
transformer_file_path = PREPROCESSING_OBJ_FILE
model_file_path = MODEL_FILE_PATH

UPLOAD_FOLDER = "Prediction/UPLOAD_CSV_FILE"


app = Flask(__name__, template_folder="templates")
ALLOWED_EXTENSIONS = {"csv"}  # Corrected variable name


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/predict", methods=["POST", "GET"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    else:
        data = customData(
            Delivery_person_Age=int(request.form.get("age")),
            Delivery_person_Ratings=float(request.form.get("rating")),
            Weather_conditions=request.form.get("Weather_conditions"),
            Road_traffic_density=request.form.get("Road_traffic_density"),
            Vehicle_condition=int(request.form.get("Vehicle_condition")),
            multiple_deliveries=int(request.form.get("multiple_deliveries")),
            distance=float(request.form.get("distance")),
            Type_of_order=request.form.get("Type_of_order"),
            Type_of_vehicle=request.form.get("Type_of_vehicle"),
            Festival=request.form.get("Festival"),
            City=request.form.get("City"),
        )
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictionPipeline()

        pred = predict_pipeline.predict(final_new_data)
        print(pred)
        result = int(pred[0])

        return render_template("result.html", final_result=result)


@app.route("/batch", methods=["POST", "GET"])
def perform_batch_prediction():
    if request.method == "GET":
        return render_template("batch.html")
    else:
        file = request.files["csv_file"]  # upload the key to csv file
        directory_path = UPLOAD_FOLDER
        os.makedirs(directory_path, exist_ok=True)  # Corrected function call

        if (
            file
            and "." in file.filename
            and file.filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
        ):
            file_path = os.path.join(
                directory_path, secure_filename(file.filename)
            )  # Secured filename usage
            file.save(file_path)
            logger.info(f"File uploaded successfully at {file_path}")

            batch = BatchPrediction(
                input_file_path=file_path,
                model_file_path=model_file_path,
                transformer_file_path=transformer_file_path,
                feature_eng_file_path=feature_engineering_file_path,
            )

            batch.start_batch_prediction()
            output = "Batch prediction done"

            return render_template(
                "batch.html", prediction_result=output, prediction_type="batch"
            )
        else:
            return render_template(
                "batch.html", error="Invalid file type", prediction_type="batch"
            )


@app.route("/train", methods=["GET", "POST"])
def train():
    return render_template("train.html")
    # error_message = ""  # Initialize error message
    # success_message = ""  # Initialize success message
    
    # if request.method == "GET":
    #     return render_template("train.html")
    # else:
    #     try:
    #         pipeline = Train()
    #         pipeline.main()
    #         success_message = "Training completed successfully."
    #     except Exception as e:
    #         logger.error(f"{e}")
    #         error_message = str(e)
    #     return render_template(
    #         "index.html", error=error_message, success=success_message
    #     )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0", debug=True, port=8888
    )  # Removed quotation marks around port
