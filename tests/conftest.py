import pytest
from app.api import app, library
from app.library import Library

@pytest.fixture(autouse=True)
def reset_library():
    library._books = []