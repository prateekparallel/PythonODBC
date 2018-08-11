from ODBCUtil import columns 
from ODBCUtil import CommonODBC


def main(argv):
	try:
		#Here the first odbc object we will create for transaction in oracle database
		oracleODBCObject = CommonODBC(oracle_sid,userid,password,'oracle')
		# you can get the sid id with the below sql statement in sql prompt
		# SELECT sys_context('USERENV', 'SID') FROM DUAL;

		#now get the cursor first
		oracle_cursor = oracleODBC.getCursor()

		#now first execute a insert statement
		sql =("insert into Employee(EMP_ID, DESIGNATION, SALARY) values('%s','%s',%s)" % ('12345', 'MGR', 1200))
		oracle_cursor.execute(sql)
		oracle_cursor.doCommit()
		oracle_cursor.close()
		#Now we will execute a select statement
		oracle_cursor = oracleODBC.getCursor()
		sql=”select EMP_ID, DESIGNATION, SALARY from EMPLOYEE”
		oracle_cursor = oracleODBC.getCursor()
		oracle_cursor.loadCursor(sql)
		dataset = oracle_cursor.fetchall()
		
		if len(dataset) > 0:
			for row in dataset :
				records = columns(oracle_cursor, row)
				EMP_ID = records.EMP_ID
				DESIGNATION = records.DESIGNATION
				SALARY =  records.SALARY
				print("Employee ID :", EMP_ID)
				print("Designation :", DESIGNATION)
				print("Salary      :", SALARY)
		oracle_cursor.close()
	except:
		print("Exception while connecting to oracle")
		#now below example is for Microsoft sql server
		ms_sqldb = CommonDBConnectionObject(database_environment,userID,password,host_name)
		#To login with windows authentication
		#ms_sqldb = CommonDBConnectionObject(database_environment,"","",host_name,True)
		#now first execute a insert statement
		sql =("insert into Employee(EMP_ID, DESIGNATION, SALARY) values('%s','%s',%s)" % ('12345', 'MGR', 1200))
		mssql_cursor = ms_sqldb.getCursor()
		mssql_cursor.execute(sql)
		mssql_cursor.doCommit()
		mssql_cursor.close()
		sql="select EMP_ID, DESIGNATION, SALARY from EMPLOYEE"
		mssql_cursor = ms_sqldb.getCursor()
		mssql_cursor.loadCursor(sql)
		dataset = mssql_cursor.fetchall()
		
		if len(dataset) > 0:
			for row in dataset :
				records = columns(oracle_cursor, row)
				EMP_ID = records.EMP_ID
				DESIGNATION = records.DESIGNATION
				SALARY =  records.SALARY
				print("Employee ID :", EMP_ID)
				print("Designation :", DESIGNATION)
				print("Salary      :", SALARY)
		mssql_cursor.close()
	except:
		print("Exception while connecting to MS SQL Server")
		#the below example is for Sybase database
		# First create connection object
		CommonDBConnectionObject(database_environment,userid,password,host,port,"sybase")

		#now get the cursor first
		sybase_cursor = oracleODBC.getCursor()

		#now first execute a insert statement
		sql =("insert into Employee(EMP_ID, DESIGNATION, SALARY) values('%s','%s',%s)" % ('12345', 'MGR', 1200))
		sybase_cursor.execute(sql)
		sybase_cursor.doCommit()
		sybase_cursor.close()
		#Now we will execute a select statement
		sybase_cursor = oracleODBC.getCursor()
		sql="select EMP_ID, DESIGNATION, SALARY from EMPLOYEE"
		sybase_cursor = oracleODBC.getCursor()
		sybase_cursor.loadCursor(sql)
		dataset = sybase_cursor.fetchall()
		
		if len(dataset) > 0:
			for row in dataset :
				records = columns(oracle_cursor, row)
				EMP_ID = records.EMP_ID
				DESIGNATION = records.DESIGNATION
				SALARY =  records.SALARY
				print("Employee ID :", EMP_ID)
				print("Designation :", DESIGNATION)
				print("Salary      :", SALARY)
		sybase_cursor.close()
	except:
		print("Exception while connecting to Sybase Server")

if __name__ == "__main__":
    main(sys.argv)	
