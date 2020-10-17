from typing import Tuple
from datetime import datetime

import mysql.connector

from modules.database.user import User
from modules.database.document import Document


def create_connection(host: str = 'localhost', port: str = '3306',
                      user: str = 'root', password: str = 'Root_1234',
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


if __name__ == '__main__':
    connection, cursor = create_connection()

#     print(connection)
#     print(type(cursor))
#
#     select_all_documents = """
# SELECT *
# FROM document;
#     """
#     cursor.execute("SHOW TABLES")
#
#     for x in cursor:
#         print(x)
#
    # user = User(connection=connection, cursor=cursor)
    #
    # user.add_user(first_name='Vadim8',
    #               second_name='Titko1',
    #               is_internal=False,
    #               position='ML eng2ineer',
    #               email='vadbeg22@tut.by',
    #               phone_number='+375 25 5480062')
#
#     all_user = user.get_all_users()
#
#     print(all_user)

    document = Document(connection=connection, cursor=cursor)
    all_documents = document.get_all_documents()

    from pprint import pprint

    pprint(all_documents)

    # time = datetime.fromisoformat('Y-m-d H:i:s')

    # print(time)


