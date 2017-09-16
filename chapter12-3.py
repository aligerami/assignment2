import os
class Account:
    def __init__(self,id=0,balance=100,annual_interest_rate=0):
        self.__id=id
        self.__balance=balance
        self.__annual_interest_rate=annual_interest_rate
    def get_balance(self):
        return self.__balance
    def set_balance(balance):
        self.__balance=balance
    def set_id(id):
        self.__id=id
    def get_id(self):
        return self.__id
    def get_annual_interest_rate():
        return annual_interest_rate
    def set_annual_interest_rate(annual_interest_rate):
        self.__annual_interest_rate=annual_interest_rate
    def get_monthly_interest_rate(self):
        return self.__annual_interest_rate/1200
    def get_monthly_interest(self):
        return self.__balance*self.get_monthly_interest_rate()
    def withdraw(self,amount):
        self.__balance=self.__balance-amount
    def deposit(self,amount):
        self.__balance=self.__balance+amount  
def main():
    account_list=[]
    for i in range(0,10):
        account_list.append(Account(i,100))
    while True:
        n=int(input("Enter an account id:"))
        if(n>=len(account_list)):
            print("Account Id is not correct please try again")
            continue
        while True:
            os.system('cls')
            os.system('clear')
            print("")
            user_request=int(input("Main menu\n1: check balance\n2: withdraw\n3: deposit\n4: exit"))
            print("")
            if(user_request==1):
                print(account_list[n].get_balance())
            if(user_request==2):
                amount=int(input("enter withdraw amount: "))
                account_list[n].withdraw(amount)
                print("request successfully done.")

            if(user_request==3):
                amount=int(input("enter withdraw amount: "))
                account_list[n].deposit(amount)
                print("request successfully done.")
            if(user_request==4):
                break
            print()
                
                
                
main()
    
    
    
    
    
    
    
    
    
    