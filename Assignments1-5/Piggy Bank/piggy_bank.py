user_dict = {"user":"password","mani":"kandan"}

class piggy_bank:    
    def __init__(self, balance):
        self.balance = balance
        print('-'*20+"Start"+'-'*20)
        self.initiateTransaction()
        
    def initiateTransaction(self):
        if(self.isValidCredential()) :
            print("Your credentials are valid.")
            while (self.bankingOperations()):
                pass               
        else:
            print("Please enter valid user name / password.")
        return
            
    def isValidCredential(self):
        user = input("Enter user name : ")
        password = input("Enter password : ")
        global user_dict
        for key in user_dict :
            if (user in user_dict and  user == key and password == user_dict[key]) :
                return True
            else: 
                return False
        
    
    def bankingOperations(self):
        txninput = input("Start or End  : ")
        if(txninput.lower() == 'start'):
            txntype = input("Add , Withdraw or Check  : ")
            if (txntype.lower() == 'add'):
                self.addMoney()
            elif (txntype.lower() == 'withdraw'):
                self.withdraw()
            elif (txntype.lower() == 'check'):
                self.checkBalance()
            else:
                print("Please enter valid operation.")
            return True
        else:
            print("Your Transaction is complete. Thank you for banking with us.")
            return False
        
        
    def addMoney(self):
        amount = input("Add amount : ")
        self.balance = str(int(self.balance)+ int(amount))
        print("After adding , your updated balance is "+ self.balance +" rupees")
    
    def withdraw(self):
        amount = input("Withdraw amount : ")
        self.balance = str(int(self.balance)- int(amount))
        print("After withdrawing, balance amount is "+ self.balance +" rupees")
    
    def checkBalance(self):
        print("Your current balance is "+str(self.balance)+ " rupees")

obj = piggy_bank(0)