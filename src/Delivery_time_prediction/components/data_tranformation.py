from Delivery_time_prediction.constants import *
from Delivery_time_prediction.config.configuration import *
from Delivery_time_prediction.logger import logger
from Delivery_time_prediction.exception import CustomException
import os, sys
import socket
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder


@dataclass
class Feature_engineering(BaseEstimator, TransformerMixin):
    def __init__(self):
        logger.info("-------Feature Engineering initiated--------")

    def distance_numpy_function(self, df, lat1, lon1, lat2, lon2):
        p = np.pi / 180
        a = (
            0.5
            - np.cos((df[lat2] - df[lat1]) * p) / 2
            + np.cos(df[lat1] * p)
            * np.cos(df[lat2] * p)
            * (1 - np.cos((df[lon2] - df[lon1]) * p))
            / 2
        )
        df["distance"] = 12742 * np.arcsin(np.sort(a))

    def transform_data(self, df):
        try:
            df.drop("id", axis=1, inplace=True)  # drop the id colums
            self.distance_numpy_function(
                df,
                "Restaurant_latitude",
                "Restaurant_longitude",
                "Delivery_location_latitude",
                "Delivery_location_longitude",
            )
            df.drop(
                [
                    "Delivery_person_ID",
                    "Restaurant_latitude",
                    "Restaurant_longitude",
                    "Delivery_location_latitude",
                    "Delivery_location_longitude",
                    "Order_date",
                    "Time_Orderd",
                    "Time_Order_picked",
                ],
                axis=1,
                inplace=True,
            )
            logger.info("droping columns from our orignal dataset")
            return df
        except Exception as e:
            raise CustomException(e)

    def tranform(self, X: pd.DataFrame, y: None):
        try:
            transform_df = self.transform_data(X)
            return transform_df
        except Exception as e:
            raise CustomException(e)


class DataTransformationConfig:
    process_obj_file_path = PREPROCESSING_OBJ_FILE
    transform_train_path = TRANSFORM_TRAIN_FILE_PATH
    transform_test_path = TRANSFORM_TEST_FILE_PATH
    feature_engineering_file_path = FEATURE_ENGG_OBJ_FILE


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        self.feature_engineering = Feature_engineering()

    def get_data_transformation_obj(self):
        try:
            Road_traffic_density = ["Low", "Medium", "High", "Jam"]
            Weather_conditions = [
                "Sunny",
                "Cloudy",
                "Fog",
                "Sandstorms",
                "Windy",
                "Stormy",
            ]

            categorical_columns = [
                "Type_of_order",
                "Type_of_vehicle",
                "Festival",
                "City",
            ]
            ordinal_encoder = ["Road_traffic_density", "Weather_conditions"]
            numerical_column = [
                "Delivery_person_Age",
                "Delivery_person_Ratings",
                "Vehicle_condition",
                "multiple_deliveries",
                "distance",
            ]

            # Numerical pipeline
            numerical_pipeline = Pipeline(
                steps=[
                    ("impute", SimpleImputer(strategy="constant", fill_value=0)),
                    ("scaler", StandardScaler(with_mean=False)),
                ]
            )

            # Categorical Pipeline
            categorical_pipeline = Pipeline(
                steps=[
                    ("impute", SimpleImputer(strategy="most_frequent")),
                    ("onehot", OneHotEncoder(handle_unknown="ignore")),
                    ("scaler", StandardScaler(with_mean=False)),
                ]
            )

            # ordinal Pipeline
            ordinal_pipeline = Pipeline(
                steps=[
                    ("impute", SimpleImputer(strategy="most_frequent")),
                    (
                        "ordinal",
                        OrdinalEncoder(
                            categories=[Road_traffic_density, Weather_conditions]
                        ),
                    ),
                    ("scaler", StandardScaler(with_mean=False)),
                ]
            )

            preprocssor = ColumnTransformer(
                [
                    ("numerical_pipeline", numerical_pipeline, numerical_column),
                    ("categorical_pipeline", categorical_pipeline, categorical_columns),
                    ("ordinal_pipeline", ordinal_pipeline, ordinal_encoder),
                ]
            )

            logger.info("Pipeline Steps Completed")
            return preprocssor

        except Exception as e:
            raise CustomException(e, sys)
