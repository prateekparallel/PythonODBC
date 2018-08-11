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

	# We will call this method to load and get the reference of the cursor for database transaction
	def loadCursor(self,sqlstmt):
		cur = self.cnxn.cursor()
		cur.arraysize = 5000
		cur.execute(sqlstmt)
		return cur

    # This is an alternate method apart from above method for loading the cursor
	def getCursor(self):
		cur = self.cnxn.cursor()
		cur.arraysize = 5000
		return cur

	def doCommit(self):
		self.cnxn.commit()

	def doClose(self):
		self.cnxn.close()