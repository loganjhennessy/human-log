# /server.py

from functools import wraps
import json
from os import environ as env
from werkzeug.exceptions import HTTPException

from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from authlib.flask.client import OAuth
from six.moves.urllib.parse import urlencode

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'


oauth = OAuth(app)

auth0 = oauth.register(
    'auth0',
    client_id='SnBnggTkFNPW9tMYo475c3BOqWnDvemM',
    client_secret='toPSp0vdH3ZeW7-2eMSIeq6ahcQlhpEXMr9XUz9DVbMMEV3afPsMgv0b36HX1djb',
    api_base_url='https://loganjhennessy.auth0.com',
    access_token_url='https://loganjhennessy.auth0.com/oauth/token',
    authorize_url='https://loganjhennessy.auth0.com/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
)


def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    if 'profile' not in session:
      # Redirect to Login page here
      return redirect('/')
    return f(*args, **kwargs)

  return decorated


@app.route('/')
@app.route('/index')
def index():
    logged_in = session.get('profile') is not None
    return render_template('index.html', logged_in=logged_in)


@app.route('/callback')
def callback_handler():
    # Handles response from token endpoint
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()

    # Store the user information in flask session.
    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }
    return redirect('/index')


@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri='http://localhost/callback')


@app.route('/logout')
def logout():
    # Clear session stored data
    session.clear()
    # Redirect user to logout endpoint
    params = {'returnTo': url_for('index', _external=True), 'client_id': 'SnBnggTkFNPW9tMYo475c3BOqWnDvemM'}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))