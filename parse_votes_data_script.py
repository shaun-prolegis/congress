# python parse_votes_data_script.py
import os
import json

script_directory = os.path.dirname(os.path.abspath(__file__))
data_array = []

for root, dirs, files in os.walk(script_directory):
    for file_name in files:
        # Check if the file ends with '.json'
        if file_name.endswith(".json"):
            # Create the full path to the JSON file
            json_file_path = os.path.join(root, file_name)

            # Now you can work with the JSON file
            with open(json_file_path, "r") as json_file:
                data = json.load(json_file)
                data_array.append(data)

# Convert data_array to a string representation
data_str = "\n".join(json.dumps(data) for data in data_array)

#
# # Print the data
# print(data_array[0])
