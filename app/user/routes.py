
from flask import Blueprint
from app.user.controler import UserPost, UserId, UserLogin

user_api = Blueprint("user_api", __name__)

user_api.add_url_rule("/criauser", view_func=UserPost.as_view("user_post"), methods=["POST"])
user_api.add_url_rule("/criauser/<int:id>", view_func=UserId.as_view("user_ids"), methods=["GET", "PUT", "PATCH", "DELETE"])
user_api.add_url_rule("/loginUser", view_func=UserLogin.as_view("user_login"), methods=["POST"])