from Delivery_time_prediction.config.configuration import (
    TRAIN_FILE_PATH,
    TEST_FILE_PATH,
    RAW_FILE_PATH,
    DATASET_PATH,
)
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from Delivery_time_prediction.logger import logger
from Delivery_time_prediction.exception import CustomException


@dataclass
class DataIngestionConfig:
    train_data_path: str = TRAIN_FILE_PATH
    test_data_path: str = TEST_FILE_PATH
    raw_data_path: str = RAW_FILE_PATH


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            df = pd.read_csv(
                DATASET_PATH
            )  # dataset is avaliable otherwise we should initiate the data download first
            os.makedirs(
                os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True
            )
            df.to_csv(self.data_ingestion_config.raw_data_path, index=False)

            # Splitting the data into train and test
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            os.makedirs(
                os.path.dirname(self.data_ingestion_config.train_data_path),
                exist_ok=True,
            )
            os.makedirs(
                os.path.dirname(self.data_ingestion_config.test_data_path),
                exist_ok=True,
            )
            train_set.to_csv(
                self.data_ingestion_config.train_data_path, header=True, index=False
            )
            test_set.to_csv(
                self.data_ingestion_config.test_data_path, header=True, index=False
            )

            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path,
            )

        except Exception as e:
            logger.error(f"Error in data ingestion: {str(e)}")
            raise CustomException(e)
