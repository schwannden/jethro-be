import motor.motor_asyncio
from beanie import init_beanie
from fastapi.logger import logger
from google.cloud import firestore


# initializing firestore
firestore_db = firestore.Client("wlchurch")
fs_collection = firestore_db.collection("service_schedule")
