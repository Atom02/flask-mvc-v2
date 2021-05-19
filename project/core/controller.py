from flask_classful import FlaskView
from flask import render_template,url_for,abort,g,make_response,Response
from project import app
from flask_wtf.csrf import generate_csrf
from core.MariaDB import MariaDB

class controller(FlaskView):
    connectDb = True
    defAcl = {
        "allow" : True,
        "action": "*",
        "matchCallback":None,
        "denyCallback":None,
        "roles": "*"
    }
    # aclDB = None
    layout = None
    pagedata = {}
    def before_request(self, name, *args, **kwargs):
        if self.innitDb == True and app.config['AUTOINITDB'] ==  True:
            if not hasattr(g,"db"):
                g.db = MariaDB()
        if self.layout is not None:
            app.config["layout"]=self.layout

        pass

    def after_request(self, name, resp):
        if hasattr(g,"db") and g.db.db is not None:
            g.db.close()

        # cookie to header flow cssrf    
        # csrf=generate_csrf()
        # resp.set_cookie('CSRF-TOKEN', csrf)
        
        return resp

    def render(self,page,data={}):
        pagedata = {}
        pagedata["pagedata"] =self.pagedata
        z = {**pagedata,**data}
        resp = make_response(render_template(page,**z))
        return resp