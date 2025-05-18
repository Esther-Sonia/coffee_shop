# Coffee Shop Domain Modeling

A Python application that models a Coffee Shop domain using object-oriented programming principles. The project demonstrates class design, object relationships, and data handling.

# Features

- **Customer Management**:
  - Create customers with validated names
  - Track all orders made by a customer
  - View all unique coffees a customer has ordered

- **Coffee Management**:
  - Create coffee items with validated names
  - Track all orders for each coffee
  - Calculate order statistics (count, average price)

- **Order System**:
  - Create orders linking customers to coffees
  - Validate order prices
  - Find top customers for specific coffees


## Project Structure
`coffee_shop/
│
├── customer.py # Customer class
├── coffee.py # Coffee class
├── order.py # Order class
├── debug.py # Manual print tests
├── tests/
│ ├── init.py
│ ├── test_customer.py
│ ├── test_coffee.py
│ └── test_order.py
└── README.md`


# To test a specific file
python -m pytest tests/test_customer.py

# Run all tests
pytest -x

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd coffee_shop

2. Set up virtual environment
pipenv install
pipenv shell

1. Install testing dependencies
pipenv install pytest


# Validation rules
Customer name must be a string with 1–15 characters

Coffee name must be a string with at least 3 characters

Order price must be between 1.0 and 10.0

