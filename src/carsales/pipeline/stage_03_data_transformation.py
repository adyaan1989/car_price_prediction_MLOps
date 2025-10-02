from carsales.config.configuration import ConfigurationManager
from carsales.components.data_transformation import DataTransformation
from carsales.logging import logger

STAGE_NAME = "Data Transformation stage"


class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        
        logger.info("Loading data...")
        df = data_transformation.load_data()
        
        logger.info("Splitting data into train and test...")
        data_transformation.split_data(df)
        
        logger.info("Building preprocessor pipeline...")
        preprocessor = data_transformation.build_preprocessor()
        
        logger.info("Transforming and saving data...")
        data_transformation.transform_and_save(preprocessor)
        
        logger.info("Data transformation completed successfully.")

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
