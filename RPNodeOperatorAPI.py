# downloads node operator addresses (i.e. deposit addresses) and number of minipools from rocketscan.io/nodes, deduplicating the dataset, and ranking large-to-small based on fifth_element (# of minipools)
# run jq.exe -r ".[:50] | .[] | [.address, to show only the first 50 records

import os
import csv
import subprocess

# Define the directory path where the CSV file will be stored
output_directory = r"C:\mypath"
output_csv_filename = "myfile.csv"

# Define the cURL command to retrieve all records
curl_command = 'curl "https://rocketscan.io/api/mainnet/minipools/all" | jq.exe -r ".[] | [.address, .nodeAddress, .pubkey, .validator.index, .node.minipoolActiveCount, .validator.status] | @csv"'

# Execute the cURL command and capture the output
curl_output = subprocess.check_output(curl_command, shell=True, universal_newlines=True)

# Create a list to store records
records = []

# Split the cURL output into lines and process each line
for line in curl_output.split('\n'):
    if line:
        # Split the line into elements
        elements = line.strip('"').split(',')
        if len(elements) >= 4:
            second_element = elements[1].strip('"')  # Remove double quotes
            fifth_element = int(elements[4])  # Convert fifth_element to an integer
            records.append((second_element, fifth_element))

# Deduplicate the records
deduplicated_records = list(set(records))

# Sort the deduplicated records by fifth_element in descending order
sorted_records = sorted(deduplicated_records, key=lambda x: x[1], reverse=True)

# Combine the output directory and filename to create the full file path
file_path = os.path.join(output_directory, output_csv_filename)

# Save the sorted and deduplicated results as a CSV
with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write the header row
    csv_writer.writerow(["second_element", "fifth_element"])

    # Write the sorted records
    for record in sorted_records:
        csv_writer.writerow(record)

print(f'Results saved to {file_path}')
