import pandas as pd
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)

def load_data(path='final.csv'):
    logging.info(f"Trying to load data from: {path}")
    
    if not os.path.exists(path):
        logging.error("CSV file not found!")
        raise FileNotFoundError(f"Could not find the file: {path}")
    
    try:
        df = pd.read_csv(path)
        if df.empty:
            logging.error("CSV file is empty.")
            raise ValueError("CSV file is empty.")
        logging.info("Data loaded successfully.")
        return df
    except pd.errors.EmptyDataError as e:
        logging.error("CSV file is empty or corrupted.")
        raise e
