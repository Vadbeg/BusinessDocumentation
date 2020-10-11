"""Module with interactions for user table"""


class User:
    COLUMNS = [
        'id', 'first_name', 'second_name',
        'is_internal', 'position', 'email',
        'phone_number'
    ]

    def __init__(self, connection, cursor):
        """
        Class for faster interactions with user table

        :param connection: connection to database
        :param cursor: cursor for database
        """

        self.connection = connection
        self.cursor = cursor

    def add_user(self, first_name, second_name, is_internal, position, email, phone_number):
        add_user_query = """
INSERT INTO user (first_name, second_name, is_internal, position, email, phone_number)
VALUES (%s, %s, %s, %s, %s, %s)
        """

        val = [first_name, second_name, is_internal, position, email, phone_number]

        self.cursor.execute(add_user_query, val)
        self.connection.commit()

    def get_all_users(self):
        get_all_users_query = """
SELECT *
FROM user
        """

        self.cursor.execute(get_all_users_query)
        all_users = self.cursor.fetchall()

        all_users = [dict(zip(self.COLUMNS, curr_user)) for curr_user in all_users]

        return all_users

