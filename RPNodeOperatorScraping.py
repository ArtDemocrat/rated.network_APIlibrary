from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import moralis_ENStoHEX  # Import ENStoHEX script as a module

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Replace 'url' with the actual URL of the website
url = 'https://rocketscan.io/nodes'  # Replace with the website URL you are scraping

driver.get(url)

try:
    # Wait for the presence of the button using its CSS selector
    wait = WebDriverWait(driver, 10)
    show_more_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="button"]')))

    # Use JavaScript to click the button and load more content
    driver.execute_script("arguments[0].click();", show_more_button)

    # Wait for the additional content to load (you may adjust the time as needed)
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'button[type="button"]')))

    # Locate all <a> elements containing "/node/" in their href attribute
    a_elements = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/node/"]')

    # Create a list to store the extracted text strings and addresses
    extracted_elements = []

    # Extract the text from the first 50 <a> elements and add to the list
    for i, a_element in enumerate(a_elements[:50]):  # Scrape the first 50 elements, or replace with a_element in enumerate(a_elements): to cover all results
        extracted_text = a_element.text
        extracted_elements.append(extracted_text)

        # Print the extracted text
        print(f"Element {i + 1}: {extracted_text}")

    # Separate the elements into '0x', '.eth', and other elements
    hex_elements = [text for text in extracted_elements if text.startswith("0x") and not text.endswith(".eth")]
    eth_elements = [text for text in extracted_elements if text.endswith(".eth")]
    other_elements = [text for text in extracted_elements if not text.startswith("0x") and not text.endswith(".eth")]

    # Process the non-'0x', non-'*.eth', and exceptions elements using Script 2
    processed_non_hex_eth_elements = []
    for element in other_elements + eth_elements:
        processed_result = moralis_ENStoHEX.process_element(element)
        processed_non_hex_eth_elements.append(processed_result)

    # Combine the '0x', processed non-'0x', non-'*.eth', and exceptions elements into a single list
    final_elements = hex_elements + processed_non_hex_eth_elements

    # Print the combined elements in the CLI
    for i, element in enumerate(final_elements):
        print(f"Processed Element {i + 1}: {element}")

    # Define the path for the JSON file
    json_path = "combined_data.json"

    # Write the combined elements list to a JSON file
    with open(json_path, 'w') as json_file:
        json.dump(final_elements, json_file)

    print(f"Data saved to {json_path}")

except Exception as e:
    print(f"An error occurred: {str(e)}")

# Close the browser when done.
driver.quit()
