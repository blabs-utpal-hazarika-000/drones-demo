from fastapi.testclient import TestClient

from main import app

# Create a TestClient instance to test the FastAPI app
client = TestClient(app)

def test_success_location_calculation():
    """
    Test the successful calculation of the location based on provided data.

    This test case sends a POST request to the /v1/get_location endpoint
    with valid input data and checks if the calculated "loc" value matches
    the expected result.
    """

    # Sending a POST request to the /v1/get_location endpoint
    response = client.post(
        "/v1/get_location",
        json={
            "x": "2",
            "y": "3",
            "z": "4",
            "velocity": "10",
        },
    )
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    # Get the JSON data from the response
    data = response.json()
    # Check if the "loc" key exists in the response JSON
    assert "loc" in data
    # Check the calculated "loc" value
    assert data["loc"] == (2 + 3 + 4) * 5 + 10

def test_missing_required_fields():
    """
    Test the behavior when required fields are missing.

    This test case sends a POST request to the /v1/get_location endpoint
    with missing required fields and checks if the response status code is
    correctly set to 422 (Unprocessable Content).
    """

    # Sending a POST request to the /v1/get_location endpoint
    response = client.post(
        "/v1/get_location",
        json={
            "x": "2",
            "z": "4",
            "velocity": "10",
        },
    )

    # Check if the response status code is 422 (Unprocessable Content)
    assert response.status_code == 422
