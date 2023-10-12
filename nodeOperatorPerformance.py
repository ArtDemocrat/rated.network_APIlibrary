# hits rocketscan.io API to download and dedupe all node operator addresses (i.e. deposit addresses)
# passes the downloaded data to the rated.network /operators/ endpoint to get node operator-level performance data

import os
import csv
import requests
import json
import subprocess

# Define the directory path where the CSV files are stored
output_directory = r"C:/mypath"

# Define the list of URLs and headers
endpoints = []

# Define fieldnames based on the columns you want in the CSV
fieldnames = [
    'from', 'to', 'size', 'granularity', 'filterType', 'hour', 'day', 'startDay', 'endDay', 'startEpoch', 'endEpoch',
    'id', 'idType', 'validatorCount', 'avgInclusionDelay', 'avgUptime', 'avgCorrectness', 'avgProposerEffectiveness',
    'avgValidatorEffectiveness', 'totalUniqueAttestations', 'sumCorrectHead', 'sumCorrectTarget', 'sumInclusionDelay',
    'sumProposedCount', 'sumProposerDutiesCount', 'slashesCollected', 'slashesReceived', 'sumEarnings',
    'sumEstimatedRewards', 'sumEstimatedPenalties', 'networkPenetration', 'sumPriorityFees', 'sumBaselineMev',
    'sumMissedExecutionRewards', 'sumConsensusBlockRewards', 'sumMissedConsensusBlockRewards', 'sumAllRewards',
    'sumCorrectSource', 'avgAttesterEffectiveness', 'sumMissedSyncSignatures', 'sumSyncCommitteePenalties',
    'sumLateSourceVotes', 'sumWrongTargetVotes', 'sumLateTargetVotes', 'sumWrongTargetPenalties',
    'sumLateTargetPenalties', 'sumMissedAttestations', 'sumMissedAttestationPenalties', 'sumWrongHeadVotes',
    'sumWrongHeadPenalties', 'sumAttestationRewards', 'sumLateSourcePenalties', 'sumExecutionProposedEmptyCount',
    'sumMissedAttestationRewards', 'sumMissedSyncCommitteeRewards', 'sumExternallySourcedExecutionRewards'
]

# Create a list to store data from individual CSVs
all_data = []

# Function to make a GET request and return response data
def make_request(endpoint_info):
    try:
        response = requests.get(endpoint_info['url'], headers=endpoint_info['headers'])
        response.raise_for_status()  # Raise an exception if the request is not successful

        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return {}

# Execute "curl 1" and process the output
curl_command = 'curl "https://rocketscan.io/api/mainnet/minipools/all" | jq -r ".[] | [.address, .nodeAddress, .pubkey, .validator.index] | @csv"'

# Capture the output of "curl 1"
curl_output = subprocess.check_output(curl_command, shell=True, universal_newlines=True)
curl_output_lines = curl_output.split('\n')  # Split the output into lines

# Process the first 50 lines
processed_elements = set()  # Keep track of processed second elements
for i, line in enumerate(curl_output_lines):
    if i >= 50:
        break  # Stop processing after the first 50 lines

    # Split the line into elements
    elements = line.strip().strip('"').split(',')

    if len(elements) >= 2:
        second_element = elements[1].strip('"')  # Remove double quotes from the second element

        # Check if the second element is not a duplicate
        if second_element not in processed_elements:
            processed_elements.add(second_element)

            # Build the URL for "script 1" with the extracted value
            url = 'https://api.rated.network/v0/eth/operators/{}/effectiveness?filterType=datetime&from=2023-10-12&granularity=day&size=1'.format(second_element)

            endpoints.append({
                'url': url,
                'filename': 'single_validator_effectiveness_{}.csv'.format(i),
                'headers': {
                    'accept': 'application.json',
                    'X-Rated-Network': 'mainnet',
                    'Authorization': 'Bearer myAPItoken'
                }
            })

# Execute each request and save the responses as CSV files
for endpoint_info in endpoints:
    data = make_request(endpoint_info)
    all_data.append(data)

# Define the directory path for the output CSV file
output_csv_file = os.path.join(output_directory, 'operatorperformanceoutput.csv')

# Prepare data for the CSV
csv_data = []

for data in all_data:
    csv_row = {}
    if 'page' in data:
        page_data = data['page']
        csv_row.update(page_data)

    if 'data' in data:
        data_data = data['data']
        for entry in data_data:
            csv_row.update(entry)

    csv_data.append(csv_row)

# Write the nested data as separate columns in the CSV
with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()

    for data in csv_data:
        csv_writer.writerow(data)

print(f'All data saved to {output_csv_file}')
