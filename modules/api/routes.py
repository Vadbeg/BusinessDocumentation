from flask import (Blueprint, Flask,
                   render_template)


blue_print = Blueprint('Business documentation', __name__)


@blue_print.route('/')
@blue_print.route('/home')
def home():
    return render_template('pages/home.html')


if __name__ == '__main__':
    blue_print.run(host='127.0.0.1', port='8000')
