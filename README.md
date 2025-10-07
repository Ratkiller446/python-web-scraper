<!-- Space for project banner/logo image -->

# 🕷️ Python Web Scraper

<div align="center">

[![License](https://img.shields.io/badge/License-BSD_2--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

**Advanced Python web scraper with intelligent metadata extraction and recursive link following capabilities**

</div>

---

## 📖 Description

Python Web Scraper is a powerful and flexible web scraping tool designed for extracting comprehensive data from websites. Built with modern Python libraries, this scraper goes beyond basic HTML parsing by intelligently extracting metadata, following links recursively, and providing structured output that's ready for analysis.

Whether you're conducting research, building datasets, or analyzing web content, this tool provides a robust foundation for your web scraping needs.

## ✨ Features

- **🔍 Intelligent Content Extraction**: Automatically extracts page titles, descriptions, and main content
- **🔗 Recursive Link Following**: Configurable depth-based crawling to discover and scrape related pages
- **📊 Metadata Extraction**: Captures meta tags, Open Graph data, and other structured metadata
- **⚡ Efficient Processing**: Built-in request throttling and error handling for reliable operation
- **📝 Structured Output**: Clean, organized data output suitable for further processing
- **🛡️ Robust Error Handling**: Gracefully manages network errors, timeouts, and malformed HTML
- **🎯 Customizable Scraping**: Easy to extend and modify for specific scraping requirements

## 🚀 Usage

### Basic Scraping

```python
from web_scraper import WebScraper

# Initialize the scraper
scraper = WebScraper()

# Scrape a single page
data = scraper.scrape('https://example.com')
print(data)
```

### Advanced Scraping with Link Following

```python
from web_scraper import WebScraper

# Initialize scraper with custom settings
scraper = WebScraper(
    max_depth=2,
    delay=1.0,
    follow_external_links=False
)

# Scrape with recursive link following
results = scraper.scrape_recursive('https://example.com', max_pages=50)

# Process results
for url, data in results.items():
    print(f"URL: {url}")
    print(f"Title: {data['title']}")
    print(f"Description: {data['description']}")
    print("---")
```

### Extracting Specific Metadata

```python
from web_scraper import WebScraper

scraper = WebScraper()
data = scraper.scrape('https://example.com')

# Access extracted metadata
print(f"Page Title: {data.get('title')}")
print(f"Meta Description: {data.get('meta_description')}")
print(f"Links Found: {len(data.get('links', []))}")
print(f"Images: {data.get('images')}")
```

## 📋 Requirements

- **Python**: 3.6 or higher
- **Dependencies**:
  - `requests` - HTTP library for making web requests
  - `beautifulsoup4` - HTML parsing and navigation
  - `lxml` - Fast XML and HTML parser
  - `urllib3` - HTTP client (typically included with requests)

### Installation

```bash
# Clone the repository
git clone https://github.com/Ratkiller446/python-web-scraper.git
cd python-web-scraper

# Install dependencies
pip install -r requirements.txt
```

## 🤝 Contribution

Contributions are welcome and greatly appreciated! Here's how you can contribute:

1. **Fork the Repository**: Click the 'Fork' button at the top right of this page
2. **Create a Feature Branch**: 
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Make Your Changes**: Implement your feature or bug fix
4. **Commit Your Changes**: 
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
5. **Push to the Branch**: 
   ```bash
   git push origin feature/AmazingFeature
   ```
6. **Open a Pull Request**: Submit your changes for review

### Contribution Guidelines

- Write clear, commented code
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Be respectful and constructive in discussions

## 📄 License

This project is licensed under the **BSD 2-Clause License** - see the [LICENSE](LICENSE) file for details.

The BSD 2-Clause License is a permissive license that allows you to freely use, modify, and distribute this software, as long as you include the original copyright notice and disclaimer.

---

<div align="center">

**Built with ❤️ by the Python Web Scraper Team**

[Report Bug](https://github.com/Ratkiller446/python-web-scraper/issues) · [Request Feature](https://github.com/Ratkiller446/python-web-scraper/issues)

</div>
