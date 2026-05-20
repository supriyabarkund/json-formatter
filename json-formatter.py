import json
import sys

def main():
    raw_json = input("Enter raw JSON string: ")
    try:
        parsed_json = json.loads(raw_json)
        formatted_json = json.dumps(parsed_json, indent=4)
        print("Formatted JSON:")
        print(formatted_json)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
if __name__ == "__main__":
    main()