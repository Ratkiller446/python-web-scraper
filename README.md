<div align="center">

![Python Web Scraper Logo](./logo.png)

# 🕷️ Python Web Scraper

[![License](https://img.shields.io/badge/License-BSD_2--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause) [![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

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
    timeout=30
)

# Scrape with recursive link following
data = scraper.scrape_recursive('https://example.com', max_depth=2)
for page_data in data:
    print(f"URL: {page_data['url']}")
    print(f"Title: {page_data['title']}")
    print(f"Content Length: {len(page_data['content'])}")
    print("---")
```

### Custom Configuration

```python
from web_scraper import WebScraper

# Configure scraper with custom parameters
scraper = WebScraper(
    user_agent='Custom Bot 1.0',
    max_retries=3,
    delay=2.0,
    timeout=45
)

# Scrape with custom settings
result = scraper.scrape('https://target-website.com')
```

## 📦 Installation

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Installing Dependencies

```bash
# Clone the repository
git clone https://github.com/Ratkiller446/python-web-scraper.git
cd python-web-scraper

# Install required packages
pip install requests beautifulsoup4 lxml
```

### Alternative Installation

```bash
# Install dependencies manually
pip install -r requirements.txt
```

### Usage

```bash
# Run the scraper
python web_scraper.py
```

## 🔧 Configuration

The scraper can be configured with various parameters:

- `max_depth`: Maximum depth for recursive crawling (default: 1)
- `delay`: Delay between requests in seconds (default: 1.0)  
- `timeout`: Request timeout in seconds (default: 30)
- `max_retries`: Maximum number of retry attempts (default: 3)
- `user_agent`: Custom User-Agent string for requests

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** and add tests if applicable
4. **Commit your changes**: `git commit -m 'Add amazing feature'`
5. **Push to the branch**: `git push origin feature/amazing-feature`
6. **Open a Pull Request**

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/python-web-scraper.git
cd python-web-scraper

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
```

## 📋 Requirements

- `requests`: HTTP library for making web requests
- `beautifulsoup4`: HTML/XML parsing library
- `lxml`: Fast XML and HTML parser

## 🐛 Troubleshooting

### Common Issues

- **Connection Timeouts**: Increase the timeout parameter or check network connectivity
- **Rate Limiting**: Increase the delay between requests
- **Blocked Requests**: Try using different User-Agent strings or rotating proxies
- **Memory Issues**: Process data in smaller batches or implement streaming

### Getting Help

- Check the [Issues](https://github.com/Ratkiller446/python-web-scraper/issues) page for known problems
- Create a new issue with detailed information about your problem
- Include error messages, code examples, and expected behavior

## 📄 License

This project is licensed under the BSD 2-Clause License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <sub>Built with ❤️ for the web scraping community</sub>
</div>
