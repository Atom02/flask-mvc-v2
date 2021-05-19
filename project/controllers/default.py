from project import app,cache
from flask import Response,send_file,send_from_directory,abort,redirect,url_for,request,g
import os

@app.route("/")
def defaultroute():
    To_default=url_for("SiteView:index")
    return redirect(To_default)

# YOUR STATIC FILES IS CONFIGURE HERE
@app.route('/static/<path:filename>')
def custom_static(filename):
	fl = os.path.join(app.root_path,'static')
	return send_from_directory(fl,filename)

# this is run after all request completed
@app.teardown_appcontext
def teardown(error):
    # if hasattr(g,"db"):
    #     g.db.close()
    print("TEARDOWN")