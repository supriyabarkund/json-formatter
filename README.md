# JSON Formatter

A small command-line Python utility that formats raw JSON input with readable indentation.

## Requirements

- Python 3

## Usage

Run the script:

```bash
python3 json-formatter.py
```

Paste a raw JSON string when prompted:

```text
Enter raw JSON string: {"name":"Ada","skills":["math","computing"]}
```

The tool prints the formatted JSON:

```json
{
    "name": "Ada",
    "skills": [
        "math",
        "computing"
    ]
}
```

Invalid JSON input prints a helpful parse error.
