import pandas as pd
import database as db


def get_by_id(id):
    return db.get_by_id(id)


def delete_by_id(id):
    db.delete_by_id(id)


def get_clients():
    clients = db.get_all()
    return clients


def update_by_id(id, new_person):
    db.update_by_id(id, new_person)
    return new_person
