import json
import os
from datetime import datetime


# Create output folder if it doesn't exist
if not os.path.exists("output"):
    os.makedirs("output")


def transform_data(item, date, id=True):
    # Changes _id.$oid by _id
    if id:
        if "_id" in item.keys():
            item['_id'] = item['_id']['$oid']
    
    # Converts dates to ISO strings
    if date == "iso":
        if "createAt" in item.keys():
            item['createdAt'] = item['createdAt']['$date']
            item['updatedAt'] = item['updatedAt']['$date']
    
    # Converts to numeric timestamps
    elif date == "numeric":
        if "createAt" in item.keys():
            item['createdAt'] = datetime.fromisoformat(item['createdAt'].replace('Z', '+00:00')).timestamp()
            item['updatedAt'] = datetime.fromisoformat(item['updatedAt'].replace('Z', '+00:00')).timestamp()

    return item

# Process every JSON file inside the input folder
for filename in os.listdir("input"):
    if filename.endswith('.json'):  # Only process .json files
        input_file_path = os.path.join("input", filename)
        output_file_path = os.path.join("output", filename)
        
        # Read JSON file
        with open(input_file_path, 'r') as infile:
            data = json.load(infile)
        
        # Transform data
        transformed_data = [transform_data(item, date="iso") for item in data]
        
        # Saves transformed JSON file in the output folder
        with open(output_file_path, 'w') as outfile:
            json.dump(transformed_data, outfile, indent=4)
        
        print(f"File '{filename}' transformed y saved in '{output_file_path}'.")

print("Transform process completed!")