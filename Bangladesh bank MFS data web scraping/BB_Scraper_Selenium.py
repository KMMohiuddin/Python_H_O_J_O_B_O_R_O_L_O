from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Set up the Selenium webdriver (ensure you have the appropriate driver installed)
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('https://www.bb.org.bd/en/index.php/financialactivity/mfsdata')

# Wait for the select elements to become visible
select_month = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'select_month')))
select_year = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'select_year')))

# Select the desired month and year
select_month.select_by_value('06')  # June
select_year.select_by_value('2022')  # 2022

# Submit the form to trigger the JavaScript event
form = driver.find_element(By.CLASS_NAME, 'needs-validation')
form.submit()

# Wait for the table to appear
table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'table')))

# Extract table data and write to CSV
with open('table_data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Iterate over the table rows
    rows = table.find_elements(By.TAG_NAME, 'tr')
    for row in rows[1:4]:  # Scraping rows 1 to 3
        # Extract the text from each cell in the row
        cells = row.find_elements(By.TAG_NAME, 'td')
        row_data = [cell.text for cell in cells]

        # Write the row data to the CSV file
        csvwriter.writerow(row_data)

# Close the browser
driver.quit()