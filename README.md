# Smart Retail Management System

The Smart Retail Management System is a Python-based application designed to help small business owners manage their shops efficiently. It supports both a Grocery Store and a Stationery Store, with the following features:

- Secure login system with password and verification code
- Product tables with ID, name, price, stock quantity, and discount rules
- Automatic discounts applied based on purchase quantity
- Stock management with automatic updates after purchases
- Option to switch between grocery and stationery stores
- Delivery and payment options (home delivery or pick-up with different costs)
- Multi-currency support (USD, EUR, EGP)
- User-friendly graphical interface built with Tkinter

## Installation

Clone the repository and install the required dependencies:

# Clone this repository

`git clone https://github.com/omarimr64/smart-retail-management-system.git`

# Navigate into the project folder

`cd smart-retail-management-system`

# Create a virtual environment (optional but recommended)

`python -m venv venv`
`source venv/bin/activate` # On macOS/Linux
`venv\Scripts\activate` # On Windows

# Install dependencies from requirements.txt

`pip install -r requirements.txt`

## Project Structure

smart-retail-management-system/
│── main.py # Main entry point (handles business logic)
│── gui.py # Graphical User Interface (Tkinter)
│── user.py # User authentication and verification
│── requirements.txt # Project dependencies
│── README.md # Project documentation
│── assets/ # Images, icons, or other resources

## Project Images

[Login Screen](/assets/Login.png)
[Verification Screen](/assets/Verification.png)
[Grocery Store](/assets/Grocery.png)
[Stationary Store](/assets/Stationary.png)
[Cart Screen](/assets/Cart.png)

## Usage

Run the application with:

`python main.py`

## Features Summary

- Grocery Store:
  - Bulk discount: 5% per 250 units (up to 25%)
- Stationery Store:
  - Bulk discount: 2% per 50 units (up to 20%)
  <!-- - Delivery Options:
  - Home Delivery: +200 USD
  - Pick-up: +50 USD -->
- Currency Conversion:
  - USD, EUR, EGP supported

## Author

Developed by **Omar Mohamed Yousry**
Email: omarimr64@gmail.com
