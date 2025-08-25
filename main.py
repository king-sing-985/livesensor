from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os
import sys
from sensor.logger import logging
from sensor.utils2 import dump_csv_file_to_mongodb_collection
# from sensor.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
from sensor.pipeline.training_pipeline import TrainPipeline

# def test_exception():
    # try:
        # logging.info("ki yaha pe bhaiya ek error aayegi division by zero wali error")
        # a=1/0
    # except Exception as e:
        # raise SensorException(e,sys)
# 

if __name__ == "__main__":
    # file_path=r"C:\Users\kiran\Programming\SENSORLIVE\aps_failure_training_set1.csv"
    # database_name="Kiran"
    # collectin_name="MongoClass"

    # dump_csv_file_to_mongodb_collection(file_path,database_name,collectin_name)

    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()






    # try:
        # test_exception()
    # except Exception as e:
        # print(e)