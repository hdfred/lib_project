import requests 

API_URL = 'https://example.com/books'

def fetch_book_from_api(book_id: int):
    response = requests.get(f"{API_URL}/{book_id}")
    response.raise_for_status()
    data = response.json()
    return data['title']