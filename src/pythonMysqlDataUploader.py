import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Lotus2ibm",
  database = "musical"
)

print(mydb)
# Read the file
data = pd.read_csv("C:\\SampleData\\employees.csv", low_memory=False)
# Output the number of rows
print("Total rows: {0}".format(len(data)))
print("EMPLOYEE_ID: {0}",data.EMPLOYEE_ID)
print("FIRST_NAME: {0}",data.FIRST_NAME)
print("LAST_NAME: {0}",data.LAST_NAME)
print("EMAIL: {0}",data.EMAIL)
print("HIRE_DATE: {0}",data.HIRE_DATE)
print("JOB_ID: {0}",data.JOB_ID)
print("SALARY: {0}",data.SALARY)
print("COMMISSION_PCT: {0}",data.COMMISSION_PCT)
print("MANAGER_ID: {0}",data.MANAGER_ID)
print("DEPARTMENT_ID: {0}",data.DEPARTMENT_ID)



mycursor = mydb.cursor()

sql = "INSERT INTO EMPLOYEE(EMPLOYEE_ID,FIRST_NAME,LAST_NAME,EMAIL,HIRE_DATE,JOB_ID,SALARY,COMMISSION_PCT,MANAGER_ID,DEPARTMENT_ID) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val = (data.EMPLOYEE_ID, data.FIRST_NAME,data.LAST_NAME,data.EMAIL,data.HIRE_DATE,data.JOB_ID,data.SALARY,data.COMMISSION_PCT,data.MANAGER_ID,data.DEPARTMENT_ID)
#mycursor.executemany(sql, val)
#mydb.commit()
#mycursor.close()
#mydb.close()