import requests
from bs4 import BeautifulSoup
import concurrent.futures
from typing import List
from .pdf_reader import PdfReader

# Single Responsibility Principle (SRP):
# This class follows SRP by handling only the responsibilities related to web scraping.


class WebScraper:
    def __init__(self):
        self.errors = []

    def scrape_url(self, url: str) -> str:
        """Scrapes content from a given URL."""
        try:
            response = requests.get(url)
            response.raise_for_status()  # Handle HTTP errors
            return response.text
        except requests.RequestException as e:
            self.errors.append(f"Error scraping URL {url}: {e}")
            return ""

    def scrape_urls_parallel(self, urls: List[str]) -> List[str]:
        """Scrapes content from multiple URLs in parallel."""
        scraped_data = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_url = {executor.submit(self.scrape_url, url): url for url in urls}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    data = future.result()
                    scraped_data.append(data)
                except Exception as e:
                    self.errors.append(f"Error scraping URL {url}: {e}")
        return scraped_data

    def scrape_pdf(self, file_path: str) -> str:
        """Scrapes text content from a PDF file."""
        pdf_reader = PdfReader()
        return pdf_reader.read_text(file_path)
