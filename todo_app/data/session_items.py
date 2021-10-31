from flask import session
from dotenv import load_dotenv, find_dotenv
import os
from todo_app.todo_item import TodoItem
import pymongo
from datetime import datetime
import random

def get_client():
    connection_string = f"{os.getenv('MONGODB_PROTOCOL')}{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@{os.getenv('MONGODB_CLUSTER')}/{os.getenv('MONGODB_DB')}?retryWrites=true&w=majority"
    return pymongo.MongoClient(connection_string)


def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """

    collection = get_client().todo_app.items

    items = []
    for card in collection.find():
        items.append(TodoItem(card))

    return items


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    for item in items:
        if item.id == int(id):
            return item


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """

    data = {
        "status": "Not Started",
        "name": title,
        "dateLastActivity": datetime.now(),
        "id": random.randint(0, 1000),
    }
    collection = get_client.todo_app.items
    collection.insert_one(data)


def delete_item(item):
    collection = get_client.todo_app.items
    for card in collection.find():
        if item.id == card["id"]:
            collection.delete_one(card)


def mark_in_progress(item):
    collection = get_client.todo_app.items
    for card in collection.find():
        if item.id == card["id"]:
            newvalues = {"$set": {"status": "In Progress"}}
            collection.update_one(card, newvalues)


def mark_complete(item):
    collection = get_client.todo_app.items
    for card in collection.find():
        if item.id == card["id"]:
            newvalues = {"$set": {"status": "Done"}}
            collection.update_one(card, newvalues)
