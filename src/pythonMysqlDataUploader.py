import mysql.connector
import pandas as pd
import employee as emp
from bs4 import BeautifulSoup

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Lotus2ibm",
  database = "musical"
)
# Read the file
df = pd.read_csv("C:\\SampleData\\employees.csv", low_memory=False,skiprows=0)
with open('sql_queries.xml', 'r') as f:
    data = f.read()
bs_data = BeautifulSoup(data, 'xml')
sqlElement = bs_data.find('sql')
sql = sqlElement.text
print("got query string {}",sql)
# Output the number of row.__getitem__(1)s
print("Total rows: {0}".format(len(df)))
mycursor = mydb.cursor()
for row in df.iterrows():
    data = emp.Employee(row.__getitem__(1)['EMPLOYEE_ID'],row.__getitem__(1)['FIRST_NAME'],row.__getitem__(1)['LAST_NAME'],row.__getitem__(1)['EMAIL'],row.__getitem__(1)['PHONE_NUMBER'],row.__getitem__(1)['HIRE_DATE'],row.__getitem__(1)['JOB_ID'],row.__getitem__(1)['SALARY'],row.__getitem__(1)['COMMISSION_PCT'],row.__getitem__(1)['MANAGER_ID'],row.__getitem__(1)['DEPARTMENT_ID'])
    val = (data.employeeId,data.firstName,data.lastName,data.email,data.phoneNumber,data.hireDate,data.jobId,data.salary,data.commisionPct,data.managerId,data.departmentId)
    print(val)
    mycursor.execute(sql, val)
mydb.commit()
mycursor.close()
mydb.close()