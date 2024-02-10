import sys
from Xray.components.data_ingestion import DataIngestion
# from xray.components.data_transformation import DataTransformation
# from xray.components.model_training import ModelTrainer
# from xray.components.model_evaluation import ModelEvaluation
from Xray.exception import XRayException
from Xray.logger import logging
from Xray.entity.artifact_entity import (
    DataIngestionArtifact,
    # DataTransformationArtifact,
    # ModelTrainerArtifact,
    # ModelEvaluationArtifact
    )

from Xray.entity.config_entity import (
    DataIngestionConfig,
    # DataTransformationConfig,
    # ModelTrainerConfig,
    # ModelEvaluationConfig
)

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        # self.data_transformation_config = DataTransformationConfig()
        # self.model_trainer_config = ModelTrainerConfig()
        # self.model_evaluation_config=ModelEvaluationConfig()
        
        
    def start_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:

            logging.info("Getting the data from s3 bucket")

            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config,
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info("Got the train_set and test_set from s3")

            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact

        except Exception as e:
            raise XRayException(e, sys)
        
        
if __name__=="__main__":
    train_pipeline=TrainPipeline()
    train_pipeline.start_data_ingestion()        