from logging import captureWarnings
from flask_classful import FlaskView
from flask import render_template,url_for,abort,g,make_response,Response
from project import app
from flask_wtf.csrf import generate_csrf
from core.MariaDB import MariaDB
import traceback
import types

class controller(FlaskView):
    connectDb = True
    defaultAcl = {
        "allow" : True,
        "action": "*",
        "matchCallback":None,
        "denyCallback":None,
        "roles": "*"
    }
    acl = {
        "DB":app.config["DB"],
        "denyCallback":(lambda x,y: abort(403)),
        "rules":[]
    }
    aclDB = None
    layout = None
    pagedata = {}
    innitDb = True
    def behaviors(self):
        return {}

    def aclCheck(self,name):
        behaviors = self.behaviors()
        acl = {**self.acl,**behaviors}
        if not acl["rules"]:
            return True

    def activateDB(self,config):
        dbtype = config['dbtype'].lower()
        db = None
        if dbtype=='mariadb':
            db = MariaDB()
        return db
    def before_request(self, name, *args, **kwargs):
        if self.innitDb == True:
            if not hasattr(g,"db"):
                try:
                    activeDBS = app.config['ACTIVEDBS']
                    if len(activeDBS) == 1:
                        g.db = self.activateDB(activeDBS[0])
                    else: 
                        g.db = types.SimpleNamespace()
                        for d in activeDBS:
                            setattr(g.db, d.lower(), self.activateDB(d))
                except Exception as e:
                    # activeDBS = app.config['ACTIVEDBS']
                    # if len(activeDBS) == 1:
                    g.db = None
                    traceback.print_exc()
        else:
            g.db = None
        if self.layout is not None:
            app.config["layout"]=self.layout
        pass

    def after_request(self, name, resp):
        activeDBS = app.config['ACTIVEDBS']
        if len(activeDBS) == 1:
            if hasattr(g,"db") and g.db.db is not None:
                g.db.close()
        else:
            for db in g.db.items():
                db.close()        
        return resp

    def render(self,page,data={}):
        pagedata = {}
        pagedata["pagedata"] =self.pagedata
        z = {**pagedata,**data}
        resp = make_response(render_template(page,**z))
        return resp