import functools
from flask import Flask,jsonify,request,g
from settings.settings import Settings
import jwt

def login_required(func):
    @functools.wraps(func)
    def secure_login(*args, **kwargs):

        auth=True
        header=request.headers.get('Authorization')
        
        if not(header) or ("Bearer " not in header):
            auth=False
        else:
            try:
                token=header.split(" ")[1]
                payload=jwt.decode(token,Settings.secretKey,algorithms=['HS256'])
                user_role = payload['role']
                print(user_role)

            except jwt.exceptions.InvalidSignatureError as err:
                 auth=False
                 print(err)

        if auth==False or user_role == 'member':
            #checks for valid JWT token or role is member, if either or is true, deny access to web API
            msg={"Message":"Not Authorized!"}
            return jsonify(msg),403

        return func(*args, **kwargs)

    return secure_login