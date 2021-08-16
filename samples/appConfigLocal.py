# mongodb = {
#     'db': 'mongodbname',
#     'host': 'mongodbhost',
# 	'port': 27017,
# 	'username':"mongodbusername",
#     'password':"mongodbpassword",
# 	'authentication_source':"admin",
# 	'connect': False
# }
mariadb ={
	"host":'mariadbhost',
	"port":3306,
	"user":'mariadbuser',
	"password":'mariadbpassword',
	"db":'mariadbname',
	"autoinit":True #wheather auto init per request
}

environment = 'development'

app_debug = True

cors_origin = "*"