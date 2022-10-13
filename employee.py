"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salaryFlag, rate, jobCount, commissionType, commisionRate, contractNum):
        self.name = name
        self.salaryFlag = salaryFlag
        self.rate = rate
        self.commissionType = commissionType
        self.commisionRate = commisionRate
        self.jobCount=jobCount
        self.contractNum=contractNum
        

    def getSalary(self):
        pay=0
        if self.salaryFlag == "salary":
            pay=self.rate
        elif self.salaryFlag=="hourly":
            pay=self.rate*self.jobCount
        return pay

    def getBonus(self):
        pay=0
        if self.commissionType=="none":
            pass
        elif self.commissionType=="bonus":
            pay=self.commisionRate
        elif self.commissionType=="contract":
            pay=(self.commisionRate*self.contractNum)
        return pay
    
    def get_pay(self):
        pay = self.getSalary() + self.getBonus()
        return pay

    def __str__(self):
        contractString = f"monthly salary of {str(self.getSalary())}" if (self.salaryFlag=="salary") else f"contract of {str(self.jobCount)} hours at {str(self.rate)}/hour"
        if self.commissionType=="none":
            bonusString=""
        else:
            bonusString = f" and receives a bonus commission of {str(self.getBonus())}" if (self.commissionType=="bonus") else f" and receives a commission for {self.contractNum} contract(s) at {self.commisionRate}/contract"
        payString=f"{self.name} works on a {contractString}{bonusString}. Their total pay is {str(self.get_pay())}."
        print(payString)
        return payString


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee(name='Billie', salaryFlag="salary", rate=4000, jobCount=0, commissionType="none", commisionRate=0, contractNum=0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee(name='Charlie', salaryFlag="hourly", rate=25, jobCount=100, commissionType="none", commisionRate=0, contractNum=0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee(name='Renee', salaryFlag="salary", rate=3000, jobCount=0, commissionType="contract", commisionRate=200, contractNum=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee(name='Jan', salaryFlag="hourly", rate=25, jobCount=150, commissionType="contract", commisionRate=220, contractNum=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee(name='Robbie', salaryFlag="salary", rate=2000, jobCount=0, commissionType="bonus", commisionRate=1500, contractNum=0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee(name='Ariel', salaryFlag="hourly", rate=30, jobCount=120, commissionType="bonus", commisionRate=600, contractNum=0)
