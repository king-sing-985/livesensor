import os

TARGET_COLUMN = "class"
PIPELINE = "sensor"
ARTIFACT_DIR = "artifact"
FILE_NAME = "sensor.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME ="preprocrssing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_NAME = os.path.join("config", "schema.yaml")
SCHEMA_DROP_COLS = "drop_columns"

"""
data ingestion related constant values
"""

DATA_INGESTION_COLLECTION_NAME: str = "MongoClass"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2