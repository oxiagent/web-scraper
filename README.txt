This script is designed to scrape product information from Rozetka webpage (product category: mobile phones) and save the results into a CSV file. It extracts the product name, old price, and new price.

Required:

- Python 3.6 or higher
- Libraries:
  - `requests`
  - `beautifulsoup4`

Install dependencies: Use pip to install the required libraries:
    pip install requests beautifulsoup4

Clone or download this repository: 
   git clone https://github.com/oxiagent/web-scraper.git
   cd web-scraper


Run the Script
   1. Open a terminal and navigate to the directory where the scrape.py script is located:
cd /path/to/directory
   2.Run the script with the following command:
python3 scrape.py --url "https://rozetka.com.ua/ua/promo/stmykday/?gad_source=1&section_id=80003" --output "/path/to/results.csv"


Output
The script will create a CSV file with the following structure (fields):
   1. Product name
   2. Old price
   3. New price
NOTE: If there is no value, it means the value was not found (it does not exists).

Troubleshooting
   1. File Not Found Error: Ensure that you are in the correct directory and the file path to the script or output is correct.
   2. Dependencies Missing: If you encounter import errors, ensure that the required libraries are installed 
   3. Invalid URL: Ensure the URL is valid and points to a Rozetka webpage https://rozetka.com.ua/ua/promo/stmykday/?gad_source=1&section_id=80003
