from humanEmotionClassifier import logger
from humanEmotionClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()   #Calls the dataIngestionTrainingPipeline class in the stage_01_data_ingestion.py
   data_ingestion.main()  #Calls the main method in the stage_01_data_ingestion.py
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e