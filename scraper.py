from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time



# Function to extract information form google maps
def get_info(driver,search_query):
    results = []
    driver.get('https://www.google.com/maps')
    search_box = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'searchboxinput'))
    )
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Wait (seconds) to Scroll down to load more results (wait as needed)
    time.sleep(50)

    # Extract information from the results
    results_elements = driver.find_elements(By.CLASS_NAME, 'Nv2PK')
    for element in results_elements:
        try:
            try:
                name = element.find_element(By.CLASS_NAME, 'qBF1Pd').text
                print("-"*10)
                print(f"result name: {name}")
            except:
                name = None

            try:
                location_element = element.find_element(By.CLASS_NAME, 'hfpxzc')
                location = location_element.get_attribute('href')
                print(f"result location: {location}")
            except:
                location = None
            
            try:
                rating = element.find_element(By.CLASS_NAME, 'MW4etd').text
                rating = float(rating.split()[0])
                print(f"result rating: {rating}")
            except:
                rating = None
            
            try:
                num_reviews = element.find_element(By.CLASS_NAME, 'UY7F9').text
                num_reviews = int(num_reviews.replace('(', '').replace(')', '').replace(',', ''))
                print(f"result num_reviews: {num_reviews}")
            except:
                num_reviews = None

            # Click on each result to open details
            element.click()
            time.sleep(2)  # Wait for details to load
            # extract information from the result details. you can extract emails,phone numbers,website, and more
            try:
                result_details_elements = driver.find_elements(By.CLASS_NAME, 'Io6YTe')
                phone = None
                for elem in result_details_elements:
                    if elem.text.replace(" ", "").isdigit():
                        phone = elem.text
                        print(f"phone num: {phone}")
                        print('-'*10,end='\n')
                        break
            except:
                phone = None
            
            results.append({
                'Name': name,
                'Location': location,
                'Phone': phone,
                'Rating': rating,
                'Number of Reviews': num_reviews
            })

            # Close the details pane
            close_button = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
            close_button.click()
            time.sleep(2)
            
        except Exception as e:
            continue
    
    return results


def main():

    search_query = input("What do you want to search for:\n")
    output_file_name = input("What name do you want for the Excel file(without .xlsx):\n")
    # Initialize the Chrome driver
    service = Service('path/to/chromedriver.exe')  # Update this path
    driver = webdriver.Chrome(service=service)

    start_time = time.time()
    # Extract data and save to Excel
    all_results_data = get_info(driver,search_query)
    print(f" number of results: {len(all_results_data)}")

    # Create a DataFrame
    df = pd.DataFrame(all_results_data)

    # Save the DataFrame to an Excel file
    df.to_excel(f'{output_file_name}.xlsx', index=False)
    print(f"{output_file_name}.xlsx have been created")
    # End the timer
    end_time = time.time()

    # Calculate and print the total runtime
    total_time = end_time - start_time
    total_in_minuts = round(total_time/60,2)
    print(f"Total run time: {total_in_minuts} seconds")
    # Close the driver
    driver.quit()

if __name__ == "__main__":
    main()
