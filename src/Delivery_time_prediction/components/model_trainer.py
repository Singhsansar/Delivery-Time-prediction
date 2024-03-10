from Delivery_time_prediction.constants import *
from Delivery_time_prediction.config.configuration import *
from Delivery_time_prediction.logger import logger
from Delivery_time_prediction.exception import CustomException
from Delivery_time_prediction.utils import save_obj, evaluate_model
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
import sys


class ModelTrainerConfig:
    trained_model_file_path = MODEL_FILE_PATH


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, train_array, test_array):
        try:
            x_train, y_train, x_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1],
            )  # splitting it into x and y, train-test and split

            models = {
                "xgboost": XGBRegressor(),
                "random_forest": RandomForestRegressor(),
                "GradientBoosting": GradientBoostingRegressor(),
                "DecisionTree": DecisionTreeRegressor(),
                "svr": SVR(),
            }

            model_report = evaluate_model(x_train, y_train, x_test, y_test, models)

            best_model_name = max(model_report, key=model_report.get)
            best_model_score = model_report[best_model_name]

            print("=" * 50)

            print(f"Best model is {best_model_name}, R2 score is {best_model_score}")
            logger.info(
                f"Best model is {best_model_name}, R2 score is {best_model_score}"
            )
            print("=" * 50)
            save_obj(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=models[best_model_name],
            )

        except Exception as e:
            logger.error(f"Error in model training: {str(e)}")
            raise CustomException(e, sys)
