import os
from datetime import datetime


def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


CURRENT_TIME_STAMP = get_current_timestamp()
ROOT_DIR_KEY = os.getcwd()

DATA_DIR = "Data"
DATA_DIR_KEY = "finalTrain.csv"
ARTIFACT_DIR = "Artifact"

# Data ingestion related variables
DATA_INGESTION_KEY = "data_ingestion"
DATA_INGESTION_RAW_DATA_DIR = "raw_data"
DATA_INGESTION_INGESTED_DATA_DIR_KEY = "ingested_data"
RAW_DATA_DIR_KEY = "raw_data.csv"
TRAIN_DATA_DIR_KEY = "train_data.csv"
TEST_DATA_DIR_KEY = "test_data.csv"

# Data transformation related variables
# atrifact /data_transformation/processer/processor.pkl and transformed -> tran.csv and test.csv
DATA_TRASFORMATION_ARTIFACT = "data_transformation"
DATA_PREPROCESSED_DIR = "processor"
DATA_TRANFOMATION_PROCESSING_OBJ = "processor.pkl"
DATA_TRANSFORMED_DIR = "transformation"
TRANSFORM_TRAIN_DATA_DIR_KEY = "train.csv"
TRANSFORM_TEST_DATA_DIR_KEY = "test.csv"
FEATURE_ENGG = "feature_engg.pkl"

# Model Training
MODEL_TRAINER_KEY = "model_trainer"
MODEL_OBJECT = "model.pkl"
