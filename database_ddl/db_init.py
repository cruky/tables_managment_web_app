from datetime import datetime
import os
import secrets

import sqlite3
from werkzeug.security import generate_password_hash


hash_algorithm = "pbkdf2:sha512:250000"

def execute_script(cursor, script_file):
    with open(script_file, encoding='utf-8') as f:
        query = f.read()
    cursor.executescript(query)


if __name__ == '__main__':
    conn = sqlite3.connect('../tables_managment_web_app/assets_database.db')
    cursor = conn.cursor()

    execute_script(cursor, 'users_hashed_init.sql')
    execute_script(cursor, 'assets_init.sql')

    users_hashed_query = """
    INSERT INTO "users" ("username", "password") 
    VALUES (:username, :password);
    """
    test_user = {'username': "test", 'password': generate_password_hash("test", hash_algorithm)}

    conn.execute(users_hashed_query, test_user)

    assets_query = """
    INSERT INTO "assets" ("source_id", "type", "latitude", "longitude", "owner", "date") 
    VALUES (:source_id, :type, :latitude, :longitude, :owner, :date);
    """
    test_asset = {'source_id': "test", 'type': "Building", 'latitude': 54.3897, 'longitude': 18.5816, 'owner': "owner", 'date': datetime.now()}
    # '2019-01-01 10:00:00'
    conn.execute(assets_query, test_asset)

    conn.commit()
    conn.close()

    os.environ["SECRET_KEY"] = secrets.token_urlsafe()
    os.environ["HASH_ALGORITHM"] = hash_algorithm
