import datetime
import time
import cx_Oracle
import pyodbc

class CommonODBC(object):
	# This is the init method through which we will create the object and initialized the object
	#with required fields to connect to a particular database
	
	def __init__(self,dbName,username,password,server,port=1433,driver='sql',winauthen=False):
		
		if(server=="oracle"):
			self.driver = server
		else:
			self.driver = driver

		if(self.driver=="oracle"):
			connectionString = username + "/" + password + "@" + dbName
		elif(self.driver=="sybase"):
			driver= '{Adaptive Server Enterprise}'
			connectionString = (('DRIVER='+driver+';PORT='+port+';SERVER='+server+';PORT='+port+';DATABASE='+dbName+';UID='+username+';PWD='+ password))
		elif(self.driver=="sql"):
			driver= '{SQL Server}'
			if(winauthen == True):
				connectionString = (('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+dbName+';Trusted_Connection=yes;'))
			else:
				connectionString = (('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+dbName+';UID='+username+';PWD='+ password))

		print(connectionString)
		
		if(self.driver=="oracle"):
			self.cnxn = cx_Oracle.connect(connectionString)
		else:
			self.cnxn = pyodbc.connect(connectionString)
