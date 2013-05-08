from flask import Flask 
from tools import return_json, login_required, get_user

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

@app.route('/')
def affairs():
  pass

@app.route('/manage')
def manage_affairs():
  pass


