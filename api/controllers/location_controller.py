import os
from utils.logger import get_logger

# Get the logger instance
logger = get_logger()

def retrieve_location(location_data: dict, sector_id: int):
    # Calculate the location using the provided formula
    loc = (location_data["x"] + location_data["y"] + location_data["z"]) * sector_id + location_data["velocity"]

    logger.info("retrieve_location function called")
    
    return {"loc": loc}