import os
import csv
import requests
import json

# Define the directory path where CSV files will be stored
output_directory = r"C:/{{CSVOutputDestinationPath}}"

# Define the list of URLs and headers
endpoints = [
    {
        'url': 'https://api.rated.network/v0/eth/validators/566177/effectiveness',
        'filename': 'single_validator_effectiveness.csv',
        'headers': {
            'accept': 'application/json',
            'X-Rated-Network': 'mainnet',
            'Authorization': 'Bearer {{myBearerToken}}'
        }
    }
]

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Function to make a GET request, save response to a file, and print response content for debugging
def make_request_save_response_to_file(endpoint_info, filename):
    try:
        response = requests.get(endpoint_info['url'], headers=endpoint_info['headers'])
        response.raise_for_status()  # Raise an exception if the request is not successful

        try:
            data = response.json()
        except ValueError as ve:
            print(f"Error decoding JSON: {ve}")
            data = {}

        if not data:
            print(f"No data found in the response for {filename}.")
            return

        # If the 'data' field exists in the response and is a JSON array, write each object in the array to a new line
        if 'data' in data and isinstance(data['data'], list):
            data_list = data['data']
        else:
            data_list = []

        if not data_list:
            print(f"No data list found in the response for {filename}.")
            return

        # Combine the output directory and filename to create the full file path
        file_path = os.path.join(output_directory, filename)

        # Save the JSON data as CSV with each object from the 'data' field on a separate line
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=data_list[0].keys())
            csv_writer.writeheader()

            for item in data_list:
                csv_writer.writerow(item)

        print(f'Response data saved to {file_path}')
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

# Execute each request and save the responses as CSV files
for endpoint_info in endpoints:
    make_request_save_response_to_file(endpoint_info, endpoint_info['filename'])
