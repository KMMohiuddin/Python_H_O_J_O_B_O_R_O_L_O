import requests
import csv
from bs4 import BeautifulSoup

def scrape_monthly_data(month):

    url = f"https://www.bb.org.bd/en/index.php/financialactivity/mfsdata/{month}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    table = soup.find('table')
    
    # Extract data from the table
    data = []
    for row in table.find_all('tr'):
        row_data = []
        for cell in row.find_all('th'):
            row_data.append(cell.text.strip())
        if row_data:
            data.append(row_data)
        for cell in row.find_all('td'):
            row_data.append(cell.text.strip())
        if row_data:
            data.append(row_data)
    
    return data

def create_event(month):
    # Scrape the data for the given month
    data = scrape_monthly_data(month)
    
    # Define the filename for the CSV
    filename = f"{month}_data.csv"
    
    # Write the data to the CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    
    print(f"Event created for {month}. Data saved in {filename}.")

# Define the months for which you want to create events and scrape data
months = ['january', 'february', 'march']  # Add more months as needed

# Create events and scrape data for each month
for month in months:
    create_event(month)
