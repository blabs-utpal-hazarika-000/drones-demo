import unittest
import requests

class TestAPI(unittest.TestCase):
    """
    Test class for testing the Location API.

    This class contains test cases to verify the behavior of the
    '/v1/get_location' API endpoint.
    """

    def test_get_location_api(self):
        """
        Test the '/v1/get_location' API with valid location data.
        """
        url = "http://localhost:8000/v1/get_location"
        
        # Sample location data
        location_data = {
            "x": "1",
            "y": "2",
            "z": "3",
            "velocity": "4"
        }

        response = requests.post(url, json=location_data)
        
        # Check response status code
        self.assertEqual(response.status_code, 200)
        
        # Check response content
        expected_response = {"loc": 34.0}
        self.assertEqual(response.json(), expected_response)

    def test_get_location_api_invalid_api(self):
        """
        Test the '/v1/get_location' API with invalid location data.
        """
        
        url = "http://localhost:8000/v1/get_location"
        
        # Sample location data
        location_data = {
            "x": "a",
            "y": "2",
            "z": "3",
            "velocity": "4"
        }

        response = requests.post(url, json=location_data)
        
        # Check response status code
        self.assertEqual(response.status_code, 422)
        
if __name__ == "__main__":
    unittest.main()





