import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from datetime import datetime

# Sending a request to the website
url = 'https://kalimatimarket.gov.np/'
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the table in the HTML
    table = soup.find('table')
    
    if table:
        # Extracting the table headers
        headers = [header.text.strip() for header in table.find_all('th')]
        rows = table.find_all('tr')
        
        # Extracting table rows
        data = []
        for row in rows[1:]:
            cols = row.find_all('td')
            row_data = [col.text.strip() for col in cols]
            data.append(row_data)

        # Print result in terminal if you want 
        # print("Data extracted:")
        # for row in data:
            # print(row)

        # Save data in csv File
        filename = f"{datetime.now().strftime('%Y%m%d')}_market.csv"
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)
        print(f"Data saved to {filename}")

         
        # Create DataFrame and save to Excel
        df = pd.DataFrame(data, columns=headers)
        filename = f"{datetime.now().strftime('%Y%m%d')}_market.xlsx"
        df.to_excel(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print("Table not found.")
else:
    print(f"Failed to retrieve the page, status code: {response.status_code}")
