import functools

from flask import Blueprint
from config import app_root

bp = Blueprint('routes', __name__, url_prefix=app_root)

# a simple page that says hello
@bp.route('/')
@bp.route('/hello')
def hello():
    return 'Hello, World!'