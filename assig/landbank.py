class Landbank:
    def __init__(self , bal , accname):
        self.__balance = bal
        self.__accountname = accname
    def deposit(self , amount):
        self.__balance += amount
    def withdraw(self , amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print "Error: Insufficient funds"
    def getbalance(self):
        return self.__balance
    def hoold(self , accname):
        self.__accountname = "landbank"
    def vname(self):
        return self.__accountname
    def changeinfo(self , accname):
        self.__accountname = accname
