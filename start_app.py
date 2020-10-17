"""Starting module of the app"""

import argparse

from modules.api import create_app
from modules.config import Config


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=f'Script for business documentation app starting.')

    parser.add_argument('--app-host', type=str, default='localhost', help='Host for the app')
    parser.add_argument('--app-port', type=int, default=4000, help='Port for the app')

    parser.add_argument('--database-host', type=str, default='localhost', help='Host for database')
    parser.add_argument('--database-port', type=int, default=3306, help='Port for database')
    parser.add_argument('--database-user', type=str, default='root', help='User of database')
    parser.add_argument('--database-password', type=str, default='root', help='Database password')
    parser.add_argument('--database-name', type=str, default='documents', help='Database name')

    args = parser.parse_args()

    app_host = args.app_host
    app_port = args.app_port

    database_host = args.database_host
    database_port = args.database_port
    database_user = args.database_user
    database_password = args.database_password
    database_name = args.database_name

    Config.database_host = database_host
    Config.database_port = database_port
    Config.database_user = database_user
    Config.database_password = database_password
    Config.database_name = database_name

    app = create_app()
    app.run(host=app_host, port=app_port)
