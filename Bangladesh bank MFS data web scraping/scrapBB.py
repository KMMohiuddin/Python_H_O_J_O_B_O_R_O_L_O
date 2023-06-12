from bs4 import BeautifulSoup
import requests
import csv
# Send a GET request to the website
url = 'https://www.bb.org.bd/en/index.php/financialactivity/mfsdata'
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')
    ths = table.find_all('th')
    tds = table.find_all('td')


    # Open a CSV file for writing
    with open('BB_table_data2.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        for row in rows:
            cells = row.find_all('th')
            csvwriter.writerow([cell.get_text() for cell in cells])

        for row in rows:
            cells = row.find_all('td')
            csvwriter.writerow([cell.get_text() for cell in cells])

    print("Scraping and CSV conversion complete.")
else:
    # Handle the case when the request was not successful
    print(f"Request failed with status code {response.status_code}")
