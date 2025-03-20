from cnnClassifier.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig,BaseModelConfig, TrainingConfig, EvaluationConfig
from pathlib import Path
import os

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,# access the config.yaml file and the params.yaml file from their paths and store them
            params_filepath = PARAMS_FILE_PATH):

            self.config = read_yaml(config_filepath)# read the yaml files using the custorm read_yaml function
            self.params = read_yaml(params_filepath)# the function returns a configBox datatype 

            create_directories([self.config.artifacts_root]) # creates a directory called artifacts root as stated in the config.yaml file

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion # using the configBox accessing method we can access the data_ingestion key inside the config file

        create_directories([config.root_dir]) # create a the root directory as mentioned in the config file

        data_ingestion_config = DataIngestionConfig( # use the previously created frozen entity for managing the data ingestion variables
            root_dir = config.root_dir,# access the information stored int he config  file and read it into respective  variables one by one
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        
        return data_ingestion_config
    
    def get_base_model_config(self) -> BaseModelConfig:
        config = self.config.prepare_base_model

        create_directories([config.root_dir])

        base_model_config = BaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
            )
        return base_model_config

    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "kidney-ctscan-data")
        create_directories([
            Path(training.root_dir)
        ])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE,
            params_learning_rate=params.LEARNING_RATE
        )

        return training_config

    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model="artifacts/training/model.h5",
            training_data='artifacts/data_ingestion/kidney-ctscan-data',
            mlflow_uri="https://dagshub.com/sumit-sk-yadav/kidney_disease_classifier.mlflow",
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        return eval_config