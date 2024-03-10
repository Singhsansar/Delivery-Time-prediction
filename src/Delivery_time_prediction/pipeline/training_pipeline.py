from Delivery_time_prediction.constants import *
from Delivery_time_prediction.config.configuration import *
from Delivery_time_prediction.logger import logger
import os, sys
from Delivery_time_prediction.utils import save_obj, evaluate_model
from Delivery_time_prediction.components.model_trainer import ModelTrainer
from Delivery_time_prediction.components.data_tranformation import (
    DataTransformation,
    DataTransformationConfig,
)
from Delivery_time_prediction.components.data_ingestion import (
    DataIngestion,
    DataIngestionConfig,
)


class Train:
    def __init__(self):
        self.c = 0
        print(f"*******{self.c}********")

    def main(self):
        data_ingestion = DataIngestion()
        train_data, test_data = data_ingestion.initiate_data_ingestion()

        data_transformation = DataTransformation()
        train_arr, test_arr, processing_obj = (
            data_transformation.inititate_data_transformation(train_data, test_data)
        )
        model_trainer = ModelTrainer()
        model_trainer.initiate_model_training(train_arr, test_arr)
        logger.info('===================Model training completed==========================')
        print('===================Model training completed==========================')
