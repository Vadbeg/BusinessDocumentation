"""Module with database interactions"""

from typing import Tuple

import mysql.connector


def create_connection(host: str = 'localhost', port: str = '3306',
                      user: str = 'root', password: str = 'root',
                      database: str = 'documents') -> Tuple:
    """
    Creates connection to MySQL database
    It returns connection and cursor, because of weak connection problem.

    :url: https://stackoverflow.com/questions/1482141/what-does-it-mean-weakly-referenced-object-no-longer-exists
    :return: connection and cursor for mysql databse
    """

    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    cursor = connection.cursor()

    return connection, cursor


def close_connection(connection, cursor):
    """
    Closes cursor and connection

    :param connection: connection to mysql database
    :param cursor: cursor for given connection
    """

    connection.close()
    cursor.close()

