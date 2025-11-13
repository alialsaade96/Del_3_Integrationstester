# Detta är en testkommentar för att trigga GitHub Actions

import requests
import pytest

BASE_URL = "https://dummyjson.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/115.0.0.0 Safari/537.36"
}

def test_get_products_status_code():
    response = requests.get(f"{BASE_URL}/products", headers=HEADERS)
    assert response.status_code == 200, f"API svarade med {response.status_code}"

def test_number_of_products():
    response = requests.get(f"{BASE_URL}/products", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert "products" in data, "Nyckeln 'products' saknas"
    assert isinstance(data["products"], list), "Produkter är inte en lista"
    assert len(data["products"]) == 30, f"Förväntade 30 produkter, fick {len(data['products'])}"

def test_specific_product_fields():
    response = requests.get(f"{BASE_URL}/products/1", headers=HEADERS)
    assert response.status_code == 200
    product = response.json()
    for field in ["title", "price", "category"]:
        assert field in product, f"Fältet '{field}' saknas i produktdata"

def test_specific_product_data():
    response = requests.get(f"{BASE_URL}/products/1", headers=HEADERS)
    assert response.status_code == 200
    product = response.json()
    assert product["id"] == 1, f"Produkt-ID är {product['id']}, förväntade 1"
    assert isinstance(product["title"], str), "Titel är inte en sträng"
    assert isinstance(product["price"], (int, float)), "Pris är inte ett tal"
