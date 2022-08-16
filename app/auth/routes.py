from app.auth.controller import Login , TokenRefresh
from flask import Blueprint

auth_api = Blueprint("auth_api", __name__)

auth_api.add_url_rule('/login', view_func= Login.as_view('user_login'), methods = ['post'])
auth_api.add_url_rule('/tokenrefresh', view_func= TokenRefresh.as_view('user_tokenrefresh'), methods = ['Get'])