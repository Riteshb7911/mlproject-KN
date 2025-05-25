from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformation,DataTransformationConfig




if __name__=="__main__":
    logging.info("The Execution has started.")

    try:
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initaite_data_ingestion()

        data_transormation=DataTransformation()
        data_transormation.initiate_data_transormation(train_data_path,train_data_path)



    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)