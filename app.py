from os import getenv
from flask import Flask

import psycopg2
from psycopg2 import sql


app = Flask(__name__)

@app.route('/')
def hello():
    # Informations de connexion
    hostname = getenv('hostname')
    port = getenv('hostname', '5432')
    username = getenv('username')
    password = getenv('password')
    database = getenv('database')

    # Établir la connexion
    try:
        connection = psycopg2.connect(
            host=hostname,
            port=port,
            user=username,
            password=password,
            dbname=database
        )
        cursor = connection.cursor()
        print("Connection to PostgreSQL success")

        # Exécuter une requête
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"Version : {db_version}")

        # Fermer le curseur et la connexion
        cursor.close()
        connection.close()
        print("Connection closed")

    except Exception as error:
        print(f"Erreur lors de la connexion à PostgreSQL : {error}")

    return f"Hello World! DB Version : {db_version}"

if __name__ == '__main__':
    port = getenv('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
