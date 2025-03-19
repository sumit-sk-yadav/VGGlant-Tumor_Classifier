from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_base_model_preparation import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline
import warnings
warnings.filterwarnings('ignore')

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

STAGE_NAME = 'MODEL TRAINING'
try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        model_training = ModelTrainingPipeline()
        model_training.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\nx=====================================================x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = 'MODEL EVALUATION'
try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        model_evaluation = ModelEvaluationPipeline()
        model_evaluation.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\nx=====================================================x")
except Exception as e:
        logger.exception(e)
        raise e