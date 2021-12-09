import csv
import employee as emp
import mysql.connector
from bs4 import BeautifulSoup

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Lotus2ibm",
  database = "musical"
)
with open('sql_queries.xml', 'r') as f:
    data = f.read()
bs_data = BeautifulSoup(data, 'xml')
sqlElement = bs_data.find('sql')
sql = sqlElement.text
print("got query string {}",sql)
mycursor = mydb.cursor()
with open('C:\\SampleData\\employees.csv', newline='\n') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data = emp.Employee(row['EMPLOYEE_ID'],row['FIRST_NAME'],row['LAST_NAME'],row['EMAIL'],row['PHONE_NUMBER'],row['HIRE_DATE'],row['JOB_ID'],row['SALARY'],row['COMMISSION_PCT'],row['MANAGER_ID'],row['DEPARTMENT_ID'])
        val = (data.employeeId,data.firstName,data.lastName,data.email,data.phoneNumber,data.hireDate,data.jobId,data.salary,data.commisionPct,data.managerId,data.departmentId)
        mycursor.execute(sql, val)
mydb.commit()
mycursor.close()
mydb.close()                           
