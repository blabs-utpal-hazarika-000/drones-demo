from fastapi import APIRouter, HTTPException
from controllers.location_controller import retrieve_location
from models.location_model import LocationInput
from utils.logger import get_logger
from utils.conversion_utils import convert_to_float
from decouple import config


# Create the location router
router = APIRouter()

# Get the logger instance
logger = get_logger()

# Get the sector ID from environment variables (or use the default value 5)
sector_id = config("SECTOR_ID", default=5, cast=int)

@router.post("/get_location")
def get_location(location_data: LocationInput):
    logger.info("Received request to retrieve location")

    converted_location_data = convert_to_float(location_data.model_dump())
    location = retrieve_location(converted_location_data, sector_id)
    
    logger.info("Location retrieved successfully")
    return location