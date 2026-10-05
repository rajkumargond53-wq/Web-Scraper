Web Scraper
This is a Python-based web scraping script designed to extract data from a specified website and save it into a CSV file (quotes_data.csv).
Description
The script utilizes the requests and BeautifulSoup libraries to fetch HTML content, parse it, and extract specific elements like quotes and author names based on HTML class tags.
How it Works:
 * Sends a URL request to the target website.
 * Parses the HTML content using BeautifulSoup.
 * Identifies and extracts the required tags for quotes and authors.
 * Organizes the extracted data into a structured list.
 * Finally, saves the data to a CSV file.
Requirements
This script requires the following Python libraries:
 * requests
 * beautifulsoup4
You can install them via pip:
pip install requests beautifulsoup4
Usage
 * Open the scraper.py script.
 * Replace the url variable with the URL of the website you want to scrape.
 * Run the script: python scraper.py
