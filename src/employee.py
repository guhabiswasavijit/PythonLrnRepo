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
        self.commisionPct = commisionPct
        self.salary = salary
        self.managerId = managerId
        self.departmentId = departmentId
        self.commisionPct = commisionPct
        Employee.all_employee.append(self)
    @classmethod
    def getEmployee() -> Employees:
        return  Employee.all_employee
        
