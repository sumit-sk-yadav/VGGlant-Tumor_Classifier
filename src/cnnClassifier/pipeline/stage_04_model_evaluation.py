from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation_mlflow import Evaluation
from cnnClassifier import logger

STAGE_NAME = 'MODEL EVALUATION'

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_evaluation_config()
        evaluate_model = Evaluation(config = evaluation_config)
        evaluate_model.evaluation()
        evaluate_model.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        model_evaluation = ModelEvaluationPipeline()
        model_evaluation.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\nx=====================================================x")
    except Exception as e:
        logger.exception(e)
        raise e