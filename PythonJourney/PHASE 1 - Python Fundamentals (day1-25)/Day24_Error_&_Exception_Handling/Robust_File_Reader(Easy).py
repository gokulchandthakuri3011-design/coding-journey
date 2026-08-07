"""
### Assignment 2: Robust File Reader (Easy)

Create `read_json_config(path: str) -> dict` that:
- Returns `{}` if file doesn't exist
- Raises `ValueError` with a clear message if JSON is invalid
- Uses `with` statement for file handling
- Uses exception chaining (`raise ... from`)
"""

import json
from pathlib import Path # imports Path class from pathlib module to handle file paths

# Function to read JSON configuration from a file
def read_json_config(path: str) -> dict:
    try:
        with open(path, 'r', encoding='utf-8') as file: # encoding='utf-8' is text format used to read file that may contain non-ASCII characters
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in file: {path}") from e


def main():
    script_dir = Path(__file__).resolve().parent

    # Test cases for the read_json_config function
    test_cases = [
        script_dir / "non_existent_file.json",  # File doesn't exist
        script_dir / "invalid_json.json",      # Invalid JSON
        script_dir / "valid_json.json"         # Valid JSON
    ]

    for test_case in test_cases:
        try:
            config = read_json_config(str(test_case))
            if config == {}:
                print(f"'{test_case.name}': file missing or empty config")
            else:
                print(f"'{test_case.name}': loaded successfully -> {config}")
        except ValueError as e:
            print(f"'{test_case.name}': {e}")
        except Exception as e:
            print(f"'{test_case.name}': unexpected error -> {e}")

if __name__ == "__main__":
    main()