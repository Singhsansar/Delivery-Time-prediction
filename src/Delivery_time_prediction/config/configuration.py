from Delivery_time_prediction.constants import *
import os, sys

ROOT_DIR = ROOT_DIR_KEY

# data ingestion related variables
DATASET_PATH = os.path.join(ROOT_DIR, DATA_DIR, DATA_DIR_KEY)
RAW_FILE_PATH = os.path.join(
    ROOT_DIR,
    ARTIFACT_DIR,
    DATA_INGESTION_KEY,
    CURRENT_TIME_STAMP,
    DATA_INGESTION_RAW_DATA_DIR,
    RAW_DATA_DIR_KEY,
)  # "Artifact/data_ingestion/2021-09-29_12-00-00/raw_data/raw_data.csv"
TRAIN_FILE_PATH = os.path.join(
    ROOT_DIR,
    ARTIFACT_DIR,
    DATA_INGESTION_KEY,
    CURRENT_TIME_STAMP,
    DATA_INGESTION_INGESTED_DATA_DIR_KEY,
    TRAIN_DATA_DIR_KEY,
)  # "Artifact/data_ingestion/2021-09-29_12-00-00/ingested_data/train_data.csv"
TEST_FILE_PATH = os.path.join(
    ROOT_DIR,
    ARTIFACT_DIR,
    DATA_INGESTION_KEY,
    CURRENT_TIME_STAMP,
    DATA_INGESTION_INGESTED_DATA_DIR_KEY,
    TEST_DATA_DIR_KEY,
)  # "Artifact/data_ingestion/2021-09-29_12-00-00/ingested_data/test_data.csv"

# data transformation related variables
PREPROCESSING_OBJ_FILE = os.path.join(
    ROOT_DIR,
    ARTIFACT_DIR,
    DATA_TRASFORMATION_ARTIFACT,
    DATA_PREPROCESSED_DIR,
    DATA_TRANFOMATION_PROCESSING_OBJ,
)  # "Artifact/data_transformation/processor/processor.pkl"

TRANSFORM_TRAIN_FILE_PATH = os.path.join(
    ROOT_DIR,
    ARTIFACT_DIR,
    DATA_TRASFORMATION_ARTIFACT,
    DATA_TRANSFORMED_DIR,
    TRANSFORM_TRAIN_DATA_DIR_KEY,
)  # "Artifact/data_transformation/transformation/train.csv"

TRANSFORM_TEST_FILE_PATH = os.path.join(
    ROOT_DIR,
    ARTIFACT_DIR,
    DATA_TRASFORMATION_ARTIFACT,
    DATA_TRANSFORMED_DIR,
    TRANSFORM_TEST_DATA_DIR_KEY,
)  # "Artifact/data_transformation/transformation/test.csv"

FEATURE_ENGG_OBJ_FILE = os.path.join(
    ROOT_DIR,
    ARTIFACT_DIR,
    DATA_TRASFORMATION_ARTIFACT,
    DATA_PREPROCESSED_DIR,
    FEATURE_ENGG,
)  # "Artifact/feature_engineering/feature_engg/feature_engg.pkl"

# Model Training
MODEL_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR, MODEL_TRAINER_KEY, MODEL_OBJECT)
