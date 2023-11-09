import requests
from bs4 import BeautifulSoup

# List of websites to scrape
websites = [
    'https://www.google.com',
    'https://finance.yahoo.com',
    # Add more websites here
]

# Function to scrape a website and save its content to a text file
def scrape_and_save_to_txt(url, filename):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the content you want from the webpage and replace newlines with spaces
        website_content = soup.get_text().replace('\n', ' ')

        # Save the content to a text file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(website_content)

        print(f'Successfully scraped and saved {url} to {filename}')

    except Exception as e:
        print(f'Error scraping {url}: {str(e)}')

# Loop through the list of websites and scrape each one
for index, website in enumerate(websites):
    filename = f'/webData/website_{index}.txt'
    scrape_and_save_to_txt(website, filename)