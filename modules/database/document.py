"""Module with interactions for document table"""

from typing import List, Dict


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

    def add_document(self, document_name: str, document_type: str,
                     date_of_creation: str, date_of_registration: str,
                     creators_ids: List[int], controllers_ids: List[int]):
        """
        For adding new document to database

        :param document_name: name of the document type
        :param document_type: name of the document type
        :param date_of_creation: date of document creation
        :param date_of_registration: date of document registration
        :param creators_ids: list of creators ids
        :param controllers_ids: list of controllers ids
        """

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

    def change_document(self, document_id: int, document_name: str, document_type: str,
                        date_of_creation: str, date_of_registration: str,
                        creators_ids: List[int], controllers_ids: List[int]):
        """
        Function for changing existing document in databse

        :param document_id: id of document to change
        :param document_name: name of the document type
        :param document_type: name of the document type
        :param date_of_creation: date of document creation
        :param date_of_registration: date of document registration
        :param creators_ids: list of creators ids
        :param controllers_ids: list of controllers ids
        """

        change_document_query = """
UPDATE document
SET document_name = %s, document_type = %s,
    date_of_creation=%s, date_of_registration=%s
WHERE document.id = %s;
        """

        val = [document_name, document_type, date_of_creation, date_of_registration, document_id]

        self.cursor.execute(change_document_query, val)
        self.connection.commit()

        self.__delete_all_document_controllers__(document_id=document_id)
        self.__delete_all_document_creators__(document_id=document_id)

        for curr_creator_id in creators_ids:
            self.__add_document_creator__(document_id=document_id, creator_id=curr_creator_id)

        for curr_controller_id in controllers_ids:
            self.__add_document_controller__(document_id=document_id, controller_id=curr_controller_id)

    def __add_document_creator__(self, document_id, creator_id):
        """
        Adds document creator to document_creator table

        :param document_id: id of the document
        :param creator_id: id of the creator
        """

        add_document_creator_query = """
INSERT INTO document_creator (document_id, creator_id)
VALUES (%s, %s)
        """

        val = [document_id, creator_id]

        self.cursor.execute(add_document_creator_query, val)
        self.connection.commit()

    def __delete_all_document_creators__(self, document_id):
        """
        Deletes all document creators by document_id

        :param document_id: id of the document
        """

        delete_all_document_creators_query = """
DELETE FROM document_creator
WHERE document_id = %s 
        """

        val = [document_id]

        self.cursor.execute(delete_all_document_creators_query, val)
        self.connection.commit()

    def __add_document_controller__(self, document_id, controller_id):
        """
        Adds document controller to document_controller table

        :param document_id: id of the document
        :param controller_id: id of the controller
        """

        add_document_controller_query = """
INSERT INTO document_controller (document_id, controller_id)
VALUES (%s, %s)
        """

        val = [document_id, controller_id]

        self.cursor.execute(add_document_controller_query, val)
        self.connection.commit()

    def __delete_all_document_controllers__(self, document_id):
        """
        Deletes all document controllers by document_id

        :param document_id: id of the document
        """

        delete_all_document_controllers_query = """
DELETE FROM document_controller
WHERE document_id = %s
        """

        val = [document_id]

        self.cursor.execute(delete_all_document_controllers_query, val)
        self.connection.commit()

    def __get_document_creators__(self, document_id) -> List[Dict]:
        """
        Gets all document creators by document_id

        :param document_id: id of the document
        :return: list of document creators (dicts with id, first_name, second_name)
        """

        get_all_document_creators_id_query = """
SELECT creator_id
FROM document_creator
WHERE document_id = %s
        """
        val = [document_id]

        self.cursor.execute(get_all_document_creators_id_query, val)
        all_document_creators_id = self.cursor.fetchall()

        # used it to flatten list of tuples
        # :url:  https://stackoverflow.com/questions/10632839/transform-list-of-tuples-into-a-flat-list-or-a-matrix
        all_document_creators_id = list(sum(all_document_creators_id, ()))

        get_all_document_creators_query = """
SELECT id, first_name, second_name
FROM user
WHERE user.id in (%s)
        """
        val = ', '.join(['%s'] * len(all_document_creators_id))
        get_all_document_creators_query = get_all_document_creators_query.replace('%s', val)

        self.cursor.execute(get_all_document_creators_query, all_document_creators_id)
        all_document_creators = self.cursor.fetchall()

        names = ['id', 'first_name', 'second_name']
        all_document_creators = [dict(zip(names, curr_document_creator))
                                 for curr_document_creator in all_document_creators]

        return all_document_creators

    def __get_document_controllers__(self, document_id):
        """
        Gets all document controllers by document_id

        :param document_id: id of the document
        :return: list of document controllers (dicts with id, first_name, second_name)
        """

        get_all_document_controllers_id_query = """
SELECT controller_id
FROM document_controller
WHERE document_id = %s
        """
        val = [document_id]

        self.cursor.execute(get_all_document_controllers_id_query, val)
        all_document_controllers_id = self.cursor.fetchall()

        # used it to flatten list of tuples
        # :url:  https://stackoverflow.com/questions/10632839/transform-list-of-tuples-into-a-flat-list-or-a-matrix
        all_document_controllers_id = list(sum(all_document_controllers_id, ()))

        get_all_document_controllers_query = """
        SELECT id, first_name, second_name
        FROM user
        WHERE user.id in (%s)
                """
        val = ', '.join(['%s'] * len(all_document_controllers_id))
        get_all_document_controllers_query = get_all_document_controllers_query.replace('%s', val)

        self.cursor.execute(get_all_document_controllers_query, all_document_controllers_id)
        all_document_controllers = self.cursor.fetchall()

        names = ['id', 'first_name', 'second_name']
        all_document_controllers = [dict(zip(names, curr_document_controller))
                                    for curr_document_controller in all_document_controllers]

        return all_document_controllers

    def get_all_documents(self) -> List[Dict]:
        """
        Returns all documents from database with controllers and creators

        :return: list of documents (with controllers and creators)
        """

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

    def get_document_by_id(self, document_id: int) -> Dict:
        """
        Finds document in database by its id and returns it (with controllers and creators).

        :param document_id: id of the document
        :return: document with give id (with controllers and creators)
        """

        get_all_documents_query = """
SELECT *
FROM document
WHERE document.id = %s
        """

        val = [document_id]

        self.cursor.execute(get_all_documents_query, val)
        document = self.cursor.fetchall()[0]

        document = dict(zip(self.COLUMNS_DOCUMENT, document))

        document['controllers'] = self.__get_document_controllers__(document['id'])
        document['creators'] = self.__get_document_creators__(document['id'])

        return document

    def get_document_by_date(self, document_n_days: int) -> List[Dict]:
        """
        Finds document in database if they were registered in last document_n_days days
        and returns it (with controllers and creators).

        :param document_n_days: number of days from dive date to the past
        :return: document with give id (with controllers and creators)
        """

        get_all_documents_query = """
SELECT *
FROM document
WHERE document.date_of_registration > DATE_SUB(now(), INTERVAL %s DAY)
        """

        val = [document_n_days]

        self.cursor.execute(get_all_documents_query, val)
        all_documents = self.cursor.fetchall()

        all_documents = [dict(zip(self.COLUMNS_DOCUMENT, curr_user)) for curr_user in all_documents]

        for curr_document in all_documents:
            curr_document['controllers'] = self.__get_document_controllers__(curr_document['id'])
            curr_document['creators'] = self.__get_document_creators__(curr_document['id'])

        return all_documents
