# Shows effectiveness percentiles ranking for the last 1D period on a depositAddress level
# Change filter to 1d, 7d, 30d or All-time to get different timeframes of data
# Change filter to poolShare in order to get staking pool-groupped data

import subprocess
import json
import csv
import os

# Define the cURL command to retrieve data
curl_command = 'curl -X "GET" "https://api.rated.network/v0/eth/operators/percentiles?window=1d&idType=depositAddress" -H "accept: application/json" -H "X-Rated-Network: mainnet" -H "Authorization: Bearer myAPIToken" | jq.exe'

# Execute the cURL command and capture the output
curl_output = subprocess.check_output(curl_command, shell=True, universal_newlines=True)

# Parse the JSON data
data = json.loads(curl_output)

# Define the path where the CSV file will be saved
output_directory = r"C:/mypath"
output_csv_filename = "effectivenesspercentilefile.csv"

# Prepare data for the CSV
csv_data = {}

# Iterate over the JSON data and convert it to a dictionary
for item in data:
    for key, value in item.items():
        if key in csv_data:
            csv_data[key].append(value)
        else:
            csv_data[key] = [value]

# Combine the output directory and filename to create the full file path
file_path = os.path.join(output_directory, output_csv_filename)

# Get a list of keys to use as fieldnames
fieldnames = list(csv_data.keys())

# Transpose the data to convert fields to rows
rows = list(zip(*csv_data.values()))

# Save the transposed data as a CSV
with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(fieldnames)
    csv_writer.writerows(rows)

print(f'Results saved to {file_path}')
