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

    # Create a list to store the extracted text strings
    extracted_texts = []

    # Extract the text from all <a> elements and add to the list
    for i, a_element in enumerate(a_elements):
        extracted_text = a_element.text
        extracted_texts.append(extracted_text)

        # Print the extracted text
        print(f"Element {i + 1}: {extracted_text}")

    # Define the path for the JSON file
    json_path = "extracted_data.json"

    # Write the extracted text list to a JSON file
    with open(json_path, 'w') as json_file:
        json.dump(extracted_texts, json_file)

    print(f"Data saved to {json_path}")

except Exception as e:
    print(f"An error occurred: {str(e)}")

# Close the browser when done.
driver.quit()
