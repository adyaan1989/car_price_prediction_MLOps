from carsales.logging import logger
from carsales.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from carsales.pipeline.stage_02_data_validation import DataValidationPipeline
from carsales.pipeline.stage_03_data_transformation import DataTransformationPipeline


# data Ingestion state
STAGE_NAME = "Data Ingestion stage"
   
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion_pipeline = DataIngestionTrainingPipeline()
   data_ingestion_pipeline.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

# Data validation

STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation_pipeline = DataValidationPipeline()
   data_validation_pipeline.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

# data Transformation

STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation_pipeline = DataTransformationPipeline()
   data_transformation_pipeline.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

