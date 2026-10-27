# Amazon Price Tracker

A Python application that monitors Amazon product prices and automatically sends an email notification when a product's price falls below a specified threshold.

## Features

- **Web Scraping:** Extracts product information from Amazon using Requests and Beautiful Soup.
- **Price Monitoring:** Compares the current product price against a predefined target.
- **Email Notifications:** Sends automated price-drop alerts using SMTP.
- **Environment Variables:** Supports secure management of email credentials.
- **Customizable Tracking:** Allows users to configure the product URL and desired price threshold.

## Technologies Used

- Python
- Requests
- Beautiful Soup 4
- HTML Parsing
- SMTP (smtplib)
- python-dotenv

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mhmd-mehrdad/amazon-price-tracker.git
cd amazon-price-tracker
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project's root directory using `.env.example` as a reference.

```dotenv
SMTP_ADDRESS=smtp.gmail.com
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
```

If using Gmail, generate an App Password for SMTP authentication rather than using your regular account password.

**Note:** The Python script must load these variables using the same names.

### 5. Configure Product Tracking

In your Python script, configure:

- **Product URL:** The Amazon product page you want to monitor.
- **Target Price:** The maximum price you're willing to pay.

### 6. Run the Application

```bash
python main.py
```

Replace `main.py` with your actual Python filename if different.

## How It Works

1. Sends an HTTP request to the configured Amazon product page.
2. Parses the HTML response using Beautiful Soup.
3. Extracts the product title and current price.
4. Compares the extracted price against the target price.
5. Sends an email notification when the price drops below the target.

## Project Structure

```text
amazon-price-tracker/
│
├── main.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Important Notes

- Amazon may modify its HTML structure, which can affect price extraction.
- Amazon may restrict automated requests.
- Email credentials should never be hardcoded or committed to GitHub.
- The script performs a price check when executed. Recurring monitoring requires a separate scheduler.

## Disclaimer

This project was created for educational purposes and is not affiliated with Amazon.

## Author

**Mehrdad Mohammadi**

GitHub: [@mhmd-mehrdad](https://github.com/mhmd-mehrdad)