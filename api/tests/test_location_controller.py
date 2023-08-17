import unittest
from controllers.location_controller import retrieve_location
import os

class TestLocationController(unittest.TestCase):

    def test_retrieve_location(self):
        """
        Test the retrieve_location function with valid location data.

        This test case uses the retrieve_location function to calculate
        the location based on provided data and sector_id. It checks if
        the calculated "loc" value matches the expected result.
        """
        
        # Test data
        location_data = {"x": 1, "y": 2, "z": 3, "velocity": 4}

        # Call the function
        result = retrieve_location(location_data, 10)

        # Assertions
        self.assertEqual(result, {"loc": 64})

    def test_retrieve_location_invalid_value(self):

        # Test data with an invalid float value
        location_data = {"x": "1", "y": 2, "z": 3, "velocity": 4}

        # Call the function
        try:
            retrieve_location(location_data, 5)
        except TypeError as e:
            error_message = str(e)
            self.assertEqual(error_message, 'can only concatenate str (not "int") to str')

if __name__ == "__main__":
    unittest.main()
