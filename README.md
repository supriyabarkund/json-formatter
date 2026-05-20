# JSON Formatter

A small command-line Python utility that reads raw JSON from a file and writes formatted JSON to another file.

## Requirements

- Python 3

## Usage

Run the script:

```bash
python3 json-formatter.py input.json output.json
```

Example input file:

```json
{"name":"Ada","skills":["math","computing"]}
```

The tool writes formatted JSON to the output file:

```json
{
    "name": "Ada",
    "skills": [
        "math",
        "computing"
    ]
}
```

Invalid JSON input prints a helpful parse error. Missing input files also print a clear error.
