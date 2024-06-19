# Google-maps-scraper
This project uses ```Selenium``` to scrape information about(hotels, shops, restruants etc.) from Google Maps. The data includes the name, google maps location, phone number, rating, and number of reviews for each result. The collected data is then saved to an Excel file.

## Prerequisites

To run this script, you'll need the following:

- Python 3.6 and above
- Google Chrome browser
- ChromeDriver compatible with your Chrome version
- The following Python packages:
  - selenium
  - pandas

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/x0120/Google-map-scraper.git
   cd Google-map-scraper
2. **Install the required Python packages:**

    ```
    pip install selenium pandas
    ```
3. **Download and install ChromeDriver:**
   - Download the ChromeDriver from <a href="https://googlechromelabs.github.io/chrome-for-testing/#stable" target="_blank">here</a>.
   - Extract the downloaded file and note the path to chromedriver.exe.
5. **Update the script with the path to your ChromeDriver:**
   
   In scraper.py, update the path to ChromeDriver:
   ```
   service = Service('path/to/chromedriver.exe')  # Update this path
   ```
   
## Usage
Run the script:

Then write what do you want to search for and the name of the generated output file

```
$ python scraper.py                                                          
What do you want to search for:
hotels in Muscat
What name do you want for the Excel file(without .xlsx):
hotels in Muscat
```

Then :
1. chromedriver.exe will run and start to search for ```hotels in Muscat```
2. Then you have to <b>Manully scroll down to load more results.</b>
3. The program will go over all results and save them in Excel file named ```hotels in Muscat.xlsx```

## Notes
- You will have <b>50</b> seconds to load all results as you can see here in the code. But you can modifiy it as needed
  ```
    # Wait (seconds) to Scroll down to load more results (wait as needed)
    time.sleep(50)
  ```
- The script uses fixed sleep intervals to wait for elements to load. Depending on your internet speed, you might need to adjust these intervals.
- Ensure your Chrome browser and ChromeDriver are compatible.


