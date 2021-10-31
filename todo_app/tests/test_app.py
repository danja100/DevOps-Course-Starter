import todo_app.app as app 
import pytest
from dotenv import load_dotenv, find_dotenv
import mongomock
import pymongo 
import datetime


@pytest.fixture
def client():
    file_path = find_dotenv(".env.test")
    load_dotenv(file_path, override=True)
    with mongomock.patch(servers=(("fakemongo.com", 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client


def test_index_page(client):
    collection = pymongo.MongoClient("mongodb://fakemongo.com").todo_app.items
    collection.insert_one(
        {
            "id": 1,
            "status": "Not Started",
            "name": "test",
            "dateLastActivity": datetime.datetime.now(),
        }
    )
    response = client.get("/")
    assert (response.status_code == 200) and ("test" in response.data.decode("utf-8"))
