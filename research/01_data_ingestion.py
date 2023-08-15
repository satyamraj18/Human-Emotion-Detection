import os
from humanEmotionClassifier.constants import *
from humanEmotionClassifier.utils.common import read_yaml, create_directories,get_size
from humanEmotionClassifier import logger
from dataclasses import dataclass
from pathlib import Path
import urllib.request as request
import zipfile
import gdown

print(os.getcwd())
os.chdir("../")
print(os.getcwd())

@dataclass(frozen=True)        #Its an entity as it will help to create your own custom return type
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,param_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.param = read_yaml(param_filepath)
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

class DataIngestion:
    def __init__(self,config : DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            gdown.download(self.config.source_URL, self.config.local_data_file, quiet=False, fuzzy=True)
            #logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}") 
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        #zipfile.ZipFile(self.config.local_data_file, 'r').testzip()
        with zipfile.ZipFile(self.config.local_data_file) as zip_ref:
            zip_ref.extractall(unzip_path)

try:
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip_file()
except Exception as e:
    raise e



    
    



