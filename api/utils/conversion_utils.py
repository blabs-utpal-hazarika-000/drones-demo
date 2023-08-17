def convert_to_float(location_dict: dict) -> dict:
    """
    Convert values in a dictionary to float and return the converted dictionary.
    """
    converted_dict = {}
    for key, value in location_dict.items():
        try:
            converted_value = float(value)
            converted_dict[key] = converted_value
        except ValueError:
            raise ValueError(f"Invalid float value for key '{key}': {value}")
    return converted_dict
