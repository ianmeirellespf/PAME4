from functools import wraps
from flask_jwt_extended import verify_jwt_in_request,  get_jwt

def self_aluno_only():
    def wrapper(fn):
        @wrapper(fn)
        def decorator(*args , **kwargs):

            verify_jwt_in_request()

            if 'aluno ' != get_jwt()['role_user']:
                return {'msg':'não autorizado'}

            return fn(*args , **kwargs)

        return decorator
    return wrapper

def self_professor_only():
    def wrapper(fn):
        @wrapper(fn)
        def decorator(*args , **kwargs):

            verify_jwt_in_request()

            if 'professor' != get_jwt()['role_user']:
                return {'msg':'não autorizado'}

            return fn(*args , **kwargs)

        return decorator
    return wrapper