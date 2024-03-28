from src.logger import logging
from src.exception import CustomException
import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_ingestion import DataIngestionConfig
from src.components.data_transformation import DataTransformationConfig,DataTransformation



if __name__=="__main__":
    logging.info("The execution has started")
    
    try:
        data_ingestion_config=DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
        #data_transformation_config = DataTransformationConfig()
        #data_transformation=DataTransformation()
        #train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)
        
        
    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e,sys)
