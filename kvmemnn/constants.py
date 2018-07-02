import os

current_filepath = os.path.dirname(os.path.abspath(__file__))

ROOT_PATH = os.path.abspath(os.path.join(current_filepath, os.pardir))
DATA_PATH = os.path.join(ROOT_PATH, 'data/raw/data.csv')
MEMORY_CACHE_PATH = os.path.join(ROOT_PATH, 'cache/memories')
TFIDF_CACHE_PATH = os.path.join(ROOT_PATH, 'cache/tfidf')

MODELS_DIR = os.path.join(ROOT_PATH, 'models/')