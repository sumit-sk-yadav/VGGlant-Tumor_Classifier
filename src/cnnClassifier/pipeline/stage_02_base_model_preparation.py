from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

STAGE_NAME = 'BASE MODEL PREPARATION'

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        base_model_config = config.get_base_model_config()
        prepare_base_model = PrepareBaseModel(config=base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model() 


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\nx=====================================================x")
    except Exception as e:
        logger.exception(e)
        raise e