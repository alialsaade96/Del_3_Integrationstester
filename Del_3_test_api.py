# Detta är en testkommentar för att trigga GitHub Actions

import requests
import pytest

BASE_URL = "https://fakestoreapi.com"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def test_get_products_status_code():
    response = requests.get(f"{BASE_URL}/products", headers=HEADERS)
    assert response.status_code == 200, f"API svarade med {response.status_code}"

def test_number_of_products():
    response = requests.get(f"{BASE_URL}/products", headers=HEADERS)
    assert response.status_code == 200, f"API svarade med {response.status_code}"
    data = response.json()
    assert isinstance(data, list), "Svaret är inte en lista"
    assert len(data) == 20, f"Förväntade 20 produkter, fick {len(data)}"

def test_specific_product_fields():
    response = requests.get(f"{BASE_URL}/products/1", headers=HEADERS)
    assert response.status_code == 200, f"API svarade med {response.status_code}"
    product = response.json()
    for field in ["title", "price", "category"]:
        assert field in product, f"Fältet '{field}' saknas i produktdata"

def test_specific_product_data():
    response = requests.get(f"{BASE_URL}/products/1", headers=HEADERS)
    assert response.status_code == 200, f"API svarade med {response.status_code}"
    product = response.json()
    assert product["id"] == 1, f"Produkt-ID är {product['id']}, förväntade 1"
    assert isinstance(product["title"], str), "Titel är inte en sträng"
    assert isinstance(product["price"], float), "Pris är inte ett flyttal"
