from app.auth.controller import Login , TokenRefresh,MudaSenhaEmail,NovaSenhaFeita
from flask import Blueprint

auth_api = Blueprint("auth_api", __name__)

auth_api.add_url_rule('/login', view_func= Login.as_view('user_login'), methods = ['post'])
auth_api.add_url_rule('/tokenrefresh', view_func= TokenRefresh.as_view('user_tokenrefresh'), methods = ['Get'])
auth_api.add_url_rule('/esquecisenhaemail', view_func=MudaSenhaEmail.as_view('esquecisenha'), methods=['POST'])
auth_api.add_url_rule('/NovaSenhaFeita', view_func=NovaSenhaFeita.as_view('novasenhafeita'), methods=['PATCH'])