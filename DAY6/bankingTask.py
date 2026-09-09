class wrongdeposit(Exception):
    pass
class wrongwithdraw(Exception):
    pass
class Nametooshort(Exception):
    pass
class BankAccount:
    owner=""
    accountnumber = 0
    balance=0
    def __init__(self,owner,accountnumber):
        self.owner= owner
        self.accountnumber= accountnumber
    def displayBalance(self):
        return self.balance
    def deposit(self,amount):
        if(amount>0):
            self.balance+=amount
            print(f"your amount of {amount} is deposited")
        else:
            raise wrongdeposit("amount is less the zero")
    def withdraw(self,amount):
        if(amount>self.balance):
            raise wrongwithdraw("insufficient balance")
        else:
            self.balance-=amount
            print(f"your amount of {amount} is withdrawed")

owner = input("enter your user name :")
accountnumber = int(input("enter your accountnumber :"))
b1 = BankAccount(owner,accountnumber)
a = int(input("type 1 to withdraw, 2 to deposit, 3 to see balance, -1 to exit"))
try:
    while(a!=-1):
        if(a==-1):
            break;
        if(a==1):
            b = int(input("enter amount you wanna withdraw from you account"))
            b1.withdraw(b)
        elif(a==2):
            b = int(input("enter amount you wanna deposit from you account"))
            b1.deposit(b)
        elif(a==3):
            print(f"amount present in your account is :{b1.displayBalance()}")
        else:
            print("entered other then options")
        a = int(input("type 1 to withdraw, 2 to deposit, 3 to see balance, -1 to exit"))
    
except wrongdeposit as a:
    print(f"deposit error: {a}")

except wrongwithdraw as a :
    print(f"withdraw error: {a}")