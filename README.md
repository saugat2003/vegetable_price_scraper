# Vegetable Price Scraper

This project is a web scraper designed to extract market price data from the Kalimati Market website. The extracted data is saved in both CSV and Excel formats for further analysis.

## Features
- Scrapes the latest market price data from [Kalimati Market](https://kalimatimarket.gov.np/)
- Extracts table headers and data from the website
- Saves the data into a CSV file
- Saves the data into an Excel file

## Prerequisites
Before running the script, ensure you have the following installed:

- Python 3.x
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `openpyxl`

You can install the required dependencies using:
```bash
pip install requests beautifulsoup4 pandas openpyxl
```

## How to Use
1. Clone this repository or copy the script.
2. Run the script:
   ```bash
   python scraper.py
   ```
3. If the website is accessible, the script will extract data and save it in:
   - A CSV file named `YYYYMMDD_market.csv`
   - An Excel file named `YYYYMMDD_market.xlsx`

## Output
The extracted data is saved with a timestamped filename (format: YYYYMMDD) to keep track of daily market price changes.

## Error Handling
- If the website is not accessible, an error message with the HTTP status code will be displayed.
- If the expected table is not found on the page, a message will be printed indicating that no data was retrieved.

## License
This project is open-source and available under the MIT License.

