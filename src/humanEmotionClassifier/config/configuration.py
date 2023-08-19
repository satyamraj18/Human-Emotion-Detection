from humanEmotionClassifier.utils.common import create_directories,read_yaml
from humanEmotionClassifier.entity.config_entity import (DataIngestionConfig,PrepareBaseModelConfig)
from humanEmotionClassifier.constants import *

class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,param_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(param_filepath)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(         #Using the entity you have created above
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )
        return data_ingestion_config
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:   #We are preparing our basemodel and storing it in h5 format
        config = self.config.prepare_base_model    #in the path we specified in the config.yaml in "prepare_base_model"
                                                   #Additionally we will use the parameter specified in the param.yaml
        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config