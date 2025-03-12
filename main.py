from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_base_model_preparation import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\nx=====================================================x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = 'BASE MODEL PREPARATION'
try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        base_model_preparation = PrepareBaseModelTrainingPipeline()
        base_model_preparation.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\nx=====================================================x")
except Exception as e:
        logger.exception(e)
        raise e