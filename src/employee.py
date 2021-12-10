import numpy as np

class Employees(list):
    def search(self, name) -> list:
        matching_employee = []
        for employee in self:
            if name in employee.firstName:
                matching_employee.append(employee)
        return matching_employee
  
class Employee:
    all_employee = Employees()

    def __init__(self, employeeId,firstName,lastName,email,phoneNumber,hireDate,jobId,salary,commisionPct,managerId,departmentId):
        self.employeeId = employeeId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email 
        self.phoneNumber=phoneNumber       
        self.hireDate = hireDate
        self.jobId = jobId
        self.salary = salary
        self.commisionPct = 0 if np.isnan(commisionPct) else commisionPct
        self.salary = salary
        self.managerId = 0 if np.isnan(managerId) else managerId
        self.departmentId = 0 if np.isnan(departmentId) else departmentId
        Employee.all_employee.append(self)
    @classmethod
    def getEmployee() -> Employees:
        return  Employee.all_employee
        
