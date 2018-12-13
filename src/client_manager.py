import pandas as pd


def get_clients(filepath):
    clients = pd.read_csv(filepath)
    return clients


def insert_client(client, filepath):
    required_fields = ["id", "first_name", "last_name", "email", "gender"]
    for requiered_field in required_fields:
        if requiered_field not in client:
            raise ValueError("Input data is incorrect!")

    client_str = "{},{},{},{},{}\n"\
        .format(client["id"], client["first_name"], client["last_name"], client["email"], client["gender"])

    with open(filepath, "a") as file_obj:
        file_obj.write(client_str)
