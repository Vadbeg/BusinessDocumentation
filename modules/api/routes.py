from flask import (Blueprint, Flask,
                   render_template)

from modules.database.database_interactions import create_connection, close_connection
from modules.database.document import Document
from modules.database.user import User
from modules.database.task import Task


blue_print = Blueprint('Business documentation', __name__)
connection, cursor = create_connection()


@blue_print.route('/')
@blue_print.route('/home')
def home():
    return render_template('pages/home.html')


@blue_print.route('/users')
def show_users():
    user = User(connection=connection, cursor=cursor)

    all_users = user.get_all_users()

    context = {
        'all_users': all_users
    }

    return render_template('pages/tables/users.html', **context)


@blue_print.route('/documents')
def show_documents():
    document = Document(connection=connection, cursor=cursor)

    all_documents = document.get_all_documents()

    context = {
        'all_documents': all_documents
    }

    return render_template('pages/tables/documents.html', **context)



if __name__ == '__main__':
    blue_print.run(host='127.0.0.1', port='8000')
