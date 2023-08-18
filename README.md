# Drones Demo FastAPI Project

This is a FastAPI project that provides an API to retrieve location information.

## Getting Started

Follow these steps to set up and run the project.

### Prerequisites

- Python 3.10.x
- Docker (optional, for running with Docker Compose)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/drones-demo.git
   cd drones-demo/api
   ```

### Running Locally

1. Install virtual environment

```sh
pip install virtualenv
```

2. Create and activate a virtual environment

```sh
python3.10 -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

3. Install the required dependencies

```sh
pip install -r requirements.txt
```

4. Start the FastAPI development server

```sh
python main.py
```

The API will be accessible at http://localhost:8000.

### Running with Docker Compose

1. Build and start the Docker containers:

```sh
docker-compose up
```

The FastAPI application will be accessible at http://localhost:8000.

### Running with Docker Compose Build

1. Build and start as Docker containers:

```sh
docker-compose build
docker run -d -p 8000:8000 -e SECTOR_ID=10 drones_demo-app:latest

```

The FastAPI application will be accessible at http://localhost:8000.


### Running Apis Tests

To run the tests, execute the following command:

navigate to the `api` folder and run:

```sh
cd api
source venv/bin/activate # On Windows: venv\Scripts\activate
python -m pytest tests/
```

### Running Client Tests

If you have test cases in the `client` folder that require the FastAPI server to be running, follow these steps:

1. Start the FastAPI development server (if not already running):

```sh
python main.py
```

2. Open a new terminal window and navigate to the `client` folder:

```sh
cd client
```

3. Run the client test cases:

```sh
source venv/bin/activate # On Windows: venv\Scripts\activate
pytest
```

## API Endpoints

- **POST /v1/get_location**: Retrieves location information based on input data.

## Sample CURL

curl 'http://localhost:8000/v1/get_location' \
   --header 'Content-Type: application/json' \
   --data '{"x":"123.12","y":"456.56","z":"789.89","velocity":"20.0"}'
