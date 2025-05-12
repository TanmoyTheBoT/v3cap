# v3cap

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/) [![PyPI version](https://badge.fury.io/py/v3cap.svg)](https://badge.fury.io/py/v3cap) [![PyPI Downloads](https://static.pepy.tech/badge/v3cap)](https://pepy.tech/projects/v3cap)

</div>

Solve reCAPTCHA v3 challenges automatically - Python package with API support.

## ⚡ Installation
```bash
pip install v3cap
```

## 🚀 Usage

### Python Package
```python
from v3cap.captcha import get_recaptcha_token

token = get_recaptcha_token(
    site_key="YOUR_RECAPTCHA_SITE_KEY",
    page_url="https://example.com/page-with-recaptcha"
)
print(token)
```

### API Server
```bash
# Start server
v3cap

# Alternative
python -m v3cap
```
Server runs on http://0.0.0.0:8000

### API Endpoints
- `POST /solve_recaptcha/`
  - Parameters: `site_key`, `page_url`
  - Returns: JSON with token

### Docker
```bash
docker build -t v3cap .
docker run -p 8000:8000 v3cap
```

## 📋 Requirements
- Python 3.10+
- Chrome/Chromium
- ChromeDriver

## ⚠️ Disclaimer
This tool is intended for educational and testing purposes only. Using this tool to circumvent reCAPTCHA on websites may violate their terms of service. Users are responsible for ensuring they have proper authorization to use this tool on any website. The author takes no responsibility for misuse of this software.

## 📄 License
MIT
