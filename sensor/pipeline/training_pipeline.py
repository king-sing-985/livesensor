from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.exception import SensorException
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.logger import loggiing
import os, sys
from sensor.components.data_ingestion import DataIngestion

from sensor.components.data_validation import DataValidation

from sensor.entity.config_entity import