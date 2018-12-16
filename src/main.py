from flask import Flask, request, abort, jsonify

import client_manager as manager

app = Flask(__name__)
filepath = "../data/clients.csv"


@app.route("/clients", methods=["GET"])
def get():
    clients = manager.get_clients()
    return jsonify(clients)


@app.route("/clients/<int:client_id>", methods=['GET'])
def get_by_id(client_id):
    client = manager.get_by_id(client_id)
    return jsonify(client)


@app.route("/clients/<int:client_id>", methods=["DELETE"])
def delete_by_id(client_id):
    manager.delete_by_id(client_id)
    return "Ok"


@app.route("/clients/<int:client_id>", methods=["POST"])
def update_by_id(client_id):
    print(request.get_json())
    return str(manager.update_by_id(client_id, request.get_json()))


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
