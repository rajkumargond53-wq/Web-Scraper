import requests
from bs4 import BeautifulSoup
import csv

# 1. Website ka URL (Yeh ek dummy website hai jo scraping practice ke liye bani hai)
url = "http://quotes.toscrape.com/"

print("Website se data fetch kiya jaa raha hai...")

# 2. Website ko request bhejna aur HTML page download karna
response = requests.get(url)

# 3. HTML data ko BeautifulSoup ki madad se parse (read) karna
soup = BeautifulSoup(response.text, 'html.parser')

# 4. Page mein se 'quotes' aur 'authors' ko unke HTML class tag ke basis par dhundhna
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

# 5. Extract kiye gaye data ko ek list mein format karna
scraped_data = []
for i in range(len(quotes)):
    quote_text = quotes[i].text
    author_name = authors[i].text
    scraped_data.append([quote_text, author_name])
    print(f"Bala gaya: {author_name} ka quote.")

# 6. Data ko CSV (Excel) file mein save karna
filename = "quotes_data.csv"
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author'])  # Excel ki Heading
    writer.writerows(scraped_data)        # Saara data likhna

print(f"\n✅ Data successfully scrape ho gaya aur '{filename}' mein save ho gaya hai!")
