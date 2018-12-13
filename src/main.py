from flask import Flask, request, abort

import client_manager as manager

app = Flask(__name__)
filepath = "../data/clients.csv"


@app.route("/clients", methods=["GET"])
def get():
    clients = manager.get_clients(filepath)
    return clients.to_json(orient="records")


@app.route("/clients", methods=["POST"])
def post():
    try:
        new_record = request.get_json()
        manager.insert_client(new_record, filepath)
    except Exception as ex:
        abort(400, ex)
    return "Record was successfully inserted."


if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = "9999"
    app.run(host=HOST, port=PORT)
