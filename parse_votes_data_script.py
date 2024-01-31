# python parse_votes_data_script.py
import subprocess
import os
import json

result = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, text=True)

print(result.stdout)

script_directory = os.path.dirname(os.path.abspath(__file__))
print("Script Directory:", script_directory)

for root, dirs, files in os.walk(script_directory):
    for file_name in files:
        # Check if the file ends with '.json'
        if file_name.endswith(".json"):
            # Create the full path to the JSON file
            json_file_path = os.path.join(root, file_name)

            # Now you can work with the JSON file
            with open(json_file_path, "r") as json_file:
                data = json.load(json_file)
                # Process the JSON data as needed
                print("Found JSON file:", json_file_path)
                print("JSON data:", data)
