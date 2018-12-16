import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-KVS4I5N;DATABASE=PythonPractice;UID=Test;PWD=123123')
cursor = cnxn.cursor()


def get_by_id(id):
    row = cursor.execute(f"SELECT * FROM Person WHERE Id = {id}").fetchall()
    if not len(row):
        return {"error": f"User with id {id} does not exists"}
    row = row[0]
    return {'id': row[0], 'first_name': row[1], 'last_name': row[2], 'email': row[3], 'gender': row[4]}


def delete_by_id(id):
    cursor.execute(f"DELETE FROM Person WHERE Id = {id}")


def get_all():
    result = cursor.execute("SELECT * FROM Person").fetchall()
    if not len(result):
        return {"error": f"User list is empty."}
    return [{'id': row[0], 'first_name': row[1], 'last_name': row[2], 'email': row[3], 'gender': row[4]} for row in result]

def to_str(expr):
    return f"'{expr}'"

def update_by_id(id, new_person):
    cursor.execute(f"UPDATE Person SET {', '.join([k + ' = ' + to_str(new_person[k]) for k in new_person.keys()])} "
                   f"WHERE Id = {id}")
