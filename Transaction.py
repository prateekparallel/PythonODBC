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
		print("Connection issue")

if __name__ == "__main__":
    main(sys.argv)	
