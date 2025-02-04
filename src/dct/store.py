
import pandas as pd
from sqlalchemy import create_engine
import logging

logging.basicConfig(filename='datatransformation.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class DataStore:
    def __init__(self,data,url):
        self.data = data
        self.url = url

    def connect(self):
        engine = create_engine(self.url)
        logging.info(f"Connected to database {self.url}")
        self.data.to_sql('cleaned_data', con=engine, if_exists='replace', index=False)
        logging.info("Data stored in database")



if __name__ == "__main__":
    data = pd.read_csv('cleaned_data.csv')
    url = "postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/dct"
    store = DataStore(data,url)
    store.connect()