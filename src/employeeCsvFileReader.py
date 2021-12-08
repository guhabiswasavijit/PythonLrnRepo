import csv
import employee as emp
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Lotus2ibm",
  database = "musical"
)
mycursor = mydb.cursor()
with open('C:\\SampleData\\employees.csv', newline='\n') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data = emp.Employee(row['EMPLOYEE_ID'],row['FIRST_NAME'],row['LAST_NAME'],row['EMAIL'],row['PHONE_NUMBER'],row['HIRE_DATE'],row['JOB_ID'],row['SALARY'],row['COMMISSION_PCT'],row['MANAGER_ID'],row['DEPARTMENT_ID'])
        sql = "INSERT INTO EMPLOYEE(EMPLOYEE_ID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUMBER,HIRE_DATE,JOB_ID,SALARY,COMMISSION_PCT,MANAGER_ID,DEPARTMENT_ID) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (data.employeeId,data.firstName,data.lastName,data.email,data.phoneNumber,data.hireDate,data.jobId,data.salary,data.commisionPct,data.managerId,data.departmentId)
        mycursor.execute(sql, val)
mydb.commit()
mycursor.close()
mydb.close()                           
