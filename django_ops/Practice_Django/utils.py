from pymongo import MongoClient, mongo_client
def get_db(db_name, host, port, username, password):
    client = MongoClient(
        port = int(port),
        username = username,
        password = password
    )
    db_handle = client['db_name']
    return db_handle, client