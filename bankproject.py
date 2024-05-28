class Bank:
    def __init__(self,name):
        self.name=name
        self.account={}
        
        




class Account:
    def __init__(self,name,accno,password):
        self.name=name
        self.accno=accno
        self.password=password
        self.bal=0
    def hello(self):
        return [self.name,self.accno,self.password,self.bal]
        







p=0
a=Bank("sbi")
while p!=5:
        print("\nOptions:")
        print("1. create a bank account")
        print("2. deposit ")
        print("3. withdraw")
        print("4. Display amount")
        print("5. Exit")
        p=int(input("enter your option"))
        if p==1:
            print("create your account")
            name=input("enter your name")
            accno =input("account no")
            password=input("password")
            b=Account(name,accno,password)
            a.account[name]=b.hello()  
            print(a.account)
            
        elif p==2:
            name=input("enter your name")
            if name in a.account:
                pas=input("enter your password")
                if pas in a.account[name]:
                    amount=int(input("enter your amount"))
                    a.account[name][3]+=amount
            else:
                print("invalid account")

            
        elif p==3:
            name=input("enter your name")
            if name in a.account:
                pas=input("enter your password")
                if pas in a.account[name]:
                    amount=int(input("enter your amount"))
                    a.account[name][3]-=amount
            else:
                print("invalid account")
        elif p==4:
            name=input("enter your name")
            if name in a.account:
                pas=input("enter your password")
                if pas in a.account[name]:
                    print(a.account[name][3])
                    
            else:
                print("invalid account")
        elif p==5:
            break
        else:
            print("invalid option")
