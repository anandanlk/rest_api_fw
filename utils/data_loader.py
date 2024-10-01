import json
import os
import logging

def load_json_data(file_path):
    try:
        logging.info(f"Loading data from {file_path} json file")
        with open(file_path) as f:
            data = json.load(f)
            logging.info(f"Data loaded successfully from {file_path}")
            return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file: {file_path}")
    except Exception as e:
        logging.error(f"An error occurred while loading data from {file_path}: {e}")

def get_relative_path(filename):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, '..', 'data', filename)

def user_data():
    return load_json_data(get_relative_path('user_data.json'))

def invalid_user_data():
    return load_json_data(get_relative_path('invalid_user_data.json'))

def booking_data():
    return load_json_data(get_relative_path('booking_data.json'))
