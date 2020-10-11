"""Module with interactions for task table"""


class Task:
    COLUMNS_TASK = [
        'id', 'task_name',
        'executor_id', 'document_id',
    ]

    def __init__(self, connection, cursor):
        """
        Class for faster interactions with user table

        :param connection: connection to database
        :param cursor: cursor for database
        """

        self.connection = connection
        self.cursor = cursor

    def add_task(self, task_name, executor_id, document_id):
        add_user_query = """
INSERT INTO task (task_name, executor_id, document_id)
VALUES (%s, %s, %s)
        """

        val = [task_name, executor_id, document_id]

        self.cursor.execute(add_user_query, val)
        self.connection.commit()

    def get_all_tasks(self):
        get_all_tasks_query = """
SELECT *
FROM task
        """

        self.cursor.execute(get_all_tasks_query)
        all_tasks = self.cursor.fetchall()

        all_tasks = [dict(zip(self.COLUMNS_TASK, curr_user)) for curr_user in all_tasks]

        return all_tasks

