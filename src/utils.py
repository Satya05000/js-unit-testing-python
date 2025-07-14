# src/utils.py

def calculate_discount(price, discount):
    if price < 0 or discount < 0 or discount > 100:
        raise ValueError("Invalid input")
    return price - (price * discount / 100)
def filter_products(products, query):
    if not isinstance(products, list) or not isinstance(query, str):
        raise ValueError("Invalid input")

    return [product for product in products
            if query.lower() in product.get('name', '').lower()]
def sort_products(products, key):
    if not isinstance(products, list) or key not in ["name", "price"]:
        raise ValueError("Invalid input")

    return sorted(products, key=lambda product: product[key])
import re

def validate_email(email):
    if not isinstance(email, str):
        raise ValueError("Invalid input")
    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return re.match(email_regex, email) is not None