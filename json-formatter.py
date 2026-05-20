import json
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 json-formatter.py <input-file> <output-file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            parsed_json = json.load(file)

        formatted_json = json.dumps(parsed_json, indent=4)

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(formatted_json)
            file.write("\n")

        print(f"Formatted JSON written to {output_file}")
    except FileNotFoundError:
        print(f"Input file not found: {input_file}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
