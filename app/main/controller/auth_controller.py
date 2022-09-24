from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth

@api.route('/login')
class UserLogin(Resource):
    """
    User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        post_data = request.json
        return Auth.login_user(data=post_data)

@api.route('/logout')
class UserLogout(Resource):
    """
    User LogOut Resource
    """
    @api.doc('logout a user')
    @api.doc(security='apikey')
    def post(self):
        #get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)