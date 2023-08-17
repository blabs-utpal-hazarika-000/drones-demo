from pydantic import BaseModel, field_validator
from utils.logger import get_logger

# Get the logger instance
logger = get_logger()

class LocationInput(BaseModel):
    # Declare fields for the location input
    x: str
    y: str
    z: str
    velocity: str

    @field_validator("x", "y", "z", "velocity")
    def validate_float_value(cls, value):
        try:
            float(value)
            return value
        except ValueError:
            # Log the error when conversion to float fails
            logger.error(f"Invalid float value: {value}")
            raise ValueError("Invalid float value")

