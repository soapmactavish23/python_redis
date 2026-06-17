import pytest
from src.models.sqlite.repository.products_repository import ProductRepository
from src.models.sqlite.settings.connection import SqliteConnectionHandle

conn_handle = SqliteConnectionHandle()
conn = conn_handle.connect()

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_insert_product():
    repo = ProductRepository(conn)

    name = 'algumaCoisa'
    price = 12.34
    quantity = 8

    repo.insert_product(name, price, quantity)

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_find_product():
    repo = ProductRepository(conn)

    name = 'algumaCoisa2'
    response = repo.find_product_by_name(name)
    print(response)
    print(type(response))