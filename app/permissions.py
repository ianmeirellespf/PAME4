from functools import wraps
from flask_jwt_extended import verify_jwt_in_request,  get_jwt



def self_professor_only():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args , **kwargs):

            verify_jwt_in_request()
            print("alegria")
            if 'professor' != get_jwt()['role']:

                return {'msg':'não autorizado'}
            print("depressao")

            return fn(*args , **kwargs)

        return decorator
    return wrapper

def self_aluno_only():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):

            verify_jwt_in_request()
            print(get_jwt()['role'].lower())
            if "aluno" != get_jwt()['role'].lower():	
                return {'msg': 'Unauthorized user'}, 403
            print("depressao")

            return fn(*args, **kwargs)

        return decorator

    return wrapper