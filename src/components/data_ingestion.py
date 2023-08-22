import os
import sys
from src.exceptions import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered The Data Ingestion Module")
        try:
            #Can Change The Method To Load the Data From Different Sources
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("DataFrame Loaded Successfully.!")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path) , exist_ok = True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Raw Data Saved Successfully.!")
            logging.info("Splitting the data into train and test sets")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            logging.info("Train Data Saved Successfully.!")
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Test Data Saved Successfully.!")

            logging.info("Data Ingestion Module Completed Successfully.!")


            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()