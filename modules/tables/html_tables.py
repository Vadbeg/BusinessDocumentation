from flask_table import Table, Col


class UserTable(Table):
    first_name = Col('first_name')
    second_name = Col('second_name')

    is_internal_user = Col('is_internal_user')
    position = Col('position')

    email = Col('email')


if __name__ == '__main__':
    users = [
        dict(first_name='Vadim', second_name='Titko',
             is_internal_user=True, position='manager',
             email='vadbeg@tut.by')
    ]

    user_table = UserTable(users)

    print(user_table.__html__())



