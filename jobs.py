from pymongo import MongoClient
import os
from logger import get_logger

logger = get_logger()


def add_to_db(obj, collection_name):
    client = __get_mongo_client()
    db = client[os.environ['DB_NAME']]
    collection = db[collection_name]

    result = collection.insert_one(obj)

    logger.info(f'result: {format(result.inserted_id)}')

    return result


def __get_mongo_client():
    client = MongoClient('mongo', 27017)

    return client

