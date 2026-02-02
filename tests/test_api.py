from fastapi.testclient import TestClient
from app.api import app
import allure 

client = TestClient(app)

@allure.feature("Library API Tests")
@allure.story("Тест добавления книги")
def test_add_book():
    response = client.post("/books", params={"title": "Dune"})
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "title": "Dune"}

@allure.feature("Library API Tests")
@allure.story("Тест на добавление дубликата книги")
def test_add_duplicate_book():
    client.post("/books", params={"title": "Dune"})
    response = client.post("/books", params={"title": "Dune"})
    assert response.status_code == 400

@allure.feature("Library API Tests")
@allure.story("Тест на список книг")
def test_list_books():
    client.post("/books", params={"title": "1984"})
    response = client.get("/books")
    assert "books" in response.json()
    assert "1984" in response.json()["books"]

@allure.feature("Library API Tests")
@allure.story("Тест поиска книги")
def test_search():
    client.post("/books", params={"title": "Harry Potter"})
    response = client.get("/books/search", params={"query": "har"})
    assert response.json()["result"] == ["Harry Potter"]

@allure.feature("Library API Tests")
@allure.story("Тест на удаление книги")
def test_remove_book():
    client.post("/books", params={"title": "Test Book"})
    response = client.delete("/books", params={"title": "Test Book"})
    assert response.status_code == 200