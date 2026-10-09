from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logger
from networksecurity.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
)
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == "__main__":
    try:
        # Data Ingestion
        trainig_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(trainig_pipeline_config)
        dataingestion = DataIngestion(data_ingestion_config)
        logger.info("Initiate Data Ingestion")
        data_ingestion_artifact = dataingestion.initiate_data_ingestion()
        logger.info("Data Ingestion Completed")
        print(data_ingestion_artifact)

        # Data Validation
        data_validation_config = DataValidationConfig(trainig_pipeline_config)
        data_validation = DataValidation(
            data_ingestion_artifact, data_validation_config
        )
        logger.info("Initiate Data Validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logger.info("Data Validation Completed")
        print(data_validation_artifact)

        # Data Transformation
        data_transformation_config = DataTransformationConfig(trainig_pipeline_config)
        data_transformation = DataTransformation(
            data_validation_artifact, data_transformation_config
        )
        logger.info("Initiate Data Transformation")
        data_transformation_artifact = (
            data_transformation.initiate_data_transformation()
        )
        logger.info("Data Transformation Completed")
        print(data_transformation_artifact)

        # Model Trainer
        model_trainer_config = ModelTrainerConfig(trainig_pipeline_config)
        model_trainer = ModelTrainer(
            model_trainer_config=model_trainer_config,
            data_transformation_artifact=data_transformation_artifact,
        )
        logger.info("Initiate Data Transformation")
        model_trainer_artifact = (
            model_trainer.initiate_model_trainer()
        )
        logger.info("Data Transformation Completed")
        print(data_transformation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)
