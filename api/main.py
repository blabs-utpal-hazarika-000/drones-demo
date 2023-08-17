import uvicorn
from fastapi import FastAPI
from decouple import config
from routes import router as main_router
from utils.logger import setup_logger

# Create a FastAPI app instance
app = FastAPI()

# Include the main router
app.include_router(main_router)

# Setup logger
setup_logger()

# Get the port from environment variables (or use the default value 8000)
port = config("PORT", default=8000, cast=int)

if __name__ == "__main__":
    # Run the FastAPI app using uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)

    