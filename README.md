# Business Documentation
Project for business documentation saving and editing

## Getting Started

To download project:
```
git clone https://github.com/Vadbeg/BusinessDocumentation.git
```


### Installing
To install all libraries you need, print in `BusinessDocumentation` directory: 

```
pip install -r requirements.txt
```

It will install all essential libraries

### Database setup

I've used MySQL database. If you want to play with this project you need to install it. 
And then execute script in `database` folder. Like this:

```
>> mysql -h hostname -u user < database/schemas.sql
```

### CLU Usage

After installation you can use this command to start app.

```
>> python start_app.py --help

usage: start_app.py [-h] [--app-host APP_HOST] [--app-port APP_PORT]
                    [--database-host DATABASE_HOST] [--database-port DATABASE_PORT] 
                    [--database-user DATABASE_USER] [--database-password DATABASE_PASSWORD] 
                    [--database-name DATABASE_NAME]

Script for business documentation app starting.

optional arguments:
  -h, --help            show this help message and exit
  --app-host APP_HOST   Host for the app
  --app-port APP_PORT   Port for the app
  --database-host DATABASE_HOST
                        Host for database
  --database-port DATABASE_PORT
                        Port for database
  --database-user DATABASE_USER
                        User of database
  --database-password DATABASE_PASSWORD
                        Database password
  --database-name DATABASE_NAME
                        Database name

```

Example of usage:

```
>> python start_app.py --app-host localhost --app-port 4000

 * Serving Flask app "modules.api" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://localhost:4000/ (Press CTRL+C to quit)
```

Now you can go to `http://localhost:4000/` and start using app.


## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [marshmallow](https://marshmallow.readthedocs.io/en/stable/) - For converting different non-python datatypes to python datatypes
* [MySQL](https://www.mysql.com) - Relational database management system used 


## Authors

* **Vadim Titko** aka *Vadbeg* - 
[LinkedIn](https://www.linkedin.com/in/vadim-titko-89ab16149) | 
[GitHub](https://github.com/Vadbeg/PythonHomework/commits?author=Vadbeg)
 