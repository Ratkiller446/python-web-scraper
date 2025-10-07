import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import sys
import re
from typing import Optional, List, Dict

class WebScraper:
    """Advanced web scraper that extracts metadata and links from URLs."""
    
    def __init__(self, timeout: int = 10, user_agent: Optional[str] = None):
        self.timeout = timeout
        self.headers = {
            'User-Agent': user_agent or 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.session = requests.Session()
    
    def validate_url(self, url: str) -> bool:
        """Validate URL format."""
        regex = re.compile(
            r'^https?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return url is not None and regex.search(url) is not None
    
    def fetch_page(self, url: str) -> Optional[BeautifulSoup]:
        """Fetch and parse HTML page."""
        try:
            response = self.session.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def extract_title(self, soup: BeautifulSoup) -> str:
        """Extract page title with fallback strategies."""
        # Try <title> tag
        if soup.title and soup.title.string:
            return soup.title.string.strip()
        
        # Try Open Graph title
        og_title = soup.find('meta', property='og:title')
        if og_title and og_title.get('content'):
            return og_title['content'].strip()
        
        # Try first h1
        h1 = soup.find('h1')
        if h1:
            return h1.get_text().strip()
        
        return "No title found"
    
    def extract_description(self, soup: BeautifulSoup) -> str:
        """Extract page description with fallback strategies."""
        # Try meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            return meta_desc['content'].strip()
        
        # Try Open Graph description
        og_desc = soup.find('meta', property='og:description')
        if og_desc and og_desc.get('content'):
            return og_desc['content'].strip()
        
        # Try first paragraph
        p = soup.find('p')
        if p:
            text = p.get_text().strip()
            return text[:200] + '...' if len(text) > 200 else text
        
        return "No description found"
    
    def extract_links(self, soup: BeautifulSoup, base_url: str, limit: int = 3) -> List[Dict[str, str]]:
        """Extract first N links with text and absolute URLs."""
        links = []
        for a_tag in soup.find_all('a', href=True):
            if len(links) >= limit:
                break
            
            href = a_tag['href'].strip()
            if not href or href.startswith(('#', 'javascript:', 'mailto:')):
                continue
            
            absolute_url = urljoin(base_url, href)
            text = a_tag.get_text().strip() or "[No text]"
            
            links.append({
                'text': text[:100],
                'url': absolute_url
            })
        
        return links
    
    def scrape(self, url: str) -> Dict:
        """Main scraping method."""
        if not self.validate_url(url):
            return {'error': 'Invalid URL format'}
        
        soup = self.fetch_page(url)
        if not soup:
            return {'error': 'Failed to fetch page'}
        
        return {
            'url': url,
            'title': self.extract_title(soup),
            'description': self.extract_description(soup),
            'links': self.extract_links(soup, url)
        }

def main():
    print("=" * 60)
    print("Advanced Web Scraper")
    print("Created by Perplexity.AI")
    print("=" * 60)
    
    scraper = WebScraper()
    
    while True:
        url = input("\nEnter URL to scrape (or 'quit' to exit): ").strip()
        
        if url.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        print("\nScraping...")
        result = scraper.scrape(url)
        
        if 'error' in result:
            print(f"\n❌ Error: {result['error']}")
            continue
        
        print("\n" + "=" * 60)
        print(f"Title: {result['title']}")
        print(f"\nDescription: {result['description']}")
        print(f"\nFirst 3 Links:")
        
        for i, link in enumerate(result['links'], 1):
            print(f"  {i}. {link['text']}")
            print(f"     URL: {link['url']}")
        
        print("=" * 60)

if __name__ == "__main__":
    main()
