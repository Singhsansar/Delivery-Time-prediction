from sklearn.metrics import r2_score
from Delivery_time_prediction.logger import logger
from Delivery_time_prediction.exception import CustomException
import os, sys
import pickle


def save_obj(file_path, obj):
    try:
        dir_name = os.path.dirname(file_path)
        os.makedirs(dir_name, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e)


def evaluate_model(x_train, y_train, x_test, y_test, models):
    try:
        report = {}
        for name, model in models.items():
            model.fit(x_train, y_train)
            y_test_pred = model.predict(x_test)
            test_model_score = r2_score(y_test, y_test_pred)
            report[name] = test_model_score
        return report
    except Exception as e:
        logger.error(f"Error in model evaluation: {str(e)}")
        raise CustomException(e)


def load_model(MODEL_FILE_PATH):
    try:
        with open(MODEL_FILE_PATH, "rb") as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        logger.error(f"Error in model loading: {str(e)}")
        raise CustomException(e)
