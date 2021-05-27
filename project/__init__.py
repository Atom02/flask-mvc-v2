# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask,redirect,url_for
from flask_socketio import SocketIO
from flask_mobility import Mobility
from flask_session import Session
from flask_caching import Cache
from flask_wtf.csrf import CSRFProtect
from datetime import timedelta
from flask_cors import CORS
from flask_mail import Mail
# from flask_mongoengine import MongoEngine
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
import types
import os
import project.appConfig as cfgGlobal
import project.appConfigLocal as cfgLocal

app = Flask('project')

app.secret_key = 'somerandomandnonsenskey!@#$88'

app.config["NAME"]="APPNAME"
app.config['SECRET_KEY'] = app.secret_key
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024 #32 Mega

app.config['CACHE_KEY_PREFIX']='unuquecachekey'
app.config["CACHE_TYPE"]="simple"
app.config["CACHE_DEFAULT_TIMEOUT"]=600
app.config["CACHE_THRESHOLD"]=1000

app.config["SESSION_TYPE"]="filesystem"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)
app.config['SESSION_PERMANENT'] = True 

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config["ALLOWED_EXTENSIONS"] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_ORIGINS'] = "*" #allow form all

# app.config['MONGODB_SETTINGS'] = cfgLocal.mongodb

# app.config['SQLALCHEMY_DATABASE_URI'] = cfgLocal.mariadb
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_ENGINE_OPTIONS']={ "pool_pre_ping" : True}

app.config['MARIADB'] = cfg.DB
app.config['AUTOINITDB'] = cfg.DB['AUTOINIT']

# app.config['DEBUG'] = cfgLocal.appdebug

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config["ALLOWED_EXTENSIONS"] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['CORS_SUPPORTS_CREDENTIALS'] = True

# app.config['MAIL_SERVER']='your.mail.server.com'
# app.config['MAIL_PORT']=465
# app.config['MAIL_USERNAME']='youruser@mail.server.com'
# app.config['MAIL_PASSWORD']='p@ssword'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True

# app.debug = True
app.jinja_env.add_extension("project.helper.JinjaExt.RelativeInclude")
app.jinja_env.add_extension("jinja2.ext.do")

mail = Mail(app)
csrf = CSRFProtect(app)
Mobility(app)
socketio = SocketIO(app, cors_allowed_origins = ["*"])
cache = Cache(app)
# mongodb = MongoEngine(app)
# mariadb = SQLAlchemy(app)
# migrate = Migrate(app, mariadb)

CORS(app)
print(CORS)

# REGISTER YOUR SQLALCHEMY IF ANY

# REGISTER YOUR CLASSES
from project.controllers import *
SiteController.SiteView.register(app)