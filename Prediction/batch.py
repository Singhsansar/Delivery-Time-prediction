import os
import sys
import pickle
import pandas as pd
from sklearn.pipeline import Pipeline
from Delivery_time_prediction.logger import logger
from Delivery_time_prediction.exception import CustomException
from Delivery_time_prediction.utils import load_model


class BatchPrediction:
    def __init__(
        self,
        input_file_path: str,
        model_file_path: str,
        transformer_file_path: str,
        feature_eng_file_path: str,
    ) -> None:
        self.input_file_path = input_file_path
        self.model_file_path = model_file_path
        self.transformer_file_path = transformer_file_path
        self.feature_eng_file_path = feature_eng_file_path

    def start_batch_prediction(self):
        try:
            # Load the feature engineering pipeline
            with open(self.feature_eng_file_path, "rb") as f:
                feature_pipeline = pickle.load(f)

            # Load the data transformation pipeline
            with open(self.transformer_file_path, "rb") as f:
                processor = pickle.load(f)

            # Load the trained model
            model = load_model(self.model_file_path)

            # Create a feature engineering pipeline
            feature_engineering_pipeline = Pipeline(
                [("feature_engineering", feature_pipeline)]
            )

            # Read the input file
            df = pd.read_csv(self.input_file_path)

            # Apply Feature engineering pipeline steps
            df = feature_engineering_pipeline.transform(df)

            # Drop the target column if necessary
            df = df.drop(columns=["Time_taken (min)"], axis=1)

            # Apply data transformation pipeline
            transformed_data = processor.transform(df)
            predictions = model.predict(transformed_data)
            df_predictions = pd.DataFrame(predictions, columns=["Prediction"])

            # Save predictions to CSV
            output_folder = "batch_prediction"
            os.makedirs(output_folder, exist_ok=True)
            output_file = os.path.join(output_folder, "output.csv")
            df_predictions.to_csv(output_file, index=False)
            logger.info(f"Batch Prediction file is saved at {output_file}")

        except Exception as e:
            logger.error(f"Error in batch prediction: {str(e)}")
            raise CustomException(e, sys)
