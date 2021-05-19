import pymysql
import pymysql.cursors
from pymysql.constants import FIELD_TYPE
from pymysql.converters import conversions as conv
from project import app
class MariaDB:
	def __init__(self,params=None,removeConv=True):
		self.open = False
		self.db = None
		self.removeConv = removeConv
		# print(config['DB'])
		if params is not None:
			self.params=params
		else:
			self.params=app.config['MARIADB']

		if self.params is not None:
			if removeConv:
				# print("REMOVE DATE OBJ")
				cf = conv.copy()
				# print(FIELD_TYPE)
				cf[246]=float
				del cf[FIELD_TYPE.DATE]
				del cf[FIELD_TYPE.DATETIME]
				del cf[FIELD_TYPE.TIME]
				del cf[FIELD_TYPE.TIMESTAMP]
				self.db = pymysql.connect(host=self.params['host'],port=self.params['port'],
						user=self.params['user'],
						password=self.params['password'],
						db=self.params['db'],
						cursorclass=pymysql.cursors.DictCursor,conv=cf)
			else:	
				print("USE DATE OBJ")
				cf = conv.copy()
				cf[246]=float
				self.db = pymysql.connect(host=self.params['host'],port=self.params['port'],
							user=self.params['user'],
							password=self.params['password'],
							db=self.params['db'],
							cursorclass=pymysql.cursors.DictCursor)
			self.open = True
			self.cur=self.db.cursor()
	
	def setDateAsString(self):
		self.__init__(self.params, True)
	
	def setDateAsObject(self):
		self.__init__(self.params, False)
		
	def reinit(self,removeConv=True):
		# print('REINIT DB')
		self.__init__(self.params, removeConv)

	def openDb(self):
		if self.removeConv:
			cf = conv.copy()
			del cf[FIELD_TYPE.DATE]
			del cf[FIELD_TYPE.DATETIME]
			del cf[FIELD_TYPE.TIME]
			self.db = pymysql.connect(host=self.params['host'],port=self.params['port'],
						user=self.params['user'],
						password=self.params['password'],
						db=self.params['db'],
						cursorclass=pymysql.cursors.DictCursor,conv=cf)
		else:
			self.db = pymysql.connect(host=self.params['host'],port=self.params['port'],
						user=self.params['user'],
						password=self.params['password'],
						db=self.params['db'],
						cursorclass=pymysql.cursors.DictCursor)
		self.open = True
	def getDb(self):
		if(self.open is False):
			# print("open db")
			self.openDb()
			self.cur=self.db.cursor()
		return self.cur
	def getCursor(self):
		if(self.open is False):
			# print("open db")
			self.openDb()
			self.cur=self.db.cursor()
		return self.cur
	def close(self):
		self.db.cursor().close()
		self.db.close()
		self.cur = None
		self.open = False

	def getCon(self):
		return self.db

	def commit(self):
		self.db.commit()
	def rollback(self):
		self.db.rollback()

		