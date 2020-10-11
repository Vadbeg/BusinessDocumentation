"""Module with interactions for document table"""

from typing import List


class Document:
    COLUMNS_DOCUMENT = [
        'id', 'document_name', 'document_type',
        'date_of_creation', 'date_of_registration'
    ]

    COLUMNS_DOCUMENT_CREATOR = ['document_id', 'creator_id']
    COLUMNS_DOCUMENT_CONTROLLER = ['document_id', 'controller_id']

    def __init__(self, connection, cursor):
        """
        Class for faster interactions with document table

        :param connection: connection to database
        :param cursor: cursor for database
        """

        self.connection = connection
        self.cursor = cursor

    def add_document(self, document_name, document_type,
                     date_of_creation, date_of_registration,
                     creators_ids: List[int], controllers_ids: List[int]):
        add_document_query = """
INSERT INTO document (document_name, document_type, date_of_creation, date_of_registration)
VALUES (%s, %s, %s, %s)
        """

        val = [document_name, document_type, date_of_creation, date_of_registration]

        self.cursor.execute(add_document_query, val)
        self.connection.commit()

        document_id = self.cursor.lastrowid

        for curr_creator_id in creators_ids:
            self.__add_document_creator__(document_id=document_id, creator_id=curr_creator_id)

        for curr_controller_id in controllers_ids:
            self.__add_document_controller__(document_id=document_id, controller_id=curr_controller_id)

    def __add_document_creator__(self, document_id, creator_id):
        add_document_creator_query = """
INSERT INTO document_creator (document_id, creator_id)
VALUES (%s, %s)
        """

        val = [document_id, creator_id]

        self.cursor.execute(add_document_creator_query, val)
        self.connection.commit()

    def __add_document_controller__(self, document_id, controller_id):
        add_document_controller_query = """
INSERT INTO document_controller (document_id, controller_id)
VALUES (%s, %s)
        """

        val = [document_id, controller_id]

        self.cursor.execute(add_document_controller_query, val)
        self.connection.commit()

    def __get_document_creators__(self, document_id):
        get_all_document_creators_query = """
SELECT creator_id
FROM document_creator
WHERE document_id = %s
        """
        val = [document_id]

        self.cursor.execute(get_all_document_creators_query, val)
        all_document_creators_id = self.cursor.fetchall()

        # used it to flatten list of tuples
        # :url:  https://stackoverflow.com/questions/10632839/transform-list-of-tuples-into-a-flat-list-or-a-matrix
        all_document_creators_id = list(sum(all_document_creators_id, ()))

        return all_document_creators_id

    def __get_document_controllers__(self, document_id):
        get_all_document_controllers_query = """
SELECT controller_id
FROM document_controller
WHERE document_id = %s
        """
        val = [document_id]

        self.cursor.execute(get_all_document_controllers_query, val)
        all_document_controllers_id = self.cursor.fetchall()

        # used it to flatten list of tuples
        # :url:  https://stackoverflow.com/questions/10632839/transform-list-of-tuples-into-a-flat-list-or-a-matrix
        all_document_controllers_id = list(sum(all_document_controllers_id, ()))

        return all_document_controllers_id

    def get_all_documents(self):
        get_all_documents_query = """
SELECT *
FROM document
        """

        self.cursor.execute(get_all_documents_query)
        all_documents = self.cursor.fetchall()

        all_documents = [dict(zip(self.COLUMNS_DOCUMENT, curr_user)) for curr_user in all_documents]

        for curr_document in all_documents:
            curr_document['controllers'] = self.__get_document_controllers__(curr_document['id'])
            curr_document['creators'] = self.__get_document_creators__(curr_document['id'])

        return all_documents

