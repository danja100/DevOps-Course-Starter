import pytest
from todo_app.view_model import ViewModel
import datetime
from todo_app.todo_item import TodoItem
import os
from dotenv import load_dotenv, find_dotenv


@pytest.fixture
def view_model():
    file_path = find_dotenv(".env.test")
    load_dotenv(file_path, override=True)

    _DEFAULT_ITEMS = [
        {
            "dateLastActivity": datetime.datetime(2021, 10, 7, 11, 32, 40, 452000),
            "id": 1,
            "name": "Todo Items",
            "status": "Not Started",
        },
        {
            "dateLastActivity": datetime.datetime(2021, 10, 7, 11, 32, 40, 452000),
            "id": 2,
            "name": "In Progress Items",
            "status": "In Progress",
        },
        {
            "dateLastActivity": datetime.datetime(3000, 10, 7, 11, 32, 40, 452000),
            "id": 3,
            "name": "Recent Done Items",
            "status": "Done",
        },
        {
            "dateLastActivity": datetime.datetime(2000, 10, 7, 11, 32, 40, 452000),
            "id": 4,
            "name": "Older Done Items",
            "status": "Done",
        },
    ]

    items = []
    for item in _DEFAULT_ITEMS:
        items.append(TodoItem(item))

    view_model = ViewModel(items)

    return view_model


def test_items(view_model):
    assert type(view_model.items) == list


def test_todo_items(view_model):
    assert len(view_model.todo_items) == 1
    for item in view_model.todo_items:
        assert item.status == "Not Started"


def test_doing_items(view_model):
    if len(view_model.doing_items) >= 1:
        for item in view_model.doing_items:
            assert item.status == "In Progress"
    else:
        assert view_model.doing_items == []


def test_done_items(view_model):
    if len(view_model.done_items) >= 1:
        for item in view_model.done_items:
            assert item.status == "Done"
    else:
        assert view_model.done_items == []


def test_show_all_done_items(view_model):
    assert len(view_model.done_items) <= 5


def test_recent_done_items(view_model):
    datetime_yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    for item in view_model.recent_done_items:
        assert (item.status == "Done") and (item.last_edited > datetime_yesterday)


def test_older_done_items(view_model):
    datetime_yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    for item in view_model.older_done_items:
        assert (item.status == "Done") and (item.last_edited < datetime_yesterday)
