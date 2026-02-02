from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.api import app
import allure 

client = TestClient(app)


@allure.feature("External API Tests")
@allure.story("Тест получения книги из внешнего API")
def test_get_book_from_external():
    # Создаём мок объекта ответа requests.get
    mock_response = MagicMock()
    mock_response.json.return_value = {"title": "Mocked Book"}
    mock_response.raise_for_status.return_value = None

    # Патчим requests.get внутри модуля external_api
    with patch("app.external_api.requests.get", return_value=mock_response):
        response = client.get("/external/123")

    assert response.status_code == 200
    assert response.json() == {"title": "Mocked Book"}