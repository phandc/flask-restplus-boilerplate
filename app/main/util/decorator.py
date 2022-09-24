from functools import wraps
from flask import request 

from app.main.service.auth_helper import Auth


def token_required(f):
    @wraps(f) #update decorated(wrapper) function has document like f(wrapped) function
    def decorated(*arg, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        userCredentials = data.get('data')

        if not userCredentials:
            return data, status #Error

        return f(*arg, **kwargs)

    return decorated

def admin_token_required(f):
    @wraps(f)
    def decorated(*arg, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        userCredentials = data.get('data')

        if not userCredentials:
            return data, status #Error

        admin = userCredentials.get('admin')
        if not admin:
            response_object = {
                'status': 'fail',
                'message': 'admin token required'
            }
            return response_object, 401

        return f(*arg, **kwargs)

    return decorated
