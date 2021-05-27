import os
import random
import string
# from project import app
from flask import session,g
# from app.RBAC.AuthManager import AuthManager
import types
class User():
    # @staticmethod
    # def can(itemName,params={}):
    #     # print("USER SET")
    #     check = User.checkLogin()
    #     if not check:
    #         return False
    #     db = g.db
    #     user = User.get()
    #     auth = AuthManager(db)
    #     # print("CAN ",user["id"],permissionName)
    #     print("USER CAN",itemName,auth.checkAccess(user.id,itemName,params))
    #     return auth.checkAccess(user.id,itemName,params)
    
    @staticmethod
    def get():
        sid = "user"
        if sid not in session:
            return None
        f = types.SimpleNamespace()
        f.id = session[sid]['id']
        f.username = session[sid]['username']
        return f

    @staticmethod
    def set(id,username):
        session["user"]['id'] = id
        session["user"]['username'] = username
    
    @staticmethod
    def current():
        sid = "user"
        if sid not in session:
            return None
        return session["user"]

    @staticmethod
    def checkLogin():
        sid = "user"
        if sid not in session:
            return False
        return True

    @staticmethod
    def destroy():
        sid = "user"
        session.pop(sid)
        pass