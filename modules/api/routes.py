from flask import (Blueprint, Flask,
                   render_template,
                   request, abort,
                   redirect, url_for)

from modules.database.database_interactions import create_connection, close_connection
from modules.database.document import Document
from modules.database.user import User
from modules.database.task import Task

from modules.api.schemas import AddNewUser


blue_print = Blueprint('documentation', __name__)
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


@blue_print.route('/add_user', methods=("GET", "POST"))
def add_user():
    if request.method == 'POST':
        add_new_user_schema = AddNewUser()

        errors = add_new_user_schema.validate(data=request.form)

        if errors:
            abort(400, str(errors))

        args = add_new_user_schema.dump(request.form)

        user = User(connection=connection, cursor=cursor)
        user.add_user(
            first_name=args['first_name'],
            second_name=args['second_name'],
            is_internal=args['is_internal'],

            position=args['position'],
            email=args['email'],
            phone_number=args['phone_number']
        )

        return redirect(url_for('documentation.home'))

    return render_template('pages/inputs/add_user.html')


@blue_print.route('/add_document', methods=("GET", "POST"))
def add_document():
    if request.method == 'POST':
        # add_new_user_schema = AddNewUser()
        #
        # errors = add_new_user_schema.validate(data=request.form)
        #
        # if errors:
        #     abort(400, str(errors))
        #
        # args = add_new_user_schema.dump(request.form)
        #
        # user = User(connection=connection, cursor=cursor)
        # user.add_user(
        #     first_name=args['first_name'],
        #     second_name=args['second_name'],
        #     is_internal=args['is_internal'],
        #
        #     position=args['position'],
        #     email=args['email'],
        #     phone_number=args['phone_number']
        # )

        return redirect(url_for('documentation.home'))

    return render_template('pages/inputs/add_document.html')



