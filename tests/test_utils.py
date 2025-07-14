# tests/test_utils.py

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils import (
    calculate_discount,
    filter_products,
    sort_products,
    validate_email
)

# ------------------- calculate_discount tests -------------------

def test_calculate_discount_valid():
    assert calculate_discount(100, 10) == 90

def test_calculate_discount_zero_discount():
    assert calculate_discount(200, 0) == 200

def test_calculate_discount_invalid_input():
    try:
        calculate_discount(-50, 10)
        assert False
    except ValueError:
        assert True

# ------------------- filter_products tests -------------------

def test_filter_products_valid():
    products = [
        {"name": "Apple iPhone", "price": 999},
        {"name": "Samsung Galaxy", "price": 899},
        {"name": "Google Pixel", "price": 799}
    ]
    result = filter_products(products, "iphone")
    assert len(result) == 1
    assert result[0]["name"] == "Apple iPhone"

def test_filter_products_case_insensitive():
    products = [{"name": "Laptop", "price": 1200}]
    result = filter_products(products, "laptop")
    assert len(result) == 1

def test_filter_products_no_match():
    products = [{"name": "Tablet", "price": 300}]
    result = filter_products(products, "phone")
    assert result == []

def test_filter_products_invalid_input():
    try:
        filter_products("not a list", 123)
        assert False
    except ValueError:
        assert True

# ------------------- sort_products tests -------------------

def test_sort_products_by_price():
    products = [
        {"name": "A", "price": 300},
        {"name": "B", "price": 100},
        {"name": "C", "price": 200}
    ]
    result = sort_products(products, "price")
    prices = [p["price"] for p in result]
    assert prices == [100, 200, 300]

def test_sort_products_by_name():
    products = [
        {"name": "Banana", "price": 1},
        {"name": "Apple", "price": 2},
        {"name": "Cherry", "price": 3}
    ]
    result = sort_products(products, "name")
    names = [p["name"] for p in result]
    assert names == ["Apple", "Banana", "Cherry"]

def test_sort_products_invalid_key():
    try:
        sort_products([{"name": "X", "price": 1}], "color")
        assert False
    except ValueError:
        assert True

def test_sort_products_invalid_input():
    try:
        sort_products("not a list", "price")
        assert False
    except ValueError:
        assert True

# ------------------- validate_email tests -------------------

def test_validate_email_valid():
    assert validate_email("test@example.com") == True
    assert validate_email("john.doe123@mail.co.uk") == True

def test_validate_email_invalid_format():
    assert validate_email("invalid-email") == False
    assert validate_email("missing@domain") == False
    assert validate_email("@nouser.com") == False
    assert validate_email("missing.com") == False

def test_validate_email_invalid_input_type():
    try:
        validate_email(12345)
        assert False
    except ValueError:
        assert True
