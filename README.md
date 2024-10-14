# MongoDB to DynamoDB JSON Converter

This Python script converts JSON files exported from MongoDB into a format compatible with DynamoDB. The script processes all JSON files located in the `input` folder and saves the converted data into the `output` folder.

## Features

- Converts MongoDB-specific `_id.$oid` field to a simple `_id` string.
- Converts MongoDB date fields (`createdAt`, `updatedAt`) from `$date` objects into ISO string or numeric format.
- Prepares the data for DynamoDB compatibility, ensuring that the structure and data types align with DynamoDB's requirements.

## Requirements

- Python 3.x

## Examples

### Input

```
[
    {
        "_id": {"$oid": "605c72f5e8d3f10b8d6e54d1"},
        "createdAt": {"$date": "2023-04-12T10:00:00Z"},
        "updatedAt": {"$date": "2023-04-13T11:30:00Z"}
    }
]
```

### Output

```
[
    {
        "_id": "605c72f5e8d3f10b8d6e54d1",
        "createdAt": "2023-04-12T10:00:00Z",
        "updatedAt": "2023-04-13T11:30:00Z"
    }
]
```

## Usage

1. Place all MongoDB-exported JSON files in the `input` folder.
2. Run the script:
   ```bash
   python main.py
   ```
