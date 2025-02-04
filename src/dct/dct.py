
import pandas as pd
import logging


logging.basicConfig(filename='datatransformation.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class DataCleaningTransformation:
    def __init__(self,data):
        self.data = data
        self.cleaned_data = None
    
    def clean_data(self):
        self.data = self.data.drop_duplicates(subset=['ID']).copy()

        self.data['Message'] = self.data['Message'].fillna('No Message')
        self.data['Media Path'] = self.data['Media Path'].fillna('No Media file')
        self.data = self.data.dropna(subset=['Date'])

        
        self.data.to_csv('cleaned_data.csv',index=False)
        logging.info("Data cleaned and transformed")


if __name__ == "__main__":
    data = pd.read_csv('../scraping/telegram_data.csv')
    dct = DataCleaningTransformation(data)
    dct.clean_data()