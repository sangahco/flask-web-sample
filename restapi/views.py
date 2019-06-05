import functools

from flask import Blueprint
from config import app_root

bp = Blueprint('routes', __name__, url_prefix=app_root)

@bp.route('/')
def index():
    return 'Index'