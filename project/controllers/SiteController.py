from flask import escape, session,render_template, request, Response, jsonify, make_response, abort, redirect, url_for, json, g
from flask_classful import route
from project import app
from project.core.controller import controller
# from project import alembic

class SiteView(controller):
	def index(self):
		return "OK"