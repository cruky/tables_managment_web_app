from functools import wraps
import os

from werkzeug.security import check_password_hash
from flask import Blueprint, request, get_flashed_messages, render_template, \
    session, redirect, flash, url_for

from db_operations import User, get_session

auth_bp = Blueprint('auth_endpoints', __name__)
hash_algorithm = os.environ.get("HASH_ALGORITHM", "pbkdf2:sha512:250000")


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if session:
            return view(*args, **kwargs)
        else:
            return redirect(url_for('auth_endpoints.login'))

    return wrapped_view


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        messages = get_flashed_messages()
        return render_template('login.html', messages=messages)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db_session = get_session()

        user_data = db_session.query(User).filter(User.username == username).all()[0]

        if user_data:
            hashed_password = user_data.password

            if check_password_hash(hashed_password, password):
                session['user_id'] = user_data.id
                session['username'] = user_data.username
                return redirect(url_for('upload_file'))

        flash('Wrong user name or password')
        return redirect(url_for('auth_endpoints.login'))


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth_endpoints.login'))
